from typing import List

from b3_parser.core.position.calculator.update_strategy.position_strategy_factory import PositionStrategyFactory
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class PositionCalculator:
    """
    Classe responsável por calcular a posição (quantidade e preço médio) a partir de uma lista de transações.
    Aplica diferentes estratégias de acordo com o tipo da transação.
    """
    def __init__(self, transactions: List[TransactionModel], transfer):
        self._transfer = transfer
        self._transactions = transactions

    def calculate_quantity(self) -> int:
        qtd = 0
        total_price = 0
        transfer = []
        for trx in self._transactions:
            strategy = PositionStrategyFactory.get_strategy(type_=trx.type, transfer=transfer)
            if strategy:
                qtd, total_price = strategy.apply(trx, qtd, total_price)
        return qtd

    def calculate_pm(self) -> float:
        qtd = 0
        total_price = 0
        transfer = []

        for trx in self._transactions:
            strategy = PositionStrategyFactory.get_strategy(type_=trx.type, transfer=transfer)
            if strategy:
                qtd, total_price = strategy.apply(trx, qtd, total_price)
        return round(total_price / qtd, 2) if qtd > 0 else 0.0