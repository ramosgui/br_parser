from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class VendaPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        pm = total_price / qtd
        qtd -= trx.qtd
        total_price -= trx.qtd * pm
        return PositionMapping(qtd=qtd, total_price=total_price)
