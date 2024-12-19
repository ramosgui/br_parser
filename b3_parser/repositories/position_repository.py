from typing import List

from b3_parser.models.position_model import PositionModel
from b3_parser.repositories.transaction_repository import TransactionRepository


class PositionRepository:

    def __init__(self, transaction_repository: TransactionRepository):
        self._transaction_repository = transaction_repository

    def get_positions(self, product_ids: List[str]) -> List[PositionModel]:
        positions = []
        for product_id in product_ids:
            transactions = self._transaction_repository.get_transactions(product_id=product_id)
            position_model = PositionModel(product_id=product_id, transactions=transactions)
            positions.append(position_model)
        return positions
