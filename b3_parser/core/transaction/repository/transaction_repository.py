from typing import List
import os
import json

from b3_parser.core.transaction.model.transaction_model import TransactionModel
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser


class TransactionRepository:

    def __init__(self, xlsx_parser: XLSXParser):
        self._raw_transactions = xlsx_parser.get_xlsx_content()

    def get_hardcoded_transactions(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), "hardcoded_transactions.json")
            with open(file_path, 'r', encoding='utf-8') as file:
                hardcoded_transactions = json.load(file)

                for trx in hardcoded_transactions:
                    trx['total_price'] = trx['unit_price'] * trx['qtd']

            return hardcoded_transactions
        except FileNotFoundError:
            print("hardcoded_transactions.json não encontrado.")
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
        return []

    def get_transactions(self, product_ids: List[str]) -> List[TransactionModel]:
        transactions = []

        all_transactions = self.get_hardcoded_transactions()
        all_transactions.extend(self._raw_transactions)

        for raw_trx in all_transactions:
            product_id = raw_trx['product'].split(' - ')[0]
            if product_id in product_ids:
                model = TransactionModel(product_id=product_id, raw_transaction=raw_trx)
                transactions.append(model)

        return transactions
