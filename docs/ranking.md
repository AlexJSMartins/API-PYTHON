# API-PYTHON

# 📊 Ranking API - Django Backend

## 📌 Descrição
O endpoint `ranking` retorna um ranking completo baseado em diferentes categorias de análise, como nome do empregado, nome do produto, cidade do ponto de venda e nome do ponto de venda. Os dados podem ser filtrados por supercategoria, mês e ano.

---

## 🚀 Como Usar
A API aceita requisições `GET` com parâmetros opcionais para personalizar a consulta.

### **🔗 URL Base**
```
http://127.0.0.1:8000/api/ranking
```

### **📥 Parâmetros Disponíveis**

| Parâmetro       | Tipo   | Obrigatório? | Descrição |
|-----------------|--------|-------------|------------|
| `tipo`         | string | Não         | Define o tipo de ranking. Opções: `"nome do empregado"`, `"nome do produto"`, `"cidade do ponto de venda"`, `"nome do ponto de venda"`. Se omitido, assume `"nome do empregado"`. |
| `mes`          | int    | Não         | Filtra os resultados por um mês específico (1-12). |
| `ano`          | int    | Não         | Filtra os resultados por um ano específico (ex: 2024). |

---

## 📌 Exemplos de Uso

### ✅ **Ranking de Empregados (Sem Filtros)**
```
GET http://127.0.0.1:8000/api/ranking
```
**Resposta:**
```json
{
    "sucesso": true,
    "tipo": "nome do empregado",
    "ranking": [
        {"Nome do empregado": "João Silva", "vendas": 150},
        {"Nome do empregado": "Maria Souza", "vendas": 130}
    ]
}
```

### ✅ **Ranking de Produtos em Julho de 2024**
```
GET http://127.0.0.1:8000/api/ranking?tipo=nome%20do%20produto&mes=7&ano=2024
```
**Resposta:**
```json
{
    "sucesso": true,
    "tipo": "nome do produto",
    "ranking": [
        {"Nome do produto": "Smartphone X", "vendas": 300},
        {"Nome do produto": "Notebook Y", "vendas": 250}
    ]
}
```

### ✅ **Ranking por Cidade com Supercategoria Específica**
```
GET http://127.0.0.1:8000/api/ranking?tipo=cidade%20do%20ponto%20de%20venda
```
**Resposta:**
```json
{
    "sucesso": true,
    "tipo": "cidade do ponto de venda",
    "ranking": [
        {"Cidade do ponto de venda": "São Paulo", "vendas": 500},
        {"Cidade do ponto de venda": "Rio de Janeiro", "vendas": 450}
    ]
}
```

---

## 🚨 Possíveis Erros

### ❌ **Tipo Inválido**
Se um `tipo` não suportado for informado:
```json
{
    "error": "Tipo 'categoria do cliente' inválido. Escolha entre: nome do empregado, nome do produto, cidade do ponto de venda, nome do ponto de venda.",
    "tipos_validos": ["nome do empregado", "nome do produto", "cidade do ponto de venda", "nome do ponto de venda"]
}
```

### ❌ **Mês ou Ano Inválido**
Se `mes` ou `ano` não forem números:
```json
{
    "error": "Parâmetro 'mes' ou 'ano' inválido."
}
```

---

## 🛠 Tecnologias Utilizadas
- Python
- Django
- Pandas (para manipulação de dados)

---

## 📢 Contribuição
Sugestões e melhorias são bem-vindas! Sinta-se à vontade para criar um PR ou abrir uma issue. 🚀

