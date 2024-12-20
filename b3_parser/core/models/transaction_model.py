from datetime import datetime
from typing import Optional


class TransactionModel:


    def __init__(self, product_id: str, raw_transaction: dict):

        ### type tipo da transacao, liquidacao.. etc

        self._raw_transaction = raw_transaction
        self.product_id = product_id

    @property
    def type(self) -> str:
        return self._raw_transaction['type'].lower()

    @property
    def in_out(self) -> str:
        return 'in' if self._raw_transaction['operation'] == 'Credito' else 'out'

    @property
    def qtd(self) -> Optional[float]:
        raw_qtd = self._raw_transaction['qtd']
        if raw_qtd != 0:
            return self._raw_transaction['qtd']
        return None

    @property
    def unit_price(self) -> Optional[float]:
        try:
            return float(self._raw_transaction['unit_price'])
        except ValueError:
            return None

    @property
    def total_price(self) -> Optional[float]:
        try:
            return float(self._raw_transaction['total_price'])
        except ValueError:
            return None

    @property
    def date(self) -> datetime:
        return datetime.strptime(self._raw_transaction['dt'], "%Y-%m-%d")
