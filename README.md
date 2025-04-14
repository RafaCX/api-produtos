# API de Produtos

## Descrição do Projeto

Este componente faz parte do sistema "Loja Online", uma aplicação de e-commerce baseada em microserviços. A API de Produtos atua como um proxy para a [FakeStore API](https://fakestoreapi.com/), fornecendo dados de produtos em um formato padronizado para o frontend.

Desenvolvida com Python e Flask, esta API implementa uma arquitetura REST e serve como intermediária entre o frontend e a API externa de produtos. Este projeto foi desenvolvido como parte do MVP para a disciplina de Desenvolvimento Full Stack Avançado, com foco na implementação de soluções baseadas em microserviços.

## Funcionalidades

- Listagem de todos os produtos disponíveis
- Busca de um produto específico por ID
- Listagem de categorias de produtos
- Filtragem de produtos por categoria

## Tecnologias Utilizadas

- Python 3.9+
- Flask (framework web)
- Flask-OpenAPI3 (documentação de API)
- Requests (para comunicação com a FakeStore API)
- Flask-CORS (para permitir requisições cross-origin)

## Requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes do Python)
- Ambiente virtual (recomendado)
- Conexão com a internet (para acessar a FakeStore API)

## Instalação e Configuração

Siga os passos abaixo para configurar e executar a API de Produtos:

1. **Clone o repositório**

```bash
git clone https://github.com/RafaCX/api-produtos.git
cd api-produtos
```

2. **Crie e ative um ambiente virtual**

```bash
# No Windows
python -m venv env
.\env\Scripts\activate

# No Linux/Mac
python3 -m venv env
source env/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```
4. **Se certifique que requests está instalado**

```bash
pip install requests
```

5. **Execute a aplicação**

```bash
flask run --host 0.0.0.0 --port 5001 --reload
```

A API estará disponível em: http://localhost:5001

A documentação interativa estará disponível em: http://localhost:5001/openapi

## Endpoints

- **GET /produtos**: Retorna todos os produtos
  - Resposta: Lista de produtos formatados

- **GET /produto/{produto_id}**: Retorna detalhes de um produto específico
  - Parâmetro de caminho: `produto_id` (ID do produto)
  - Resposta: Detalhes do produto formatado

- **GET /categorias**: Retorna todas as categorias disponíveis
  - Resposta: Lista de categorias

- **GET /produtos/categoria/{categoria}**: Retorna produtos de uma categoria específica
  - Parâmetro de caminho: `categoria` (Nome da categoria)
  - Resposta: Lista de produtos formatados da categoria

## Formato dos Dados

A API retorna os produtos no seguinte formato:

```json
{
  "produtos": [
    {
      "id": 1,
      "nome": "Nome do Produto",
      "preco": 19.99,
      "descricao": "Descrição detalhada do produto",
      "categoria": "categoria",
      "imagem": "url_da_imagem"
    },
    ...
  ]
}
```

## Estrutura do Projeto

```
api-produtos/
├── app.py                # Aplicação principal
├── Dockerfile            # Configuração do Docker
└── requirements.txt      # Dependências do projeto
```

## API Externa Utilizada

Este componente utiliza a [FakeStore API](https://fakestoreapi.com/) como fonte de dados para produtos. A FakeStore API é um serviço gratuito que fornece dados fictícios de produtos para desenvolvimento e teste de aplicações de e-commerce.

- URL Base: https://fakestoreapi.com
- Endpoints utilizados:
  - `/products`: Lista todos os produtos
  - `/products/{id}`: Obtém um produto específico
  - `/products/categories`: Lista todas as categorias
  - `/products/category/{category}`: Lista produtos por categoria

## Execução com Docker

Este projeto inclui um Dockerfile para facilitar a implantação:

1. **Construa a imagem Docker**

```bash
docker build -t api-produtos .
```

2. **Execute o contêiner**

```bash
docker run -p 5001:5001 api-produtos
```

A API estará disponível em: http://localhost:5001



Projeto desenvolvido como MVP para a disciplina de Desenvolvimento Full Stack Avançado.