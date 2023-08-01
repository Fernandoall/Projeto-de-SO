def prioridade_preemptiva(processos):
    tempo_total_execucao = 0
    tempo_espera_total = 0
    tempo_atual = 0
    quantidade_processos = len(processos)

    while len(processos) > 0:
        # Encontre o processo de maior prioridade (menor valor de prioridade)
        menor_prioridade = min(processos, key=lambda x: x[2])
        indice_menor_prioridade = processos.index(menor_prioridade)
        processo_atual = processos[indice_menor_prioridade]

        # Remova o processo selecionado da lista
        processos.pop(indice_menor_prioridade)

        # Verifique se o processo precisa ser interrompido
        if processo_atual[1] > 0:
            # Tempo de espera para este processo é o tempo atual - tempo de chegada
            tempo_espera = tempo_atual - processo_atual[0]
            tempo_espera_total += tempo_espera

            # O tempo de execução é o tempo de chegada + tempo restante do processo
            tempo_atual += min(processo_atual[1], 1)
            processo_atual[1] -= 1

            # Reinsira o processo na lista se ainda tiver tempo restante
            if processo_atual[1] > 0:
                processos.append(processo_atual)

        # Atualize o tempo total de execução
        tempo_total_execucao = tempo_atual

    # Calcule o tempo médio de espera
    tempo_medio_espera = tempo_espera_total / quantidade_processos

    return tempo_total_execucao, tempo_medio_espera

# Exemplo de uso:
if __name__ == "__main__":
    lista_processos = [
        # Formato: [tempo_de_chegada, tempo_de_execucao, prioridade]
        [0, 5, 2],
        [1, 3, 1],
        [2, 6, 3],
        [4, 2, 4]
    ]

    tempo_total, tempo_medio_espera = prioridade_preemptiva(lista_processos)

    print(f"Tempo total de execução: {tempo_total} unidades de tempo")
    print(f"Tempo médio de espera: {tempo_medio_espera} unidades de tempo")
