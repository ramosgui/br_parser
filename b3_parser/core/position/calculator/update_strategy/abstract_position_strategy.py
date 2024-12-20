from abc import ABC, abstractmethod
from typing import List

from b3_parser.core.transaction.model.transaction_model import TransactionModel


class BasePositionStrategy(ABC):

    def __init__(self, transferencias: List[TransactionModel]):
        self._transferencias = transferencias

    @abstractmethod
    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> (float, float):
        """
        Aplica a lógica da estratégia para atualizar quantidade e preço total, retornando os valores atualizados.
        """
        pass
