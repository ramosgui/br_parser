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
        qtd = self._position_calculator.calculate_quantity()
        return int(qtd) if self.type == 'Ações' else qtd

    @property
    def pm(self) -> float:
        return self._position_calculator.calculate_pm()

    @property
    def type(self) -> str:
        return ALLOWED_PRODUCTS[self.product_id]['type']

    @property
    def ideal(self) -> float:
        return ALLOWED_PRODUCTS[self.product_id]['ideal']
