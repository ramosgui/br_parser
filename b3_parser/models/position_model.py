from typing import List

from b3_parser.models.transaction_model import TransactionModel


class PositionModel:

    def __init__(self, product_id: str, transactions: List[TransactionModel]):
        self.product_id = product_id

        self._transactions = transactions

        self.pm = None
        self.type = "" # se é FII, açoes...

    @property
    def qtd(self):
        return self._get_qtd()

    def _get_qtd(self):
        for trx in self._transactions:
            print(trx)
