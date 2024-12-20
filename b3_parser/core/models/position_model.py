from typing import List

from b3_parser.constants import ALLOWED_PRODUCTS
from b3_parser.core.models.transaction_model import TransactionModel


class PositionModel:

    def __init__(self, product_id: str, transactions: List[TransactionModel]):
        self.product_id = product_id

        self._transactions = transactions

        self._pm = 0
        self._qtd = 0
        self._total_price = 0
        self._pm = 0

    @property
    def qtd(self) -> int:
        last_transfer = None
        for trx in self._transactions:
            if trx.type in ['empréstimo'] and trx.in_out == 'in':
                last_transfer = trx
            elif trx.type in ['transferência - liquidação', 'atualização']:
                if last_transfer:
                    last_transfer = None
                elif trx.in_out == 'in':
                    self._qtd += trx.qtd
                else:
                    self._qtd -= trx.qtd
        return self._qtd

    @property
    def pm(self) -> float:
        qtd = 0
        total_price = 0

        subscricoes = []
        last_transfer = None
        for trx in self._transactions:
            if trx.type in ['direitos de subscrição - exercido']:
                subscricoes.append(trx)
            elif trx.type in ['empréstimo'] and trx.in_out == 'in':
                last_transfer = trx
            elif trx.type in ['atualização']:
                for sub in subscricoes:
                    if sub.qtd == trx.qtd and not sub.total_price:
                        qtd += trx.qtd
                        total_price = qtd * self._pm
                    elif sub.qtd == trx.qtd and sub.total_price:
                        qtd += trx.qtd
                        total_price += sub.total_price

            elif trx.type == 'transferência - liquidação':
                if last_transfer:
                    last_transfer = None
                elif trx.in_out == 'in':
                    qtd += trx.qtd
                    if trx.total_price:
                        total_price += trx.total_price
                        self._pm = total_price / qtd
                    else:
                        total_price = qtd * self._pm
                else:

                    qtd -= trx.qtd
                    total_price -= (trx.qtd * self._pm)

                    try:
                        self._pm = total_price / qtd
                    except ZeroDivisionError:
                        self._pm = 0
                        total_price = 0

            # if trx.type in ['transferência - liquidação', 'atualização', 'direitos de subscrição - exercido', 'empréstimo']:
            # # if trx.type not in ['rendimento', 'transferência']:
            #     print(trx._raw_transaction)
            #     print(qtd)
            #     print(total_price)
            #     print(self._pm)
            #     print(trx.type)

        return round(self._pm, 2)

    @property
    def type(self) -> str:
        return ALLOWED_PRODUCTS[self.product_id]['type']
