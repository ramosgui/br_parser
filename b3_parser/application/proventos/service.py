from b3_parser.core.position.repository.position_repository import PositionRepository
from b3_parser.core.transaction.repository.transaction_repository import TransactionRepository
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser


class ProventoService:

    def __init__(self, position_repository: PositionRepository):
        self._position_repository = position_repository

    def get_proventos(self):
        position_models = self._position_repository.get_all_positions()
        return sum([x.proventos for x in position_models])

    def get_proventos_by_month(self):
        position_models = self._position_repository.get_all_positions()
        return sum([x.proventos_by_month for x in position_models])

if __name__ == '__main__':
    xlsx_parser = XLSXParser()
    transaction_repository = TransactionRepository(xlsx_parser)
    position_repository = PositionRepository(transaction_repository)
    service = ProventoService(position_repository)
    ret = service.get_proventos_by_month()
    print(ret)
