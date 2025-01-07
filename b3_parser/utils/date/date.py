from datetime import datetime


def reset_to_first_day_of_month(dt: datetime) -> datetime:
    """
    Ajusta um objeto datetime para o primeiro dia do mês e zera a hora.

    Args:
        dt (datetime): Objeto datetime original.

    Returns:
        datetime: Objeto datetime ajustado para o primeiro dia do mês.
    """
    return datetime(dt.year, dt.month, 1)
