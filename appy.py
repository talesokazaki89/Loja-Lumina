"""Backend da Loja Lumina.

Servidor Flask que:
- serve os arquivos estáticos do frontend (HTML, CSS, JS e imagens);
- expõe uma API REST simples para consulta de produtos.

Execução:
    python backend/app.py
"""

import json
from pathlib import Path

from flask import Flask, abort, jsonify, send_from_directory

# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"
PRODUTOS_JSON = BASE_DIR / "data" / "produtos.json"

# ---------------------------------------------------------------------------
# Aplicação
# ---------------------------------------------------------------------------
app = Flask(__name__, static_folder=None)
app.config["JSON_AS_ASCII"] = False  # mantém acentos nas respostas JSON


def carregar_produtos():
    """Lê a lista de produtos do arquivo JSON."""
    if not PRODUTOS_JSON.exists():
        return []
    with PRODUTOS_JSON.open(encoding="utf-8") as arquivo:
        return json.load(arquivo)


# ---------------------------------------------------------------------------
# Rotas da API
# ---------------------------------------------------------------------------
@app.get("/api/produtos")
def listar_produtos():
    """Retorna todos os produtos."""
    return jsonify(carregar_produtos())


@app.get("/api/produtos/<int:produto_id>")
def obter_produto(produto_id):
    """Retorna um produto pelo id."""
    for produto in carregar_produtos():
        if produto.get("id") == produto_id:
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404


@app.get("/api/saude")
def saude():
    """Rota simples para verificar se o servidor está no ar."""
    return jsonify({"status": "ok"})


# ---------------------------------------------------------------------------
# Rotas do frontend
# ---------------------------------------------------------------------------
@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/pages/<path:nome>")
def paginas(nome):
    return send_from_directory(FRONTEND_DIR / "pages", nome)


@app.get("/<any(css, js, assets):pasta>/<path:nome>")
def estaticos(pasta, nome):
    return send_from_directory(FRONTEND_DIR / pasta, nome)


# ---------------------------------------------------------------------------
# Tratamento de erros
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def nao_encontrado(_erro):
    return jsonify({"erro": "Recurso não encontrado"}), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
