
import warnings

from json_parser import JSONParser
from xlsx_parser import XLSXParser

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")





if __name__ == '__main__':
    xlsx_parser = XLSXParser()
    xlsx_content = xlsx_parser.get_xlsx_content()

    json_parser = JSONParser(xlsx_content)
    json_parser.get_positions()


