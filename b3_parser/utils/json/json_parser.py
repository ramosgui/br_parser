
import json


def get_content_from_json(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
        return content
    except FileNotFoundError:
        print("filepath não encontrado.")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    return []
