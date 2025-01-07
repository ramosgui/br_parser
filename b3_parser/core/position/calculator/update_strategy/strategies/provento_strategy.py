from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel
from b3_parser.utils.date.date import reset_to_first_day_of_month


class ProventoPositionStrategy(BasePositionStrategy):
    ALLOWED_TYPES = ['rendimento', 'juros sobre capital próprio', 'dividendo', 'reembolso']

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        if trx.type in self.ALLOWED_TYPES:
            total_price += trx.total_price
        return PositionMapping(qtd=qtd, total_price=total_price)

    def month_total_price(self, trx: TransactionModel, month_mapping: dict):
        dt = reset_to_first_day_of_month(dt=trx.date)
        if dt not in month_mapping:
            month_mapping[dt] = trx.total_price
        else:
            month_mapping[dt] += trx.total_price
        return month_mapping
