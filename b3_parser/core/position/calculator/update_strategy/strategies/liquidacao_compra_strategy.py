from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class LiquidacaoCompraPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:

        if self._transfer_control:

            for transf_qtd in self._transfer_control:
                if transf_qtd == trx.qtd:
                    self._transfer_control.remove(transf_qtd)
                    return qtd, total_price

        pm = (total_price / qtd) if qtd > 0 else 0
        qtd += trx.qtd

        if trx.total_price is not None:
            total_price += trx.total_price
        else:
            total_price += trx.qtd * pm

        return PositionMapping(qtd=qtd, total_price=total_price)
