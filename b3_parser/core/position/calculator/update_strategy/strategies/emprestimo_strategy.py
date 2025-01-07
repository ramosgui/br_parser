from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class EmprestimoPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:

        # if trx.in_out == 'in' and not self._transferencias:
        if trx.in_out == 'in' and trx.qtd:
            self._transfer_control.add(trx.qtd)

        # if trx.qtd:
        #     self._transferencias.append(trx)
        # else:
        #     self._transferencias = []
        return PositionMapping(qtd=qtd, total_price=total_price)
