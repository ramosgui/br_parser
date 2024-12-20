from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class EmprestimoPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> (float, float):
        if trx.in_out == 'in':
            self._transferencias.append(trx)
        return qtd, total_price