


class TypeModel:

    BONIFICAO_ATIVOS = 1
    DESDOBRO = 2
    LEILA_DE_FRACAO = 3
    LIQUIDACAO = 4
    EMPRESTIMO = 5
    ATUALIZACAO = 6
    SUBSCRICAO_EXERCIDO = 7
    COMPRA = 8
    VENDA = 9

    _types = {
        BONIFICAO_ATIVOS: 'bonificação em ativos',
        DESDOBRO: 'desdobro',
        LEILA_DE_FRACAO: 'leilão de fração',
        LIQUIDACAO: 'transferência - liquidação',
        EMPRESTIMO: 'empréstimo',
        ATUALIZACAO: 'atualização',
        SUBSCRICAO_EXERCIDO: 'direitos de subscrição - exercido',
        COMPRA: 'compra',
        VENDA: 'venda'
    }

    @classmethod
    def get_id(cls, type_: str) -> int:
        type_id = [x for x, y in cls._types.items() if y == type_]
        if type_id:
            return type_id[0]
