from abc import ABC, abstractmethod
from collections import namedtuple
from typing import List

from b3_parser.core.transaction.model.transaction_model import TransactionModel


PositionMapping = namedtuple('PositionMapping', ['qtd', 'total_price'])

class BasePositionStrategy(ABC):

    def __init__(self, transferencias: List[TransactionModel], subscricoes: List[TransactionModel]):
        self._transferencias = transferencias
        self._subscricoes = subscricoes

    @abstractmethod
    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        """
        Aplica a lógica da estratégia para atualizar quantidade e preço total, retornando os valores atualizados.
        """
        pass
