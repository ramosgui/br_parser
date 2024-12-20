from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class BonusDesdobroPositionStrategy(BasePositionStrategy):
    """
    Estratégia para 'bonificação em ativos' e 'desdobro'.
    Soma a quantidade e o preço total.
    """
    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> (float, float):
        trx_qtd = trx.qtd or 0
        trx_total = trx.total_price or 0
        qtd += trx_qtd
        total_price += trx_total
        return qtd, total_price
