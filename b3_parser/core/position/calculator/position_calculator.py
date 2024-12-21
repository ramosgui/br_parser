from typing import List

from b3_parser.core.position.calculator.update_strategy.position_strategy_factory import PositionStrategyFactory
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class PositionCalculator:
    """
    Classe responsável por calcular a posição (quantidade e preço médio) a partir de uma lista de transações.
    Aplica diferentes estratégias de acordo com o tipo da transação.
    """
    def __init__(self):
        self._position_transactions = None

    def initialize_transactions(self, position_transactions: List[TransactionModel]):
        self._position_transactions = position_transactions

    def calculate_quantity(self) -> int:
        if not self._position_transactions:
            raise Exception('Necessário inicializar as transações da posição primeiramente.')

        qtd = 0
        total_price = 0
        transfer = []
        subs = []

        for trx in self._position_transactions:
            strategy = PositionStrategyFactory.get_strategy(type_=trx.type, transfer=transfer, subscricoes=subs,
                                                            in_out=trx.in_out)
            if strategy:
                qtd, total_price = strategy.apply(trx, qtd, total_price)

        return qtd

    def calculate_pm(self) -> float:
        if not self._position_transactions:
            raise Exception('Necessário inicializar as transações da posição primeiramente.')

        qtd = 0
        total_price = 0
        transfer = []
        subs = []

        for trx in self._position_transactions:
            strategy = PositionStrategyFactory.get_strategy(type_=trx.type, transfer=transfer, subscricoes=subs,
                                                            in_out=trx.in_out)
            if strategy:
                qtd, total_price = strategy.apply(trx, qtd, total_price)
        return round(total_price / qtd, 2) if qtd > 0 else 0.0
