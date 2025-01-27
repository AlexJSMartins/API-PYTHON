import pandas as pd

# Caminho do arquivo Excel
PLANILHA_CAMINHO = "./planilha/VENDAS SEM IMEIS.xlsx"


def carregar_dados():
    df = pd.read_excel(PLANILHA_CAMINHO)
    df['Data da pesquisa'] = pd.to_datetime(df['Data da pesquisa'], format='%d/%m/%Y', errors='coerce')  # Garante formato datetime

    # Uniformizar colunas relevantes em letras minúsculas
    colunas_para_uniformizar = [
        "Nome do empregado",
        "Nome do produto",
        "Cidade do ponto de venda",
        "Nome do ponto de venda",
        "Supercategoria",
        "Bandeira"
    ]

    for coluna in colunas_para_uniformizar:
        if coluna in df.columns:
            df[coluna] = df[coluna].str.lower()  # Converte para letras minúsculas

    return df


# Função genérica para aplicar filtros
def aplicar_filtros(df, categoria=None, mes=None, ano=None):
    # Filtrar por mês e ano, se fornecido
    if mes:
        df = df[df['Data da pesquisa'].dt.month == int(mes)]
    if ano:
        df = df[df['Data da pesquisa'].dt.year == int(ano)]

    # Filtrar por categoria (tratando caso seja enviado em letras maiúsculas ou minúsculas)
    if categoria:
        df = df[df['Supercategoria'].str.lower() == categoria.lower()]

    return df


# Função genérica para agrupar e calcular o ranking
def calcular_ranking(df, coluna_agrupamento, limite=1):
    """
    Agrupa a base de dados pela coluna especificada e calcula o ranking com base nas vendas 'Online'.
    """
    resultado = df.groupby(coluna_agrupamento)["Online"].sum().reset_index()
    resultado = resultado.sort_values(by="Online", ascending=False).head(limite)
    return resultado
