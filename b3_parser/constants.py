ALLOWED_PRODUCTS = {
    'KNCR11': {
        'tickets': ['KNCR11', 'KNCR12', 'KNCR13', 'KNCR14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'XPML11': {
        'tickets': ['XPML11', 'XPML12', 'XPML13', 'XPML14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'HGLG11': {
        'tickets': ['HGLG11', 'HGLG12', 'HGLG13', 'HGLG14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'AFHI11': {
        'tickets': ['AFHI11', 'AFHI12', 'AFHI13', 'AFHI14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'HGRU11': {
        'tickets': ['HGRU11', 'HGRU12', 'HGRU13', 'HGRU14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'PVBI11': {
        'tickets': ['PVBI11', 'PVBI12', 'PVBI13', 'PVBI14'],
        'type': 'FIIs',
        'ideal': 0.03
    },
    'KNRI11': {
        'tickets': ['KNRI11', 'KNRI12', 'KNRI13', 'KNRI14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'CDII11': {
        'tickets': ['CDII11', 'CDII12', 'CDII13', 'CDII14'],
        'type': 'FIIs',
        'ideal': 0.05
    },
    'RURA11': {
        'tickets': ['RURA11', 'RURA12', 'RURA13', 'RURA14'],
        'type': 'FIIs',
        'ideal': 0.03
    },
    'ALZR11': {
        'tickets': ['ALZR11', 'ALZR12', 'ALZR13', 'ALZR14'],
        'type': 'FIIs',
        'ideal': 0.03
    },
    'POMO3': {
        'tickets': ['POMO3'],
        'type': 'Ações',
        'ideal': 0.03
    },
    'KEPL3': {
        'tickets': ['KEPL3'],
        'type': 'Ações',
        'ideal': 0.03
    },
    'RANI3': {
        'tickets': ['RANI3'],
        'type': 'Ações',
        'ideal': 0.03
    },
    'CXSE3': {
        'tickets': ['CXSE3'],
        'type': 'Ações',
        'ideal': 0.05
    },
    'EGIE3': {
        'tickets': ['EGIE3'],
        'type': 'Ações',
        'ideal': 0.03
    },
    'CSMG3': {
        'tickets': ['CSMG3'],
        'type': 'Ações',
        'ideal': 0.05
    },
    'TAEE11': {
        'tickets': ['TAEE11'],
        'type': 'Ações',
        'ideal': 0.05
    },
    'ITSA4': {
        'tickets': ['ITSA4'],
        'type': 'Ações',
        'ideal': 0.05
    },
    'BBAS3': {
        'tickets': ['BBAS3'],
        'type': 'Ações',
        'ideal': 0.05
    },
    'Tesouro IPCA+ 2029': {
        'tickets': ['Tesouro IPCA+ 2029'],
        'type': 'Renda Fixa',
        'ideal': 0.01
    },
    'Tesouro Prefixado 2027': {
        'tickets': ['Tesouro Prefixado 2027'],
        'type': 'Renda Fixa',
        'ideal': 0.01
    },
    'BTC': {
        'tickets': ['BTC'],
        'type': 'Criptomoedas',
        'ideal': 0.1
    },
    'SGOV': {
        'tickets': ['SGOV'],
        'type': 'ETFs',
        'ideal': 0.09
    }
}


def get_product_by_ticket_id(ticket_id: str):
    result = [x for x, y in ALLOWED_PRODUCTS.items() if ticket_id in y['tickets']]
    if result:
        return ALLOWED_PRODUCTS[result[0]]
