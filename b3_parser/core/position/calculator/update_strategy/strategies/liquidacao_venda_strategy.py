from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class LiquidacaoVendaPositionStrategy(BasePositionStrategy):
    """
    Estratégia para 'transferência - liquidação'.
    Dependendo de 'in' ou 'out', ajusta a posição.
    Se não houver preço total, usa o pm atual.
    """

    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:

        if self._transferencias:
            self._transferencias.pop(0)
            return qtd, total_price

        trx_qtd = trx.qtd
        trx_total = trx.total_price
        pm = (total_price / qtd) if qtd > 0 else 0

        if trx.in_out == 'in':
            qtd += trx_qtd
            if trx_total is not None:
                total_price += trx_total
            else:
                total_price += trx_qtd * pm
        else:
            qtd -= trx_qtd
            total_price -= trx_qtd * pm

        return PositionMapping(qtd=qtd, total_price=total_price)
