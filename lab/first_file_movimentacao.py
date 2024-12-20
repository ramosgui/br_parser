from datetime import datetime

import pandas as pd
import json
import glob
import warnings

# Suprimir o aviso do openpyxl sobre estilo padrão
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def format_columns_corrected(df):

    if 'Data' in df.columns:
        df['dt'] = pd.to_datetime(df['Data'], dayfirst=True).dt.strftime('%Y-%m-%d')

    # Renomear múltiplas colunas de uma vez
    df = df.rename(columns={
        "Entrada/Saída": "operation",
        "Produto": "product",
        "Quantidade": "qtd",
        "Preço unitário": "unit_price",
        "Valor da Operação": "total_price",
        "Movimentação": "type"
    })

    # Remover colunas desnecessárias
    df = df.drop(columns=['Data', 'Instituição', 'Mercado', 'Prazo/Vencimento'], errors='ignore')

    return df


def load_and_format_data_from_directory(directory_path):
    # Caminho para todos os arquivos no diretório especificado
    file_pattern = f'{directory_path}/*.xlsx'

    # Lista para armazenar os DataFrames de todos os arquivos
    all_records = []

    # Processar cada arquivo no diretório
    for file in glob.glob(file_pattern):
        df = pd.read_excel(file, sheet_name='Movimentação', engine='openpyxl')
        df = format_columns_corrected(df)
        all_records.append(df)

    # Concatenar todos os DataFrames
    if all_records:
        combined_df = pd.concat(all_records).drop_duplicates()
        if 'dt' in combined_df.columns:
            combined_df = combined_df.sort_values(by='dt', ascending=False)
        return combined_df
    else:
        return pd.DataFrame()  # Retorna um DataFrame vazio se nenhum arquivo for encontrado


def format_content_to_json(raw_content):
    # Converter o DataFrame para JSON
    json_data = raw_content.to_dict(orient='records')
    return json_data

def inserir_json_na_planilha(json_data, arquivo_planilha, aba="Planilha1"):
    """
    Insere os dados de uma estrutura JSON em uma planilha Excel.

    :param json_data: Lista de dicionários com os dados.
    :param arquivo_planilha: Caminho para o arquivo Excel.
    :param aba: Nome da aba da planilha onde os dados serão inseridos. Default: "Sheet1".
    """
    # Carregar a planilha existente
    try:
        planilha = pd.ExcelFile(arquivo_planilha)
    except Exception as e:
        print(f"Erro ao carregar a planilha: {e}")
        return

    # Verificar se a aba existe
    if aba not in planilha.sheet_names:
        print(f"A aba '{aba}' não foi encontrada na planilha.")
        return

    # Carregar a aba existente
    df_existente = planilha.parse(aba)

    # Criar um DataFrame a partir dos dados JSON
    df_novo = pd.DataFrame(json_data)

    # Garantir a ordem das colunas
    colunas_ordenadas = [
        "Data operação", "Categoria", "Código Ativo", "Operação C/V",
        "Quantidade", "Preço unitário", "Corretora", "Corretagem",
        "Taxas", "Impostos", "IRRF"
    ]

    for coluna in colunas_ordenadas:
        if coluna not in df_novo.columns:
            df_novo[coluna] = None  # Adicionar colunas ausentes com valores vazios

    df_novo = df_novo[colunas_ordenadas]  # Reordenar as colunas

    # Salvar os dados na planilha, sobrescrevendo a aba
    with pd.ExcelWriter(arquivo_planilha, engine="openpyxl", mode="w") as writer:
        df_novo.to_excel(writer, index=False, sheet_name=aba)

    print(f"Dados inseridos com sucesso na aba '{aba}'.")


if __name__ == '__main__':
    # Diretório contendo os arquivos
    directory_path = '../b3_parser/files/movimentacao'

    # Carregar e processar os dados de todos os arquivos no diretório
    combined_df = load_and_format_data_from_directory(directory_path)

    # Converter para JSON
    json_output = format_content_to_json(combined_df)

    formatted_trxs = []

    for trx in json_output:

        product = trx['product'].split(' - ')[0]

        if trx['qtd'] == 0:
            continue

        if 'RURA' in product:
            trx['product'] = 'RURA11'
        # elif 'XPML' in product:
        #     trx['product'] = 'XPML11'
        # elif 'KNCR' in product:
        #     trx['product'] = 'KNCR11'
        else:
            continue

        if trx['total_price'] == '-':
            # if trx['type'] == 'Transferência - Liquidação':
            #     print('SEM PREÇO', trx)
            continue


        if trx['type'] not in ['Direitos de Subscrição - Exercido', 'Transferência - Liquidação']:
            print(trx['type'], trx['qtd'])
            continue

        # else:
        #     print(trx['type'])


        trx['Operação C/V'] = 'C' if trx['operation'] == 'Credito' else 'V'
        trx['Código Ativo'] = trx['product']
        trx['Quantidade'] = trx['qtd']
        try:
            trx['Preço unitário'] = str(round(trx['total_price']/trx['qtd'], 2)).replace('.',',')
        except:
            continue
        trx['Corretora'] = 'ITAU CV S/A'

        if trx['product'] in ['HGLG11', 'AFHI11', 'FIIB11', 'XPML11', 'KNRI11', 'ALZR11', 'HGCR11', 'KNCR11']:
            trx['Categoria'] = 'Fundos imobiliários'
        elif trx['product'] in ['RURA11']:
            trx['Categoria'] = 'Fiagros'

        trx['Data operação'] = datetime.strptime(trx['dt'], "%Y-%m-%d").strftime("%d/%m/%Y")

        if trx['type'] == 'Direitos de Subscrição - Exercido':
            trx['Operação C/V'] = 'C'

        del trx['product']
        del trx['operation']
        del trx['dt']
        del trx['qtd']
        del trx['unit_price']
        del trx['total_price']
        del trx['type']

        # print(trx)

        formatted_trxs.append(trx)


    json_output = formatted_trxs

    inserir_json_na_planilha(json_output, 'importacao.xlsx')

    # Exibir uma amostra do JSON ou salvar
    # print(json.dumps(json_output, ensure_ascii=False, indent=4))
