from typing import List

from b3_parser.core.position.calculator.position_calculator import PositionCalculator
from b3_parser.core.position.model.position_model import PositionModel
from b3_parser.core.transaction.repository.transaction_repository import TransactionRepository


class PositionRepository:

    def __init__(self, transaction_repository: TransactionRepository):
        self._transaction_repository = transaction_repository

    def get_all_positions(self) -> List[PositionModel]:
        transactions = self._transaction_repository.get_transactions()
        all_product_ids = {x.product_id for x in transactions}

        allowed_product_ids = []
        for product_id in all_product_ids:
            if len(product_id) == 6 and product_id[-2:] in ['12', '13', '14']:
                pass
            else:
                allowed_product_ids.append(product_id)

        positions = []
        for product_id in allowed_product_ids:
            if len(product_id) == 6 and product_id[-2:] == '11':
                product_ids = [product_id[0:4]+x for x in ['11', '12', '13', '14']]
            else:
                product_ids = [product_id]
            transactions = self._transaction_repository.get_transactions_by_product_ids(product_ids)
            sorted_transactions = sorted(transactions, key=lambda x: (x.date, x.type))
            position_calculator = PositionCalculator(sorted_transactions)

            position_model = PositionModel(product_id=product_id, transactions=sorted_transactions,
                                           position_calculator=position_calculator)
            positions.append(position_model)

        return positions
