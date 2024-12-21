# B3 Parser

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/release/python-380/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

O **B3 Parser** é uma ferramenta desenvolvida em Python para processar e analisar dados financeiros da B3 (Bolsa de Valores Brasileira). Ele permite a leitura e manipulação de arquivos Excel contendo informações de movimentação e negociação financeira, automatizando cálculos de posição e facilitando análises.

---

## Índice

1. [Funcionalidades](#funcionalidades)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Uso](#uso)
6. [Contribuição](#contribuição)
7. [Licença](#licença)

---

## Funcionalidades

- **Leitura de Arquivos Excel**: Processa dados financeiros de movimentações e negociações.
- **Cálculo de Posições**: Automatiza o cálculo de posições financeiras.
- **Suporte a Produtos Financeiros**: Gerencia produtos como ações, fundos imobiliários, e outros.
- **Extensível**: Fácil de adaptar para novos tipos de produtos ou estratégias de cálculo.

---

## Pré-requisitos

- Python 3.8 ou superior.
- Bibliotecas necessárias (especificadas no `requirements.txt`):
  - `pandas`
  - `openpyxl`

---

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
   source venv/bin/activate  # No Windows: venv\Scripts\Activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

---

## Estrutura do Projeto

```plaintext
b3_parser/
├── application/          # Serviços principais
├── core/                 # Cálculos e estratégias
├── files/                # Arquivos de entrada (.xlsx)
├── utils/                # Funções auxiliares
├── service.py            # Script principal para execução
└── requirements.txt      # Dependências do projeto
```

---

## Uso

1. Coloque os arquivos de dados no diretório `files/`:
   - Exemplo: `2023.xlsx`

2. Execute o serviço principal para processar os dados:

   ```bash
   python service.py
   ```

### Exemplo de Entrada e Saída

#### Entrada (`files/2023.xlsx`):
| Data       | Produto   | Operação  | Quantidade | Valor   |
|------------|-----------|-----------|------------|---------|
| 2023-01-01 | ABEV3     | Compra    | 100        | 1500.00 |
| 2023-01-15 | ABEV3     | Venda     | 50         | 800.00  |

#### Saída (cálculo de posições):
```json
{
  "produto": "ABEV3",
  "posição_final": 50,
  "valor_médio": 15.00
}
```

---

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Adiciona minha feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
