
from pandas import DataFrame


class JSONParser:

    def __init__(self, xlsx_content: DataFrame):
        self._xlsx_content = xlsx_content

        self._TYPE_BLACKLIST = [
            'Rendimento'
        ]

        self._PRODUCT_WHITELIST = [
            'RURA11'
        ]

    def get_json_from_xlsx(self):
        json_data = self._xlsx_content.to_dict(orient='records')
        result = []
        for line in json_data:
            product = line['product'].split(' - ')[0]
            line['product'] = product
            if product in self._PRODUCT_WHITELIST:
                result.append(line)
        return result

    def get_positions(self):
        transactions = self.get_json_from_xlsx()
        sorted_transactions = sorted(transactions, key=lambda x: x['dt'])

        qtd = 0
        pm = 0
        price = 0

        for trx in sorted_transactions:
            if trx['type'] == 'Transferência - Liquidação':
                print(trx)

                if trx['operation']

