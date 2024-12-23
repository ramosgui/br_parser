from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class AtualizacaoPositionStrategy(BasePositionStrategy):

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        # position_type = get_product_by_ticket_id(trx.product_id)
        pm = (total_price / qtd) if qtd > 0 else 0
        qtd += trx.qtd

        if len(trx.product_id) == 6 and trx.product_id[-2:] in ['11', '12', '13', '14']:
            for sub in self._subscricoes:
                if sub.qtd == trx.qtd and not sub.total_price:
                    total_price = qtd * pm
                elif sub.qtd == trx.qtd and sub.total_price:
                    total_price += sub.total_price
        else:
            if trx.total_price:
                    total_price += trx.total_price
            else:
                total_price += trx.qtd * pm

        return PositionMapping(qtd=qtd, total_price=total_price)
