from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class EmprestimoPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        if trx.qtd:
            self._transferencias.append(trx)
        else:
            try:
                self._transferencias.pop(0)
            except IndexError:
                pass
        return PositionMapping(qtd=qtd, total_price=total_price)
