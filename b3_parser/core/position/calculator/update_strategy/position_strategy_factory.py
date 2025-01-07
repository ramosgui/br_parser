from collections import namedtuple
from typing import List
from typing import Set

from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.atualizacao_strategy import \
    AtualizacaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.bonificacao_strategy import \
    BonificacaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.compra_strategy import CompraPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.desdobro_strategy import DesdobroPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.emprestimo_strategy import EmprestimoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.leilao_de_fracao_strategy import \
    LeilaoDeFracaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.liquidacao_compra_strategy import LiquidacaoCompraPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.liquidacao_venda_strategy import \
    LiquidacaoVendaPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.subscricao_strategy import SubscricaoPositionStrategy
from b3_parser.core.position.calculator.update_strategy.strategies.venda_strategy import VendaPositionStrategy
from b3_parser.core.position.model.in_out_model import INOUTModel
from b3_parser.core.position.model.type_model import TypeModel
from b3_parser.core.transaction.model.transaction_model import TransactionModel

PositionMapping = namedtuple('PositionMapping', ['type', 'in_out'])


class PositionStrategyFactory:

    _strategies = {
        PositionMapping(type=TypeModel.BONIFICAO_ATIVOS, in_out=INOUTModel.IN): BonificacaoPositionStrategy,
        PositionMapping(type=TypeModel.DESDOBRO, in_out=INOUTModel.IN): DesdobroPositionStrategy,
        PositionMapping(type=TypeModel.LEILA_DE_FRACAO, in_out=INOUTModel.IN): LeilaoDeFracaoPositionStrategy,
        PositionMapping(type=TypeModel.LIQUIDACAO, in_out=INOUTModel.IN): LiquidacaoCompraPositionStrategy,
        PositionMapping(type=TypeModel.COMPRA, in_out=INOUTModel.IN): CompraPositionStrategy,
        PositionMapping(type=TypeModel.LIQUIDACAO, in_out=INOUTModel.OUT): LiquidacaoVendaPositionStrategy,
        PositionMapping(type=TypeModel.VENDA, in_out=INOUTModel.OUT): VendaPositionStrategy,
        PositionMapping(type=TypeModel.EMPRESTIMO, in_out=INOUTModel.IN): EmprestimoPositionStrategy,
        PositionMapping(type=TypeModel.ATUALIZACAO, in_out=INOUTModel.IN): AtualizacaoPositionStrategy,
        PositionMapping(type=TypeModel.SUBSCRICAO_EXERCIDO, in_out=INOUTModel.OUT): SubscricaoPositionStrategy
    }

    @staticmethod
    def get_strategy(type_: str, in_out: str, transfer_control: Set[float],
                     subscricoes: List[TransactionModel]) -> BasePositionStrategy:

        position_mapping = PositionMapping(type=TypeModel.get_id(type_), in_out=INOUTModel.get_id(in_out))
        if position_mapping in PositionStrategyFactory._strategies:
            return PositionStrategyFactory._strategies[position_mapping](transfer_control, subscricoes)
