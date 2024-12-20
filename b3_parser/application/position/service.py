from b3_parser.core.repositories.position_repository import PositionRepository
from b3_parser.core.repositories.transaction_repository import TransactionRepository
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser

if __name__ == '__main__':
    xlsx_parser = XLSXParser()
    transaction_repository = TransactionRepository(xlsx_parser)
    position_repository = PositionRepository(transaction_repository)
    position_repository.get_all_positions()