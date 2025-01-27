

from django.http import JsonResponse
from .utils import carregar_dados, aplicar_filtros, calcular_ranking

def melhor(request):
    """
    Endpoint genérico para os filtros (melhor em diversas categorias).
    """
    # Parâmetros da requisição
    tipo = request.GET.get('tipo')
    categoria = request.GET.get('Supercategoria', None)
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)
    limite = request.GET.get('limite', 1)  # Limite para o ranking (padrão: 1)

    if tipo:
        tipo = tipo.lower()  # Converte o tipo para minúsculas

    # Validação do parâmetro 'tipo'
    tipos_validos = {
        "nome do empregado": "Nome do empregado",
        "nome do produto": "Nome do produto",
        "cidade do ponto de venda": "Cidade do ponto de venda",
        "nome do ponto de venda": "Nome do ponto de venda",
    }
    if tipo not in tipos_validos:
        return JsonResponse(
            {"error": f"Tipo '{tipo}' inválido. Escolha entre: {', '.join(tipos_validos.keys())}."},
            status=400
        )

    # Carregar dados e aplicar filtros
    df = carregar_dados()
    df = aplicar_filtros(df, categoria, mes, ano)

    # Calcular ranking
    coluna_agrupamento = tipos_validos[tipo]
    resultado = calcular_ranking(df, coluna_agrupamento, limite=int(limite))

    # Retornar o resultado
    return JsonResponse({f"melhor_{tipo}": resultado.to_dict(orient="records")})

def ranking(request):
    """
    Endpoint para retornar um ranking completo (não apenas o melhor).
    """
    tipo = request.GET.get('tipo')
    categoria = request.GET.get('Supercategoria', None)
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)

    if tipo:
        tipo = tipo.lower()  # Converte o tipo para minúsculas

    # Validação do parâmetro 'tipo'
    tipos_validos = {
        "nome do empregado": "Nome do empregado",
        "nome do produto": "Nome do produto",
        "cidade do ponto de venda": "Cidade do ponto de venda",
        "nome do ponto de venda": "Nome do ponto de venda",
    }
    if tipo not in tipos_validos:
        return JsonResponse(
            {"error": f"Tipo '{tipo}' inválido. Escolha entre: {', '.join(tipos_validos.keys())}."},
            status=400
        )

    # Carregar dados e aplicar filtros
    df = carregar_dados()
    df = aplicar_filtros(df, categoria, mes, ano)

    # Calcular ranking completo
    coluna_agrupamento = tipos_validos[tipo]
    resultado = calcular_ranking(df, coluna_agrupamento, limite=len(df))

    # Retornar o resultado
    return JsonResponse({f"ranking_{tipo}": resultado.to_dict(orient="records")})

def melhor_vendedor_por_categoria(request):
    """
    Retorna o melhor vendedor por categoria e o produto mais vendido dessa categoria por vendedor.
    """
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)

    # Carregar dados e aplicar filtros de mês/ano
    df = carregar_dados()
    df = aplicar_filtros(df, mes=mes, ano=ano)

    # Agrupar por categoria e vendedor
    resultado = []
    for categoria, grupo in df.groupby("Supercategoria"):
        # Melhor vendedor por categoria
        vendas_vendedor = grupo.groupby("Nome do empregado")["Online"].sum().reset_index()
        melhor_vendedor = vendas_vendedor.sort_values(by="Online", ascending=False).head(1)

        if not melhor_vendedor.empty:
            vendedor = melhor_vendedor.iloc[0]["Nome do empregado"]

            # Produto mais vendido do melhor vendedor nessa categoria
            produtos_vendedor = grupo[grupo["Nome do empregado"] == vendedor]
            produto_vendas = produtos_vendedor.groupby("Nome do produto")["Online"].sum().reset_index()
            produto_mais_vendido = produto_vendas.sort_values(by="Online", ascending=False).head(1)

            resultado.append({
                "categoria": categoria,
                "melhor_vendedor": vendedor,
                "vendas_totais": melhor_vendedor.iloc[0]["Online"],
                "produto_mais_vendido": produto_mais_vendido.to_dict(orient="records")
            })

    return JsonResponse({"melhor_vendedor_por_categoria": resultado})

