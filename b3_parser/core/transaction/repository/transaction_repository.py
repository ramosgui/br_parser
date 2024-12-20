from typing import List

from b3_parser.core.transaction.model.transaction_model import TransactionModel
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser


class TransactionRepository:

    def __init__(self, xlsx_parser: XLSXParser):
        self._raw_transactions = xlsx_parser.get_xlsx_content()

    def get_transactions(self, product_ids: List[str]) -> List[TransactionModel]:
        transactions = []
        for raw_trx in self._raw_transactions:
            product_id = raw_trx['product'].split(' - ')[0]
            if product_id in product_ids:
                model = TransactionModel(product_id=product_id, raw_transaction=raw_trx)
                # print(f"product_id: {model.product_id}, type: {model.type}, in/out: {model.in_out}, qtd: {model.qtd}, unit_price: {model.unit_price}"
                #       f", total_price: {model.total_price}, date: {model.date}")
                transactions.append(model)
        return transactions
