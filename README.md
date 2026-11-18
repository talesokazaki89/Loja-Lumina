# Loja Lumina
Projeto de loja virtual com frontend estático (HTML, CSS e JavaScript) e backend em Python (Flask), que serve as páginas e uma API de produtos.

## Estrutura do projeto

```
loja-lumina/
├── .gitignore
├── README.md
├── requirements.txt
├── docs/
│   └── requisitos.md
├── frontend/
│   ├── index.html
│   ├── pages/
│   │   ├── produtos.html
│   │   └── carrinho.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── assets/
│       └── images/
├── backend/
│   ├── app.py
│   ├── data/
│   │   └── produtos.json
│   └── services/
│       └── __init__.py
├── tests/
│   └── __init__.py
└── notebooks/
    └── README.md
```

## Requisitos

- Python 3.9 ou superior
- pip

## Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:

   ```bash
   python backend/app.py
   ```

4. Acesse no navegador: <http://127.0.0.1:5000>

## API

| Método | Rota                     | Descrição                         |
|--------|--------------------------|-----------------------------------|
| GET    | `/api/produtos`          | Lista todos os produtos           |
| GET    | `/api/produtos/<id>`     | Retorna um produto pelo id        |
| GET    | `/api/saude`             | Verifica se o servidor está no ar |

Os produtos são lidos do arquivo `backend/data/produtos.json`.

## Páginas

- `/`: página inicial
- `/pages/produtos.html`: catálogo de produtos
- `/pages/carrinho.html`: carrinho de compras

## Documentação

Os requisitos do projeto ficam em [`docs/requisitos.md`](docs/requisitos.md).

## Testes

A pasta `tests/` está reservada para os testes automatizados.

## Licença

Defina aqui a licença do projeto.
