from collections import Counter

def produto_mais_vendido(produtos):
    """
    Determina o produto mais vendido em uma lista de produtos.

    Args:
        produtos (list): Lista de strings representando os produtos.

    Returns:
        str: O produto mais vendido.
    """

    # Utiliza o Counter para contar a frequência de cada produto de forma eficiente
    contagem = Counter(produtos)

    # Encontra o produto com a maior contagem
    produto_mais_vendido = contagem.most_common(1)[0][0]

    return produto_mais_vendido

def obter_entrada_produtos():
    """
    Obtém a entrada do usuário e converte em uma lista de produtos.

    Returns:
        list: Lista de strings representando os produtos.
    """

    # Solicita a entrada do usuário e divide em uma lista, removendo espaços em branco
    produtos = input().split(',')
    produtos = [produto.strip() for produto in produtos]

    return produtos

# Exemplo de uso
produtos = obter_entrada_produtos()
resultado = produto_mais_vendido(produtos)
print(resultado)