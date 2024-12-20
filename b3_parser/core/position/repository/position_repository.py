from typing import List

from b3_parser.constants import ALLOWED_PRODUCTS
from b3_parser.core.position.calculator.position_calculator import PositionCalculator
from b3_parser.core.position.model.position_model import PositionModel
from b3_parser.core.transaction.repository.transaction_repository import TransactionRepository


class PositionRepository:

    def __init__(self, transaction_repository: TransactionRepository, position_calculator: PositionCalculator):
        self._transaction_repository = transaction_repository
        self._position_calculator = position_calculator

    def get_all_positions(self) -> List[PositionModel]:
        set_products = set()
        for k, v in ALLOWED_PRODUCTS.items():
            set_products.update(set(v['tickets']))

        positions = []
        for product_id in ALLOWED_PRODUCTS.keys():
            product_ids = ALLOWED_PRODUCTS[product_id]['tickets']
            transactions = self._transaction_repository.get_transactions(product_ids=product_ids)
            sorted_transactions = sorted(transactions, key=lambda x: (x.date, x.type))

            self._position_calculator.initialize_transactions(sorted_transactions)
            position_model = PositionModel(product_id=product_id, transactions=sorted_transactions, position_calculator=self._position_calculator)
            positions.append(position_model)

        return positions
