📊 **Gestor de Análise de Vendas – Backend**


🚀 Um sistema robusto para análise de dados de vendas, fornecendo insights detalhados sobre vendedores, produtos, lojas e cidades. Desenvolvido com Django e Django REST Framework, este backend fornece uma API poderosa e estruturada para alimentar dashboards e outras aplicações de análise de dados.


🏆 Sobre o Projeto
O Gestor de Análise de Vendas foi desenvolvido para processar e analisar dados de vendas de forma eficiente, oferecendo um conjunto de endpoints RESTful para fornecer informações estratégicas.

🔹 API estruturada para consulta de dados de vendas.
🔹 Filtragem avançada por vendedor, produto, loja e cidade.
🔹 Rankings para identificar os melhores desempenhos.
🔹 Análise temporal, permitindo insights sobre tendências.
🔹 Processamento eficiente com Pandas para manipulação de dados.

⚙️ Tecnologias Utilizadas

📌 Backend:

Python (Django) 🐍

Django REST Framework 🌐

Pandas para análise de dados 📊

SQLite (pode ser substituído por PostgreSQL) 💾


📂 Arquitetura do Projeto

📦 ProjetoBackDasboard
├── 📂 dashboard_backend/        # Configurações principais do Django
├── 📂 dashboard_backend/        # Lógica de análise de dados
├── 📂 data_api/                 # Endpoints RESTful
├── 📂 planilha/                 # Arquivos de dados e ETL
├── 📄 manage.py                 # Arquivo principal do Django
├── 📄 requirements.txt          # Dependências do backend
└── 📂 docs/                     # Documentação detalhada dos endpoints
    ├── ranking_vendedores.md
    ├── analise_por_loja.md
    ├── analise_por_cidade.md
    ├── analise_por_produto.md

**--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**


🚀 Como Executar o Backend

🔧 Pré-requisitos

Antes de começar, você precisará ter instalado:

Python 3.9+

🖥 Passos para Rodar o Projeto

1️⃣ Clone o repositório:

git clone https://github.com/AlexJSMartins/API-PYTHON.git

cd dashboard_backend

2️⃣ Crie um ambiente virtual e ative:

python -m venv venv

source venv/bin/activate  # No Windows: venv\Scripts\activate

3️⃣ Instale as dependências:

pip install -r requirements.txt

4️⃣ Execute as migrações do banco de dados:

python manage.py migrate

5️⃣ Inicie o servidor Django:

python manage.py runserver

Agora, a API estará disponível em http://127.0.0.1:8000 🚀

🔗 Endpoints Principais
Todos os endpoints aceitam parâmetros adicionais opcionais:
?mes=<número_do_mês>&ano=<ano> para refinar a análise por período.

📊 Rankings de Vendas
🔝 Ranking Geral de Vendedores
GET /api/ranking
📌 Retorna o ranking dos melhores vendedores com opção de filtro por mês e ano.

🏙 Ranking por Cidade ou Bandeira
GET /api/ranking-cidade-ou-bandeira?tipo=cidade
GET /api/ranking-cidade-ou-bandeira?tipo=bandeira
📌 Ranking de vendas por cidade ou por bandeira de loja.

🏪 Análises Detalhadas
🧍 Análise por Empregado
GET /api/analise-por-empregado?empregado=nome_completo_do_empregado
📌 Análise detalhada de um vendedor individual.


🏙 Análise por Cidade
GET /api/analise-por-cidade?cidade=nome_da_cidade
📌 Vendas totais e por categoria em uma cidade específica.

🏬 Análise por Bandeira
GET /api/analise-por-bandeira?bandeira=nome_da_bandeira
📌 Análise de desempenho por bandeira (ex: magazine luiza, lojas americanas...).

📦 Análise por Produto
GET /api/analise-por-produto?produto=nome_do_produto
📌 Informações sobre o produto mais vendido, categorias associadas e lojas.

🏆 Melhores Desempenhos
⭐ Melhor Cidade ou Bandeira
GET /api/melhor-cidade-ou-bandeira?tipo=cidade
GET /api/melhor-cidade-ou-bandeira?tipo=bandeira
📌 Retorna a cidade ou bandeira com maior volume de vendas.

🥇 Melhor Geral (Vendedor, Loja, Cidade ou Bandeira)
GET /api/melhor?tipo=empregado
GET /api/melhor?tipo=loja
GET /api/melhor?tipo=cidade do ponto de venda
GET /api/melhor?tipo=bandeira
📌 Mostra o melhor em cada dimensão.

🔍 Para mais detalhes, consulte a pasta docs/!

📌 Próximos Passos
🔹 Melhorar a performance das consultas.
🔹 Implementar autenticação e controle de acesso.
🔹 Criar testes automatizados para os endpoints.
🔹 Adicionar novos filtros e métricas.

👨‍💻 Autor
**Alex Soares**
📧 Email: alexsoares848@gmail.com
🌐 LinkedIn: linkedin.com/in/alexjsmartins

Se gostou do projeto, deixe uma ⭐ no repositório! 🚀🔥