def analise_por_empregado(request):
    """
    Retorna uma análise detalhada dos dados de vendas de um empregado.
    """
    empregado = request.GET.get('empregado', None)
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)


    if not empregado:
        return JsonResponse({"error": "Parâmetro 'empregado' é obrigatório."}, status=400)

    # Carregar dados e aplicar filtros de mês/ano
    df = carregar_dados()
    df = aplicar_filtros(df, mes=mes, ano=ano)

    # Filtrar dados do empregado
    df_empregado = df[df["Nome do empregado"] == empregado]

    if df_empregado.empty:
        return JsonResponse({"error": f"Nenhum dado encontrado para o empregado '{empregado}'."}, status=404)

    # Total de vendas por mês
    vendas_por_mes = df_empregado.groupby(df_empregado["Data da pesquisa"].dt.month)["Online"].sum().reset_index()
    vendas_por_mes.columns = ["mes", "vendas_totais"]

    # Melhor mês
    melhor_mes = vendas_por_mes.sort_values(by="vendas_totais", ascending=False).head(1)

    # Total de vendas por categoria
    vendas_por_categoria = df_empregado.groupby("Supercategoria")["Online"].sum().reset_index()
    vendas_por_categoria.columns = ["categoria", "vendas_totais"]

    # Produto mais vendido por categoria
    produtos_por_categoria = []
    for categoria, grupo in df_empregado.groupby("Supercategoria"):
        produto_vendas = grupo.groupby("Nome do produto")["Online"].sum().reset_index()
        produto_mais_vendido = produto_vendas.sort_values(by="Online", ascending=False).head(1)
        produtos_por_categoria.append({
            "categoria": categoria,
            "produto_mais_vendido": produto_mais_vendido.to_dict(orient="records")
        })

    return JsonResponse({
        "empregado": empregado,
        "vendas_por_mes": vendas_por_mes.to_dict(orient="records"),
        "melhor_mes": melhor_mes.to_dict(orient="records"),
        "vendas_por_categoria": vendas_por_categoria.to_dict(orient="records"),
        "produtos_por_categoria": produtos_por_categoria
    })


def analise_por_cidade(request):
    """
    Retorna uma análise detalhada dos dados de vendas de uma cidade.
    """
    cidade = request.GET.get('cidade', None)
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)


    if not cidade:
        return JsonResponse({"error": "Parâmetro 'cidade' é obrigatório."}, status=400)

    # Carregar dados e aplicar filtros de mês/ano
    df = carregar_dados()
    df = aplicar_filtros(df, mes=mes, ano=ano)

    # Filtrar dados da cidade
    df_cidade = df[df["Cidade do ponto de venda"] == cidade]

    if df_cidade.empty:
        return JsonResponse({"error": f"Nenhum dado encontrado para a cidade '{cidade}'."}, status=404)

    # Total de vendas por mês
    vendas_por_mes = df_cidade.groupby(df_cidade["Data da pesquisa"].dt.month)["Online"].sum().reset_index()
    vendas_por_mes.columns = ["mes", "vendas_totais"]

    # Melhor mês
    melhor_mes = vendas_por_mes.sort_values(by="vendas_totais", ascending=False).head(1)

    # Total de vendas por categoria
    vendas_por_categoria = df_cidade.groupby("Supercategoria")["Online"].sum().reset_index()
    vendas_por_categoria.columns = ["categoria", "vendas_totais"]

    # Produto mais vendido por categoria
    produtos_por_categoria = []
    for categoria, grupo in df_cidade.groupby("Supercategoria"):
        produto_vendas = grupo.groupby("Nome do produto")["Online"].sum().reset_index()
        produto_mais_vendido = produto_vendas.sort_values(by="Online", ascending=False).head(1)
        produtos_por_categoria.append({
            "categoria": categoria,
            "produto_mais_vendido": produto_mais_vendido.to_dict(orient="records")
        })

    return JsonResponse({
        "cidade": cidade,
        "vendas_por_mes": vendas_por_mes.to_dict(orient="records"),
        "melhor_mes": melhor_mes.to_dict(orient="records"),
        "vendas_por_categoria": vendas_por_categoria.to_dict(orient="records"),
        "produtos_por_categoria": produtos_por_categoria
    })


