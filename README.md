# B3 Parser

O **B3 Parser** é uma ferramenta desenvolvida em Python para processar e analisar dados financeiros da B3 (Bolsa de Valores Brasileira). Ela permite a leitura de arquivos de movimentação e negociação, facilitando a extração e manipulação de informações relevantes para análises financeiras.

## Funcionalidades

- **Leitura de Arquivos Excel**: Processa arquivos `.xlsx` contendo dados de movimentações e negociações financeiras.
- **Cálculo de Posições**: Calcula posições financeiras com base nas transações fornecidas.
- **Suporte a Múltiplos Produtos**: Gerencia diversos produtos financeiros conforme definidos no arquivo `constants.py`.

## Estrutura do Projeto

```plaintext
b3_parser/
├── application/
│   └── position/
│       ├── position_service.py
│       └── __init__.py
├── core/
│   ├── position/
│   │   ├── calculator/
│   │   │   ├── position_calculator.py
│   │   │   ├── update_strategy/
│   │   │   │   ├── position_update_strategy.py
│   │   │   │   ├── position_strategy_factory.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── model/
│   │   │   ├── position_model.py
│   │   │   └── __init__.py
│   │   ├── repository/
│   │   │   ├── position_repository.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── transaction/
│   │   ├── model/
│   │   │   ├── transaction_model.py
│   │   │   └── __init__.py
│   │   ├── repository/
│   │   │   ├── transaction_repository.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
├── utils/
│   ├── xlsx/
│   │   ├── xlsx_parser.py
│   │   └── __init__.py
│   └── __init__.py
├── files/
│   ├── 2022.xlsx
│   ├── 2023.xlsx
│   ├── 2024.xlsx
│   └── __init__.py
├── first_file_movimentacao.py
├── first_file_negociacao.py
├── requirements.txt
└── constants.py
```

## Pré-requisitos

- Python 3.8 ou superior.
- Bibliotecas listadas no `requirements.txt`:
  - `pandas`
  - `openpyxl`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/ramosgui/b3_parser.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd b3_parser
   ```

3. Crie um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scriptsctivate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Certifique-se de que os arquivos de dados (`.xlsx`) estejam no diretório `files/`.
2. Execute os scripts conforme necessário. Por exemplo:

   ```bash
   python first_file_movimentacao.py
   ```

   ou

   ```bash
   python first_file_negociacao.py
   ```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:

   ```bash
   git checkout -b minha-feature
   ```

3. Commit suas alterações:

   ```bash
   git commit -m 'Adiciona minha feature'
   ```

4. Envie para o repositório remoto:

   ```bash
   git push origin minha-feature
   ```

5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
