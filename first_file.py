import pandas as pd
import json
import glob
import warnings

# Suprimir o aviso do openpyxl sobre estilo padrão
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def format_columns(df):
    # Verifica se a coluna de data existe e formata para yyyy-mm-dd
    if 'Data' in df.columns:
        df['dt'] = pd.to_datetime(df['Data'], dayfirst=True).dt.strftime('%Y-%m-%d')
        df = df.drop(columns=['Data'])  # Remove a coluna 'Data'

    # Renomeia a coluna 'Entrada/Saída' para 'in_out' se existir
    if "Entrada/Saída" in df.columns:
        df = df.rename(columns={"Entrada/Saída": "in_out"})

    df = df.rename(columns={"Quantidade": "qtd"})
    df = df.rename(columns={"Preço unitário": "unit_price"})
    df = df.rename(columns={"Produto": "product"})
    df = df.rename(columns={"Valor da Operação": "total_price"})
    df = df.rename(columns={"Movimentação": "operation"})
    df = df.drop(columns=['Instituição'])

    return df


def get_files_content():
    # Caminho para a pasta contendo os arquivos
    folder_path = 'files/*.xlsx'

    # Lista para armazenar todos os registros
    all_records = []

    # Loop para carregar cada arquivo Excel na pasta especificada
    for file_path in glob.glob(folder_path):
        # Carregar o arquivo Excel
        df = pd.read_excel(file_path, sheet_name='Movimentação', engine='openpyxl')

        # Limpar e adicionar os dados ao registro
        records = df.dropna(subset=['Movimentação', 'Produto'])

        # Formatar as colunas relevantes
        records = format_columns(records)

        all_records.append(records)

    # Concatenar todos os registros em um único DataFrame e remover duplicatas
    combined_df = pd.concat(all_records).drop_duplicates()

    # Ordenar o DataFrame pela coluna 'dt' em ordem decrescente, se 'dt' existir
    if 'dt' in combined_df.columns:
        combined_df = combined_df.sort_values(by='dt', ascending=False)

    return combined_df


def format_content_to_json(raw_content):
    # Converter o DataFrame para JSON
    json_data = raw_content.to_dict(orient='records')

    # Exibir o JSON sem duplicações
    print(json.dumps(json_data, ensure_ascii=False, indent=2))

    print(len(json_data))


if __name__ == '__main__':
    combined_df = get_files_content()
    format_content_to_json(combined_df)
