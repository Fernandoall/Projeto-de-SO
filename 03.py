def escalona_por_prioridade(processos):
    tempo_total_execucao = 0
    tempo_medio_espera = 0
    tempo_atual = 0
    numero_processos = len(processos)
    tempos_espera = [0] * numero_processos

    for i in range(numero_processos):
        tempo_total_execucao += processos[i][1]

    while numero_processos > 0:
        menor_prioridade = float('inf')
        proximo_processo = None

        for i, processo in enumerate(processos):
            if processo[2] < menor_prioridade and processo[1] > 0:
                menor_prioridade = processo[2]
                proximo_processo = i

        if proximo_processo is not None:
            processo_executado = processos[proximo_processo]
            if processo_executado[1] == processos[proximo_processo][1]:
                tempos_espera[proximo_processo] = tempo_atual - processos[proximo_processo][0]
            processos[proximo_processo][1] -= 1
            tempo_atual += 1

            if processos[proximo_processo][1] == 0:
                numero_processos -= 1

    tempo_medio_espera = sum(tempos_espera) / len(tempos_espera)

    return tempo_total_execucao, tempo_medio_espera

if __name__ == "__main__":
    # Exemplo de uso
    processos = [
        # (tempo de chegada, tempo de execução, prioridade)
        (0, 5, 3),
        (1, 3, 1),
        (2, 4, 2),
    ]

    tempo_total, tempo_medio = escalona_por_prioridade(processos)
    print(f"Tempo total de execução: {tempo_total}")
    print(f"Tempo médio de espera: {tempo_medio}")