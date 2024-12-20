from b3_parser.constants import get_product_by_ticket_id
from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class AtualizacaoPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        position_type = get_product_by_ticket_id(trx.product_id)
        pm = (total_price / qtd) if qtd > 0 else 0
        qtd += trx.qtd

        if position_type and position_type['type'] == 'Ações':
            if not trx.total_price:
                total_price += trx.total_price
            else:
                total_price += trx.qtd * pm
        elif position_type and position_type['type'] == 'FIIs':
            for sub in self._subscricoes:
                if sub.qtd == trx.qtd and not sub.total_price:
                    total_price = qtd * pm
                elif sub.qtd == trx.qtd and sub.total_price:
                    total_price += sub.total_price

        return PositionMapping(qtd=qtd, total_price=total_price)
