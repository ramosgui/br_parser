from typing import List

from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.atualizacao_strategy import \
    AtualizacaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.bonus_desdobro_strategy import \
    BonusDesdobroPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.emprestimo_strategy import EmprestimoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.leilao_de_fracao_strategy import \
    LeilaoDeFracaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.liquidacao_strategy import LiquidacaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.subscricao_strategy import SubscricaoPositionStrategy
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class PositionStrategyFactory:

    _strategies = {
        'bonificação em ativos': BonusDesdobroPositionStrategy,
        'desdobro': BonusDesdobroPositionStrategy,
        'leilão de fração': LeilaoDeFracaoPositionStrategy,
        'transferência - liquidação': LiquidacaoPositionStrategy,
        'empréstimo': EmprestimoPositionStrategy,
        'atualização': AtualizacaoPositionStrategy,
        'direitos de subscrição - exercido': SubscricaoPositionStrategy
    }

    @staticmethod
    def get_strategy(type_: str, transfer: List[TransactionModel], subscricoes: List[TransactionModel]) -> BasePositionStrategy:
        if type_ in PositionStrategyFactory._strategies:
            return PositionStrategyFactory._strategies[type_](transfer, subscricoes)
