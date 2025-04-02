# Documentação do Endpoint: Melhor Filtro

## Descrição

O endpoint `/melhor` retorna o melhor elemento dentro de uma determinada categoria de vendas, como o melhor vendedor, melhor produto, melhor cidade ou melhor loja.

## URL do Endpoint

```
GET /melhor
```

## Parâmetros da Requisição

Os seguintes parâmetros podem ser passados via query string:

| Parâmetro     | Tipo   | Obrigatório | Descrição |
|--------------|------|------------|------------|
| `tipo`       | string | Sim | Define qual métrica será analisada. Pode ser: `nome do empregado`, `nome do produto`, `cidade do ponto de venda`, `nome do ponto de venda`. |
| `Supercategoria` | string | Não | Filtra os resultados por categoria. |
| `mes`        | int | Não | Filtra os resultados pelo mês. |
| `ano`        | int | Não | Filtra os resultados pelo ano. |
| `limite`     | int | Não | Define quantos resultados serão retornados. O padrão é `1`. |

## Exemplo de Requisição

```bash
GET /melhor?tipo=nome%20do%20empregado&mes=3&ano=2024
```

## Exemplo de Resposta

```json
{
    "melhor_nome do empregado": [
        {
            "Nome do empregado": "João Silva",
            "Online": 15000
        }
    ]
}
```

## Possíveis Códigos de Resposta

| Código | Descrição |
|--------|------------|
| 200 | Requisição bem-sucedida. |
| 400 | Parâmetro `tipo` inválido. |
| 500 | Erro interno do servidor. |

## Observações

- Se `tipo` não for passado ou for inválido, a API retornará um erro.
- O campo `limite` permite exibir mais de um resultado caso desejado.

---

Essa documentação ajuda a entender como interagir com o endpoint `/melhor`. Para mais detalhes sobre os filtros disponíveis, veja a documentação geral do projeto.

