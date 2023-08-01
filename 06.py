class Processo:
    def __init__(self, pid, tamanho_memoria, tempo_execucao, prioridade):
        self.pid = pid
        self.tamanho_memoria = tamanho_memoria
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade


def alocacao_best_fit(blocos_memoria, processo):
    best_fit_index = -1
    smallest_remaining_size = float('inf')

    for i, tamanho_bloco in enumerate(blocos_memoria):
        if tamanho_bloco >= processo.tamanho_memoria and tamanho_bloco - processo.tamanho_memoria < smallest_remaining_size:
            best_fit_index = i
            smallest_remaining_size = tamanho_bloco - processo.tamanho_memoria

    return best_fit_index


def agendador_processos(processos, tamanho_total_memoria, quantum_round_robin):
    # Ordenar a lista de processos por prioridade (maior prioridade primeiro)
    processos.sort(key=lambda p: p.prioridade, reverse=True)

    # Inicializar a lista de blocos de memória com um bloco que representa toda a memória disponível
    blocos_memoria = [tamanho_total_memoria]

    ordem_execucao = []  # Lista para armazenar a ordem de execução dos processos

    while len(processos) > 0:
        processo_atual = processos.pop(0)  # Obter o primeiro processo da lista (maior prioridade)

        # Verificar se o processo pode ser alocado na memória
        bloco_alocado = alocacao_best_fit(blocos_memoria, processo_atual)

        if bloco_alocado != -1:
            # Alocar o processo no bloco encontrado
            bloco_atual = blocos_memoria[bloco_alocado]
            bloco_tamanho_restante = bloco_atual - processo_atual.tamanho_memoria

            # Atualizar o tamanho do bloco alocado (parte usada pelo processo)
            blocos_memoria[bloco_alocado] = processo_atual.tamanho_memoria

            # Adicionar o processo à ordem de execução
            ordem_execucao.append(processo_atual.pid)

            # Verificar se há espaço restante no bloco para ser utilizado por outros processos
            if bloco_tamanho_restante > 0:
                # Inserir o novo bloco livre ordenadamente na lista de blocos
                blocos_memoria.insert(bloco_alocado + 1, bloco_tamanho_restante)

            # Atualizar o tempo restante do processo com o tempo de execução ou o quantum restante, o que for menor
            tempo_execucao = min(quantum_round_robin, processo_atual.tempo_execucao)
            processo_atual.tempo_execucao -= tempo_execucao

            # Reagendar o processo caso ainda haja tempo de execução restante
            if processo_atual.tempo_execucao > 0:
                processos.append(processo_atual)
        else:
            print(f"Processo {processo_atual.pid} não pode ser alocado na memória e será ignorado.")

    return ordem_execucao, blocos_memoria


# Exemplo de uso:
if __name__ == "__main__":
    # Lista de processos (pid, tamanho_memoria, tempo_execucao, prioridade)
    lista_processos = [
        Processo(1, 50, 20, 2),
        Processo(2, 100, 40, 1),
        Processo(3, 70, 30, 3),
        Processo(4, 30, 10, 4)
    ]

    tamanho_total_memoria = 200
    quantum_round_robin = 5

    ordem_execucao, blocos_memoria = agendador_processos(lista_processos, tamanho_total_memoria, quantum_round_robin)

    print("Ordem de execução dos processos:")
    print(ordem_execucao)

    print("\nBlocos de memória alocados:")
    for i, tamanho_bloco in enumerate(blocos_memoria):
        print(f"Bloco {i+1}: {tamanho_bloco} unidades de memória")