def analise_por_bandeira(request):
    """
    Retorna uma análise detalhada dos dados de vendas de uma bandeira.
    """
    bandeira = request.GET.get('bandeira', None)
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)



    if not bandeira:
        return JsonResponse({"error": "Parâmetro 'bandeira' é obrigatório."}, status=400)

    # Carregar dados e aplicar filtros de mês/ano
    df = carregar_dados()
    df = aplicar_filtros(df, mes=mes, ano=ano)

    # Filtrar dados da bandeira
    df_bandeira = df[df["Bandeira"] == bandeira]

    if df_bandeira.empty:
        return JsonResponse({"error": f"Nenhum dado encontrado para a bandeira '{bandeira}'."}, status=404)

    # Total de vendas por mês
    vendas_por_mes = df_bandeira.groupby(df_bandeira["Data da pesquisa"].dt.month)["Online"].sum().reset_index()
    vendas_por_mes.columns = ["mes", "vendas_totais"]

    # Melhor mês
    melhor_mes = vendas_por_mes.sort_values(by="vendas_totais", ascending=False).head(1)

    # Total de vendas por categoria
    vendas_por_categoria = df_bandeira.groupby("Supercategoria")["Online"].sum().reset_index()
    vendas_por_categoria.columns = ["categoria", "vendas_totais"]

    # Produto mais vendido por categoria
    produtos_por_categoria = []
    for categoria, grupo in df_bandeira.groupby("Supercategoria"):
        produto_vendas = grupo.groupby("Nome do produto")["Online"].sum().reset_index()
        produto_mais_vendido = produto_vendas.sort_values(by="Online", ascending=False).head(1)
        produtos_por_categoria.append({
            "categoria": categoria,
            "produto_mais_vendido": produto_mais_vendido.to_dict(orient="records")
        })

    return JsonResponse({
        "bandeira": bandeira,
        "vendas_por_mes": vendas_por_mes.to_dict(orient="records"),
        "melhor_mes": melhor_mes.to_dict(orient="records"),
        "vendas_por_categoria": vendas_por_categoria.to_dict(orient="records"),
        "produtos_por_categoria": produtos_por_categoria
    })


def melhor_para_cidade_ou_bandeira(request):
    """
    Retorna o melhor Cidade ou Bandeira com base no total de vendas.
    """
    tipo = request.GET.get('tipo', None)  # 'cidade' ou 'bandeira'
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)

    if tipo:
        tipo = tipo.lower()  # Converte o tipo para minúsculas

    if tipo not in ['cidade', 'bandeira']:
        return JsonResponse({
            "error": "Parâmetro 'tipo' inválido. Escolha entre: 'cidade' ou 'bandeira'."
        }, status=400)

    # Carregar dados e aplicar filtros
    df = carregar_dados()
    df = aplicar_filtros(df, mes=mes, ano=ano)

    # Selecionar a coluna correta
    coluna = "Cidade do ponto de venda" if tipo == "cidade" else "Bandeira"

    # Agrupar e calcular total de vendas
    resultado = df.groupby(coluna)["Online"].sum().reset_index()
    resultado = resultado.sort_values(by="Online", ascending=False).head(1)

    return JsonResponse({
        f"melhor_{tipo}": resultado.to_dict(orient="records")
    })


def ranking_para_cidade_ou_bandeira(request):
    """
    Retorna o ranking completo para Cidades ou Bandeiras com base no total de vendas.
    """
    tipo = request.GET.get('tipo', None)  # 'cidade' ou 'bandeira'
    mes = request.GET.get('mes', None)
    ano = request.GET.get('ano', None)

    if tipo:
        tipo = tipo.lower()  # Converte o tipo para minúsculas

    if tipo not in ['cidade', 'bandeira']:
        return JsonResponse({
            "error": "Parâmetro 'tipo' inválido. Escolha entre: 'cidade' ou 'bandeira'."
        }, status=400)

    # Carregar dados e aplicar filtros
    df = carregar_dados()
    df = aplicar_filtros(df, mes=mes, ano=ano)

    # Selecionar a coluna correta
    coluna = "Cidade do ponto de venda" if tipo == "cidade" else "Bandeira"

    # Agrupar e calcular total de vendas
    ranking = df.groupby(coluna)["Online"].sum().reset_index()
    ranking = ranking.sort_values(by="Online", ascending=False)

    return JsonResponse({
        f"ranking_{tipo}": ranking.to_dict(orient="records")
    })
