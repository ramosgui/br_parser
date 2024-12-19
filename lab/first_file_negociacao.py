import pandas as pd
import json
import glob
import warnings

# Suprimir o aviso do openpyxl sobre estilo padrão
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def format_columns_corrected(df):
    # Verifica se a coluna de data existe e formata para yyyy-mm-dd
    if 'Data do Negócio' in df.columns:
        df['dt'] = pd.to_datetime(df['Data do Negócio'], dayfirst=True).dt.strftime('%Y-%m-%d')

    # Renomear múltiplas colunas de uma vez
    df = df.rename(columns={
        "Tipo de Movimentação": "operation",
        "Código de Negociação": "product",
        "Quantidade": "qtd",
        "Preço": "unit_price",
        "Valor": "total_price",
        "Mercado": "market",
        "Prazo/Vencimento": "maturity"
    })

    # Remover colunas desnecessárias
    df = df.drop(columns=['Data do Negócio', 'Instituição'], errors='ignore')

    return df


def load_and_format_data_from_directory(directory_path):
    # Caminho para todos os arquivos no diretório especificado
    file_pattern = f'{directory_path}/*.xlsx'

    # Lista para armazenar os DataFrames de todos os arquivos
    all_records = []

    # Processar cada arquivo no diretório
    for file in glob.glob(file_pattern):
        # Carregar o arquivo Excel usando a aba correta
        df = pd.read_excel(file, sheet_name='Negociação', engine='openpyxl')
        # Formatar as colunas
        formatted_df = format_columns_corrected(df)
        all_records.append(df)

    # Concatenar todos os DataFrames
    if all_records:
        combined_df = pd.concat(all_records).drop_duplicates()
        if 'dt' in combined_df.columns:
            combined_df = combined_df.sort_values(by='dt', ascending=False)
        return combined_df
    else:
        return pd.DataFrame()  # Retorna um DataFrame vazio se nenhum arquivo for encontrado

    return all_records


def format_content_to_json(raw_content):
    # Converter o DataFrame para JSON
    json_data = raw_content.to_dict(orient='records')
    return json.dumps(json_data, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    # Caminho do arquivo
    file_path = '/mnt/data/negociacao-2024-11-20-13-30-57.xlsx'

    # Carregar e processar os dados
    combined_df = load_and_format_data_from_directory(file_path)

    # Converter para JSON
    json_data = format_content_to_json(combined_df)

    # Salvar em arquivo ou exibir
    print(json.dumps(json_data, ensure_ascii=False, indent=2))  # Exibir os primeiros 1000 caracteres do JSON
