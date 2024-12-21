from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class LiquidacaoVendaPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:

        if self._transferencias:
            self._transferencias.pop(0)
            return qtd, total_price

        pm = (total_price / qtd) if qtd > 0 else 0
        qtd -= trx.qtd
        total_price -= trx.qtd * pm

        return PositionMapping(qtd=qtd, total_price=total_price)
