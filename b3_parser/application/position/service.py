from b3_parser.core.position.model.position_model import PositionModel
from b3_parser.core.position.repository.position_repository import PositionRepository
from b3_parser.core.transaction.repository.transaction_repository import TransactionRepository
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser

from typing import List

import warnings


warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


class PositionService:
    """
    Uma classe de serviço responsável por gerenciar e formatar dados de posições.
    Esta classe interage com o `PositionRepository` para recuperar os dados de posições, processá-los e fornecer uma
    saída formatada para uso posterior. Ela abstrai a lógica do repositório de dados subjacente e foca em fornecer uma
    API limpa para acesso a informações relacionadas a posições.
    """

    def __init__(self, position_repository: PositionRepository):
        """
        Inicializa o PositionService com o repositório de posições.
        :param position_repository: Uma instância de `PositionRepository` usada para acessar os dados de posições.
        """
        self._position_repository = position_repository

    @staticmethod
    def _format_positions(positions: List[PositionModel]):
        """
        Formata uma lista de modelos de posições em uma estrutura de dicionário.
        :param positions: Uma lista de instâncias de `PositionModel` representando posições.
        :return: Uma lista de dicionários contendo os dados formatados das posições com as seguintes chaves:
            - `product`: O ID do produto associado à posição.
            - `pm`: O preço médio (PM) da posição.
            - `qtd`: A quantidade da posição.
            - `type`: O tipo da posição (ex.: ação, FII).
            - `ideal`: A alocação ideal da posição.
        """
        formatted_positions = []
        for pos in positions:
            if pos.qtd:
                formatted_positions.append({
                    'product': pos.product_id,
                    'pm': pos.pm,
                    'qtd': pos.qtd,
                    'proventos': pos.proventos
                })
        return formatted_positions

    def get_positions(self):
        """
        Recupera e formata todas as posições do repositório.
        :return: Uma lista de dicionários representando todas as posições formatadas.
        """
        position_models = self._position_repository.get_all_positions()
        return self._format_positions(position_models)


if __name__ == '__main__':
    xlsx_parser = XLSXParser()
    transaction_repository = TransactionRepository(xlsx_parser)
    position_repository = PositionRepository(transaction_repository)

    service = PositionService(position_repository)
    ret = service.get_positions()

    print(ret)