
import warnings

from json_parser import JSONParser
from xlsx_parser import XLSXParser

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def format_positions(positions):
    formatted_positions = []
    for k, v in positions.items():
        formatted_positions.append({'product': k, 'pm': v['pm'], 'qtd': v['qtd'], 'total_amount': v['total_amount']})
    return formatted_positions


if __name__ == '__main__':
    xlsx_parser = XLSXParser()
    xlsx_content = xlsx_parser.get_xlsx_content()

    json_parser = JSONParser(xlsx_content)
    positions = json_parser.get_positions()
    result = format_positions(positions)

    print(result)
