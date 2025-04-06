# API de Análise de Vendas

Esta API fornece endpoints para análise de vendas com base em diversos filtros, incluindo melhor vendedor, ranking de produtos, análise por cidade, bandeira e muito mais.

## Endpoints

### 1. Melhor em Diversas Categorias
**Rota:** `GET /melhor`

**Parâmetros:**
- `tipo` (obrigatório): Define o critério para encontrar o melhor. Opções:
  - `nome do empregado`
  - `nome do produto`
  - `cidade do ponto de venda`
  - `nome do ponto de venda`
- `Supercategoria` (opcional): Filtra por categoria de produto.
- `mes` (opcional): Filtra por mês.
- `ano` (opcional): Filtra por ano.
- `limite` (opcional, padrão: 1): Define quantos itens retornar no ranking.

**Resposta:**
```json
{
  "melhor_nome_do_empregado": [
    {
      "Nome do empregado": "João Silva",
      "Vendas": 5000
    }
  ]
}
```

---

### 2. Ranking Completo
**Rota:** `GET /ranking`

**Parâmetros:**
- `tipo` (opcional, padrão: "nome do empregado"): Mesmos valores do endpoint `/melhor`.
- `Supercategoria`, `mes`, `ano`: Mesmos filtros do endpoint `/melhor`.

**Resposta:**
```json
{
  "sucesso": true,
  "tipo": "nome do empregado",
  "ranking": [
    {
      "Nome do empregado": "João Silva",
      "Vendas": 5000
    },
    {
      "Nome do empregado": "Maria Souza",
      "Vendas": 4500
    }
  ]
}
```

---

### 3. Melhor Vendedor por Categoria
**Rota:** `GET /melhor-por-categoria`

**Parâmetros:**
- `mes`, `ano` (opcionais): Filtra por período.

**Resposta:**
```json
{
  "melhor_vendedor_por_categoria": [
    {
      "categoria": "Eletrônicos",
      "melhor_vendedor": "Carlos Lima",
      "vendas_totais": 3200,
      "produto_mais_vendido": [
        {"Nome do produto": "Smartphone X", "Vendas": 1500}
      ]
    }
  ]
}
```

---

### 4. Análise por Empregado
**Rota:** `GET /analise-por-empregado`

**Parâmetros:**
- `empregado` (obrigatório): Nome do empregado para análise.
- `mes`, `ano` (opcionais): Filtra por período.

**Resposta:**
```json
{
  "empregado": "João Silva",
  "vendas_por_mes": [...],
  "melhor_mes": [...],
  "vendas_por_categoria": [...],
  "produtos_por_categoria": [...]
}
```

---

### 5. Análise por Cidade
**Rota:** `GET /analise-por-cidade`

**Parâmetros:**
- `cidade` (obrigatório): Nome da cidade para análise.
- `mes`, `ano` (opcionais): Filtra por período.

**Resposta:**
```json
{
  "cidade": "São Paulo",
  "vendas_por_mes": [...],
  "melhor_mes": [...],
  "vendas_por_categoria": [...],
  "produtos_por_categoria": [...]
}
```

---

### 6. Análise por Bandeira
**Rota:** `GET /analise-por-bandeira`

**Parâmetros:**
- `bandeira` (obrigatório): Nome da bandeira para análise.
- `mes`, `ano` (opcionais): Filtra por período.

**Resposta:**
```json
{
  "bandeira": "Loja X",
  "vendas_por_mes": [...],
  "melhor_mes": [...],
  "vendas_por_categoria": [...],
  "produtos_por_categoria": [...]
}
```

---

### 7. Melhor Cidade ou Bandeira
**Rota:** `GET /melhor-cidade-ou-bandeira`

**Parâmetros:**
- `tipo` (obrigatório): `cidade` ou `bandeira`.
- `mes`, `ano` (opcionais): Filtra por período.

**Resposta:**
```json
{
  "melhor_cidade": [
    {"Cidade do ponto de venda": "Rio de Janeiro", "Vendas": 10000}
  ]
}
```

---

### 8. Ranking de Cidades ou Bandeiras
**Rota:** `GET /ranking-cidade-ou-bandeira`

**Parâmetros:**
- `tipo` (obrigatório): `cidade` ou `bandeira`.
- `mes`, `ano` (opcionais): Filtra por período.

**Resposta:**
```json
{
  "ranking_cidade": [
    {"Cidade do ponto de venda": "Rio de Janeiro", "Vendas": 10000},
    {"Cidade do ponto de venda": "São Paulo", "Vendas": 9000}
  ]
}
```

---

## Como Rodar o Projeto Localmente

1. Clone o repositório:
```sh
git clone https://github.com/AlexJSMartins/API-PYTHON.git
cd seuprojeto
```

2. Crie um ambiente virtual e instale as dependências:
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Execute as migrações:
```sh
python manage.py migrate
```

4. Inicie o servidor:
```sh
python manage.py runserver
```

Agora a API estará disponível em `http://127.0.0.1:8000/`.

---

Se precisar de melhorias ou adições, é só avisar!

