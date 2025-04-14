from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify, request
import requests
from flask_cors import CORS
from pydantic import BaseModel, Field

info = Info(title="API de Produtos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# URL base da FakeStore API
FAKESTORE_API_URL = "https://fakestoreapi.com"

# Definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Consulta de produtos da FakeStore API")

# Esquemas para parâmetros de rota
class ProdutoPath(BaseModel):
    produto_id: int = Field(..., description="ID do produto")

class CategoriaPath(BaseModel):
    categoria: str = Field(..., description="Nome da categoria")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/produtos', tags=[produto_tag])
def get_produtos():
    """Obtém todos os produtos da FakeStore API
    """
    try:
        response = requests.get(f"{FAKESTORE_API_URL}/products")
        produtos = response.json()
        
        # Formata os produtos para o formato esperado pelo frontend
        produtos_formatados = []
        for produto in produtos:
            produtos_formatados.append({
                "id": produto["id"],
                "nome": produto["title"],
                "preco": produto["price"],
                "descricao": produto["description"],
                "categoria": produto["category"],
                "imagem": produto["image"]
            })
        
        return jsonify({"produtos": produtos_formatados})
    
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar produtos: {str(e)}"}), 500

# Corrigido: /produto/{produto_id} → /produto/{path.produto_id}
@app.get('/produto/{produto_id}', tags=[produto_tag])
def get_produto(query: ProdutoPath):
    """Obtém um produto específico da FakeStore API
    """
    try:
        produto_id = query.produto_id
        response = requests.get(f"{FAKESTORE_API_URL}/products/{produto_id}")
        produto = response.json()
        
        # Formata o produto para o formato esperado pelo frontend
        produto_formatado = {
            "id": produto["id"],
            "nome": produto["title"],
            "preco": produto["price"],
            "descricao": produto["description"],
            "categoria": produto["category"],
            "imagem": produto["image"]
        }
        
        return jsonify(produto_formatado)
    
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar produto: {str(e)}"}), 500

@app.get('/categorias', tags=[produto_tag])
def get_categorias():
    """Obtém todas as categorias de produtos da FakeStore API
    """
    try:
        response = requests.get(f"{FAKESTORE_API_URL}/products/categories")
        categorias = response.json()
        
        return jsonify({"categorias": categorias})
    
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar categorias: {str(e)}"}), 500

# Corrigido: /produtos/categoria/{categoria} → /produtos/categoria/{path.categoria}
@app.get('/produtos/categoria/{categoria}', tags=[produto_tag])
def get_produtos_por_categoria(query: CategoriaPath):
    """Obtém produtos por categoria da FakeStore API
    """
    try:
        categoria = query.categoria
        response = requests.get(f"{FAKESTORE_API_URL}/products/category/{categoria}")
        produtos = response.json()
        
        # Formata os produtos para o formato esperado pelo frontend
        produtos_formatados = []
        for produto in produtos:
            produtos_formatados.append({
                "id": produto["id"],
                "nome": produto["title"],
                "preco": produto["price"],
                "descricao": produto["description"],
                "categoria": produto["category"],
                "imagem": produto["image"]
            })
        
        return jsonify({"produtos": produtos_formatados})
    
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar produtos por categoria: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)