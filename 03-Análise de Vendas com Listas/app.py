def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)  # Calcula o total da lista
    media_vendas = total_vendas / len(vendas)  # Calcula a média
    return f"{total_vendas}, {media_vendas:.2f}"    

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas = list(map(int, entrada.split(',')))  # Converte a string em lista de inteiros    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
