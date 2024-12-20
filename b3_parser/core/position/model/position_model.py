from typing import List

from b3_parser.constants import ALLOWED_PRODUCTS
from b3_parser.core.position.calculator.position_calculator import PositionCalculator
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class PositionModel:

    def __init__(self, product_id: str, transactions: List[TransactionModel], position_calculator: PositionCalculator):
        self.product_id = product_id
        self._transactions = transactions
        self._position_calculator = position_calculator

    @property
    def qtd(self) -> int:
        qtd = 0
        transfers = []
        for trx in self._transactions:
            if trx.type in ['empréstimo'] and trx.in_out == 'in':
                if trx.qtd:
                    transfers.append(trx)
                else:
                    try:
                        transfers.pop(0)
                    except IndexError:
                        pass
            elif trx.type in ['bonificação em ativos']:
                qtd += trx.qtd
            elif trx.type in ['leilão de fração']:
                qtd -= trx.qtd
            elif trx.type in ['transferência - liquidação', 'atualização']:
                if transfers:
                    transfers.pop(0)
                elif trx.in_out == 'in':
                    qtd += trx.qtd
                else:
                    qtd -= trx.qtd
            elif trx.type in ['desdobro']:
                qtd += trx.qtd

        if self.type == 'Ações':
            return int(qtd)

        return qtd

    @property
    def new_qtd(self) -> int:
        qtd = self._position_calculator.calculate_quantity()
        return int(qtd) if self.type == 'Ações' else qtd

    @property
    def new_pm(self) -> float:
        return self._position_calculator.calculate_pm()

    @property
    def pm(self) -> float:
        qtd = 0
        total_price = 0
        pm = 0

        subscricoes = []
        transfers = []
        for trx in self._transactions:
            if trx.type in ['direitos de subscrição - exercido']:
                subscricoes.append(trx)
            elif trx.type in ['empréstimo'] and trx.in_out == 'in':
                if trx.qtd:
                    transfers.append(trx)
                else:
                    try:
                        transfers.pop(0)
                    except IndexError:
                        pass

            elif trx.type in ['atualização'] and self.type == 'Ações':
                qtd += trx.qtd
                total_price += pm * trx.qtd

            elif trx.type in ['atualização']:
                for sub in subscricoes:
                    if sub.qtd == trx.qtd and not sub.total_price:
                        qtd += trx.qtd
                        total_price = qtd * pm
                    elif sub.qtd == trx.qtd and sub.total_price:
                        qtd += trx.qtd
                        total_price += sub.total_price

            elif trx.type in ['bonificação em ativos', 'desdobro']:
                qtd += trx.qtd
                if trx.total_price:
                    total_price += trx.total_price

            elif trx.type in ['leilão de fração']:
                qtd -= trx.qtd
                total_price += trx.total_price

            elif trx.type == 'transferência - liquidação':

                if transfers:
                    transfers.pop(0)
                elif trx.in_out == 'in':
                    qtd += trx.qtd
                    if trx.total_price:
                        total_price += trx.total_price
                    else:
                        total_price = qtd * pm
                else:
                    qtd -= trx.qtd
                    total_price -= (trx.qtd * pm)

            try:
                pm = total_price / qtd
            except ZeroDivisionError:
                pm = 0
                total_price = 0

            # if trx.type in ['empréstimo']:
            # # if trx.type in ['transferência - liquidação', 'atualização', 'direitos de subscrição - exercido', 'empréstimo']:
            # # if trx.type not in ['rendimento', 'transferência', 'juros sobre capital próprio', 'dividendo',
            # # #                     'juros sobre capital próprio - transferido', 'reembolso']:
            #     print("####")
            #     print(len(transfers))
            #     print(trx._raw_transaction)
            #     print(trx.type)
            #     print(qtd)
            #     print(total_price)
            #     print(self._pm)

        return round(pm, 2)

    @property
    def type(self) -> str:
        return ALLOWED_PRODUCTS[self.product_id]['type']

    @property
    def ideal(self) -> float:
        return ALLOWED_PRODUCTS[self.product_id]['ideal']
