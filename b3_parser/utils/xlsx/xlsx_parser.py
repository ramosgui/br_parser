import glob
import os
from typing import List

import pandas as pd
from pandas import DataFrame

from b3_parser.constants import ROOT_FILEPATH

XLSXFILE_PATH = os.path.join(ROOT_FILEPATH, 'files', 'xlsx', '*')


class XLSXParser:

    def __init__(self):
        self._MAP_COLUMNS = {
            "Entrada/Saída": "operation",
            "Produto": "product",
            "Quantidade": "qtd",
            "Preço unitário": "unit_price",
            "Valor da Operação": "total_price",
            "Movimentação": "type",
            "Data": "dt"
        }
        self._COLUMN_TO_DROP = ['Instituição', 'Mercado', 'Prazo/Vencimento']

    @staticmethod
    def _sort_content(all_records: List[DataFrame]):
        if all_records:
            combined_df = pd.concat(all_records).drop_duplicates()
            if 'dt' in combined_df.columns:
                combined_df = combined_df.sort_values(by='dt', ascending=False)
            return combined_df
        else:
            return pd.DataFrame()

    def _format_columns(self, df):
        df = df.rename(columns=self._MAP_COLUMNS)
        df['dt'] = pd.to_datetime(df['dt'], dayfirst=True).dt.strftime('%Y-%m-%d')
        df = df.drop(columns=self._COLUMN_TO_DROP, errors='ignore')
        return df

    def get_xlsx_content(self) -> List[dict]:
        all_records = []
        for file in glob.glob(XLSXFILE_PATH):
            df = pd.read_excel(file, sheet_name='Movimentação', engine='openpyxl')
            df = self._format_columns(df)
            all_records.append(df)
        sorted_results = self._sort_content(all_records)
        return sorted_results.to_dict(orient='records')
