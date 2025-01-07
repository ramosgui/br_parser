from typing import List

from b3_parser.core.position.calculator.position_calculator import PositionCalculator
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class PositionModel:

    def __init__(self, product_id: str, transactions: List[TransactionModel], position_calculator: PositionCalculator):
        self.product_id = product_id
        self._transactions = transactions
        self._position_calculator = position_calculator

    @property
    def qtd(self) -> int:
        return self._position_calculator.calculate_quantity()

    @property
    def pm(self) -> float:
        return self._position_calculator.calculate_pm()

    @property
    def proventos(self) -> float:
        return self._position_calculator.calculate_proventos()

    @property
    def proventos_by_month(self):
        return self._position_calculator.calculate_provento_by_month()