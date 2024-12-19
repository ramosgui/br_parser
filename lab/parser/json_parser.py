from pandas import DataFrame


class JSONParser:

    def __init__(self, xlsx_content: DataFrame):
        self._xlsx_content = xlsx_content

        self._TYPE_BLACKLIST = [
            'Rendimento'
        ]

        self._PRODUCT_WHITELIST = [
            'KNCR11', 'KNCR12', 'KNCR13', 'KNCR14',
            'RURA11', 'RURA12', 'RURA13', 'RURA14',
            'XPML11', 'XPML12', 'XPML13', 'XPML14',
            'AFHI11', 'AFHI12', 'AFHI13', 'AFHI14',
            'HGLG11', 'HGLG12', 'HGLG13', 'HGLG14',
            'HGRU11', 'HGRU12', 'HGRU13', 'HGRU14',
            'PVBI11', 'PVBI12', 'PVBI13', 'PVBI14',
            'CDII11', 'CDII12', 'CDII13', 'CDII14',
            'KNRI11', 'KNRI12', 'KNRI13', 'KNRI14',
            'ALZR11', 'ALZR12', 'ALZR13', 'ALZR14',
            'POMO3'
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

        position_map = {x['product']: {
            'qtd': 0,
            'pm': 0,
            'total_amount': 0,
            'subscricoes': []
        } for x in sorted_transactions if x['type'] == 'Transferência - Liquidação'}

        for trx in sorted_transactions:

            # print(trx)

            if trx['type'] == 'Direitos de Subscrição - Exercido':
                product = trx['product'][0:4] + '11'
                position_map[product]['subscricoes'].append(trx)

            if trx['type'] == 'Atualização':
                for sub in position_map[trx['product']]['subscricoes']:
                    if sub['qtd'] == trx['qtd']:
                        trx['type'] = 'Transferência - Liquidação'
                        trx['atualizacao'] = 'true'
                        trx['unit_price'] = sub['unit_price']
                        trx['total_price'] = sub['total_price']

            if trx['type'] in ['Transferência - Liquidação']:

                # if trx['unit_price'] == '-':
                #     trx['unit_price'] = 0
                #
                # if trx['total_price'] == '-':
                #     trx['total_price'] = 0

                # simulacao de preço em caso de transacoes com valor vazio
                if trx['unit_price'] == '-' and trx['total_price'] == '-':
                    trx['unit_price'] = position_map[trx['product']]['pm']
                    trx['total_price'] = trx['qtd'] * trx['unit_price']

                if trx['operation'] == 'Credito':
                    position_map[trx['product']]['qtd'] += trx['qtd']
                    position_map[trx['product']]['total_amount'] += trx['total_price']

                else:
                    position_map[trx['product']]['total_amount'] -= (
                                position_map[trx['product']]['qtd'] * position_map[trx['product']]['pm'])
                    position_map[trx['product']]['qtd'] -= trx['qtd']

                try:
                    position_map[trx['product']]['pm'] = position_map[trx['product']]['total_amount'] / position_map[trx['product']]['qtd']
                except ZeroDivisionError:
                    position_map[trx['product']]['pm'] = 0

                # print(position_map)

        return position_map
