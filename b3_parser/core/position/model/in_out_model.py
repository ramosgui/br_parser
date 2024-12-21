

class INOUTModel:

    IN = 1
    OUT = 2

    _mapping = {
        IN: 'in',
        OUT: 'out'
    }

    @classmethod
    def get_id(cls, in_out: str) -> int:
        in_out_id = [x for x, y in cls._mapping.items() if y == in_out]
        if in_out_id:
            return in_out_id[0]
