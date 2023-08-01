def alocacao_melhor_ajuste(blocos_memoria, tamanho_necessario):
    indice_melhor_ajuste = -1
    menor_tamanho_restante = float('inf')

    for i, tamanho_bloco in enumerate(blocos_memoria):
        if tamanho_bloco >= tamanho_necessario and tamanho_bloco - tamanho_necessario < menor_tamanho_restante:
            indice_melhor_ajuste = i
            menor_tamanho_restante = tamanho_bloco - tamanho_necessario

    if indice_melhor_ajuste != -1:
        blocos_memoria[indice_melhor_ajuste] -= tamanho_necessario

    return indice_melhor_ajuste

# Exemplo de uso:
if __name__ == "__main__":
    blocos_memoria = [100, 50, 200, 80, 150]
    tamanho_necessario = int(input())

    resultado = alocacao_melhor_ajuste(blocos_memoria, tamanho_necessario)

    if resultado != -1:
        print(f"Bloco {resultado + 1} alocado.")
    else:
        print("Nenhum bloco adequado encontrado.")
