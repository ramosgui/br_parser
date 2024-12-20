from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class LiquidacaoPositionStrategy(BasePositionStrategy):
    """
    Estratégia para 'transferência - liquidação'.
    Dependendo de 'in' ou 'out', ajusta a posição.
    Se não houver preço total, usa o pm atual.
    """
    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> (float, float):

        if self._transferencias:
            self._transferencias.pop(0)
            return qtd, total_price

        trx_qtd = trx.qtd or 0
        trx_total = trx.total_price

        if trx.in_out == 'in':
            qtd += trx_qtd
            if trx_total is not None:
                total_price += trx_total
            else:
                pm = (total_price / qtd) if qtd > 0 else 0
                total_price += trx_qtd * pm
        else:
            # saída
            old_qtd = qtd
            qtd -= trx_qtd
            pm = (total_price / old_qtd) if old_qtd > 0 else 0
            total_price -= trx_qtd * pm

        return qtd, total_price