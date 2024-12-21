from b3_parser.core.position.model.position_model import PositionModel
from b3_parser.core.position.repository.position_repository import PositionRepository
from b3_parser.core.transaction.repository.transaction_repository import TransactionRepository
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser

from typing import List


class PositionService:

    def __init__(self, position_repository: PositionRepository):
        self._position_repository = position_repository

    @staticmethod
    def _format_positions(positions: List[PositionModel]):
        formatted_positions = []
        for pos in positions:
            formatted_positions.append({
                'product': pos.product_id,
                'pm': pos.pm,
                'qtd': pos.qtd,
                'type': pos.type,
                'ideal': pos.ideal
            })
        return formatted_positions

    def get_positions(self):
        position_models = self._position_repository.get_all_positions()
        return self._format_positions(position_models)


if __name__ == '__main__':
    xlsx_parser = XLSXParser()
    transaction_repository = TransactionRepository(xlsx_parser)
    position_repository = PositionRepository(transaction_repository)

    service = PositionService(position_repository)
    ret = service.get_positions()

    print(ret)