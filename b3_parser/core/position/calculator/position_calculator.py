from collections import namedtuple

from typing import List

from b3_parser.core.position.calculator.update_strategy.position_strategy_factory import PositionStrategyFactory
from b3_parser.core.position.calculator.update_strategy.strategies.provento_strategy import ProventoPositionStrategy
from b3_parser.core.transaction.model.transaction_model import TransactionModel

TotalMonthMapping = namedtuple('TotalMonthMapping', ['dt', 'total_price'])

class PositionCalculator:
    """
    Classe responsável por calcular a posição (quantidade e preço médio) a partir de uma lista de transações.
    Aplica diferentes estratégias de acordo com o tipo da transação.
    """
    def __init__(self, position_transactions: List[TransactionModel]):
        self._position_transactions = position_transactions

    def calculate_quantity(self) -> int:
        qtd = 0
        total_price = 0
        transfer = set()
        subs = []

        for trx in self._position_transactions:
            strategy = PositionStrategyFactory.get_strategy(type_=trx.type, transfer_control=transfer, subscricoes=subs,
                                                            in_out=trx.in_out)
            if strategy:
                qtd, total_price = strategy.apply(trx, qtd, total_price)

                # print(trx._raw_transaction, qtd)

        return round(qtd, 6)

    def calculate_pm(self) -> float:
        qtd = 0
        total_price = 0
        transfer = set()
        subs = []

        for trx in self._position_transactions:
            strategy = PositionStrategyFactory.get_strategy(type_=trx.type, transfer_control=transfer, subscricoes=subs,
                                                            in_out=trx.in_out)
            if strategy:
                qtd, total_price = strategy.apply(trx, qtd, total_price)

        return round(total_price / qtd, 2) if qtd > 0 else 0.0

    def calculate_proventos(self) -> float:
        total_price = 0
        strategy = ProventoPositionStrategy()
        for trx in self._position_transactions:
            _, total_price = strategy.apply(trx=trx, qtd=0, total_price=total_price)
        return round(total_price, 2)

    def calculate_provento_by_month(self) :
        strategy = ProventoPositionStrategy()
        month_mapping = {}

        for trx in self._position_transactions:
            month_mapping = strategy.month_total_price(trx=trx, month_mapping=month_mapping)
        return month_mapping
