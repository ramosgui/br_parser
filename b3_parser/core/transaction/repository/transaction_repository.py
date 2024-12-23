from typing import List
import os

from b3_parser.constants import ROOT_FILEPATH
from b3_parser.core.transaction.model.transaction_model import TransactionModel
from b3_parser.utils.json.json_parser import get_content_from_json
from b3_parser.utils.xlsx.xlsx_parser import XLSXParser

TRX_FILE_PATH = os.path.join(ROOT_FILEPATH, 'files', 'json', 'hardcoded_transactions.json')


class TransactionRepository:
    """
    Classe que gerencia a recuperação e o processamento de transações.
    Esta classe combina transações extraídas de uma planilha (via XLSXParser) e transações codificadas em
    um arquivo JSON para fornecer uma visão consolidada das transações.
    """

    def __init__(self, xlsx_parser: XLSXParser):
        """
        Inicializa o repositório de transações com um parser de planilhas XLSX.
        :param xlsx_parser: Uma instância de `XLSXParser` usada para extrair transações de uma planilha.
        """
        self._xlsx_transactions = xlsx_parser.get_xlsx_content()

    @staticmethod
    def _get_hardcoded_transactions() -> list:
        """
        Recupera as transações codificadas em um arquivo JSON.
        O arquivo JSON deve conter transações no formato esperado, e este método  calcula o preço total
        (unit_price * qtd) para cada transação antes de retorná-las.
        :return: Uma lista de dicionários representando as transações do arquivo JSON.
        """
        trxs = get_content_from_json(TRX_FILE_PATH)
        for trx in trxs:
            trx['total_price'] = trx['unit_price'] * trx['qtd']
        return trxs

    def get_transactions(self) -> List[TransactionModel]:
        all_transactions = self._get_hardcoded_transactions()
        all_transactions.extend(self._xlsx_transactions)
        transactions = []
        for raw_trx in all_transactions:
            product_id = raw_trx['product'].split(' - ')[0]
            model = TransactionModel(product_id=product_id, raw_transaction=raw_trx)
            transactions.append(model)
        return transactions

    def get_transactions_by_product_ids(self, product_ids: List[str]) -> List[TransactionModel]:
        """
        Recupera transações filtradas pelos IDs de produtos fornecidos.
        Este método combina transações do arquivo JSON e da planilha XLSX, filtrando apenas aquelas cujo ID do produto
        esteja na lista fornecida.
        :param product_ids: Uma lista de IDs de produtos a serem filtrados.
        :return: Uma lista de instâncias de `TransactionModel` representando as transações filtradas.
        """
        transactions = []
        all_transactions = self.get_transactions()
        for trx in all_transactions:
            if trx.product_id in product_ids:
                transactions.append(trx)
        return transactions
