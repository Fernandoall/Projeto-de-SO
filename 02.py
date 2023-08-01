def circular(fila_de_processos, quantum, troca_de_contexto):
    turn_around = [0] * len(fila_de_processos) # vai receber o tempo_atual em que cada processo terminou a execução
    # Nessa linha dois é criada uma array onde é guardado os tempos de cada processo
    # e O TEMPO em que foi finalizado a execução do quantum

    tempo_atual = 0 #Variável do tempo atual, contador de tempo
    while True: #Utilização do While true.
        if sum(fila_de_processos) <= 0:
            print("Todos os processos foram executados!") #Verificação PARA SABER SE TODOS OS PROCESSOS TIVERAM SEU TEMPO ZERADO #COMO ELE TÁ REDUZINDO CONFORME O PASSAR DO TEMPO, VAI CHEGAR UMA HORA QUE EM A SOMA DE TODOS OS TEMPOS IRÁ DAR ZERO  #E ELE ENCERRARÁ O ALGORITMO. CASO HAJA ALGUM PROCESSO COM TEMPO FALTANDO ELE CAI NO ELSE A SEGUIR
            break
        else:
            for i in range(len(fila_de_processos)): #A FINALIDADE DESSE FOR É REPETIR ESSA VERIFICAÇÃO PARA SABER SE O PROCESSO JÁ FOI FINALIZADO OU SE HÁ MAIS ALGUMA EXECUÇÃO
                if fila_de_processos[i] <= 0: #AQUI OCORRE A PRIMEIRA VERIFICAÇÃO, SE A FILA DE PROCESSO É IGUAL A ZERO.
                    print(f"\nP{i} já finalizado") #SENDO TRUE O RESULTADO ACIMA, É IMPRESSO A MENSAGEM DENTRO DO PRINTF, SENDO "JÁ FINALIZADO".
                elif fila_de_processos[i] <= quantum:  #AQUI É SE A CONDIÇÃO DO PROCESSO NÃO TER SIDO FINALIZADO E SE O TEMPO É MENOR OU IGUAL AO QUANTUM 
                    tempo_atual += fila_de_processos[i] #SE A CONDIÇÃO ACIMA FOR TRUE, É ACRESCENTADO NO TEMPO ATUAL O TAMANHO DO PROCESSO
                    fila_de_processos[i] -= fila_de_processos[i] #AQUI NESSA LINHA ELE ZERA O TEMPO DO PROCESSO

                    print(f"\nP{i} executa")
                    print(f"Termino em T-{tempo_atual}") #O IF A SEGUIR SERVE PARA VERIFICAR E EVITAR QUE SEJA ACRESCIDO O TEMPO NOVAMENTE
                    if fila_de_processos[i] == 0: #aQUI É VERIFICADO SE O PROCESSO FOI ZERADO
                        turn_around[i] = tempo_atual #AQUI O ALGORITMO PEGA O TEMPO ATUAL E IGUAL O NOVAMENTE
                        print(f"Processo P{i} terminou em T-{tempo_atual}")
                        print("TROCA DE CONTEXTO")
                        tempo_atual += troca_de_contexto

                    else: #CASO A CONDIÇÃO ACIMA SEJA FALSO, OU SEJA SE O TEMPO NÃO É ZERO OU NÃO É MENOR OU IGUAL AO QUANTUM, ELE É MAIOR.
                        tempo_atual += quantum #NESSA VERIFICAÇÃO ATUAL ELE PEGA O TEMPO ATUAL E ACRESCENTA AO QUANTUM.
                        fila_de_processos[i] -= quantum #AQUI ELE PEGA O PROCESSO E DIMINUI DO QUANTUM 

                        print(f"\nP{i} executa") #ESSA LINHA É BASICAMENTE PARA INFORMAR QUE VAI ACONTECER UMA TROCA DE CONTEXTO
                        print(f"Termino em T-{tempo_atual}") #ESSA LINHA É BASICAMENTE PARA INFORMAR QUE VAI ACONTECER UMA TROCA DE CONTEXTO
                        print ("TROCA DE CONTEXTO") #ESSA LINHA É BASICAMENTE PARA INFORMAR QUE VAI ACONTECER UMA TROCA DE CONTEXTO
                        tempo_atual += troca_de_contexto #SOMASSE AO TEMPO A TROCA DE CONTEXTO
                        turn_around[i] = tempo_atual #ENQUANTO O PROCESSADOR TIVER PROCESSOS COM TEMPO PARA SER EXECUTADO É ACRESCIDO NESSA LINHA
                        print("-" * 30)

    print(f"Tempo onde Terminou cada processo: {turn_around}")
    return turn_around

def tempo_atual_medio_turnaround(lista_de_processos, lista_de_tempos): #FUNÇÃO CRIADA PARA CALCULAR O TEMPO MÉDIO DE TURNAROUND
    resultado = sum(lista_de_tempos) / (len(lista_de_processos)) #NESASA LINHA É SOMADO OS TEMPOS E O RESULTADO É DIVIDO PELA QUANTIDADE DE PROCESSOS
    print(f"Tempo Médio de Turnaround = {resultado:.2f}") #AQUI É IMPRESSO O TEMPO MÉDIO E A VARIÁVEL RESULTADO JÁ COM O RESULTADO DO CALCULO

if __name__ == '__main__':
    fila_de_processos = [40, 20, 50, 30] 
    quantum = 20
    troca_de_contexto = 5

    #fila_de_processos = [40, 20]
    #quantum = 20
    #troca_de_contexto = 5

    #fila_de_processos [10, 7, 8]
    #quantum = 3
    #troca_de_contexto = 1

    turnAround = circular(fila_de_processos, quantum, troca_de_contexto) #ESSA FUNÇÃO QUE FOI CRIADA NA LINHA 1 É CHAMADA AQUI PARA 
    tempo_atual_medio_turnaround(fila_de_processos, turnAround)
        
    # Função que estará executando o algoritmo