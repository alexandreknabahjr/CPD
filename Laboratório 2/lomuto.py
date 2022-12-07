# Bibliotecas auxiliares usadas no programa
import random as r
import time as t

# Variáveis globais usadas no programa
SWAPS = 0
RECURSAO = 0

# Dicionário que contém os nomes dos arquivos de entrada fornecidos e os nomes dos arquivos de saida esperados
ARQUIVOS = {
    'INPUT_1' : 'entrada-quicksort.txt',
    'OUTPUT_1' : 'stats-aleatorio-lomuto.txt',
    'OUTPUT_2' : 'stats-mediana-lomuto.txt',
}

# Entradas:

# (a) vetor, que guarda os elementos lidos a partir do arquivo de entrada;
# (b) inicio, que é o comeco do vetor;
# (c) fim, que é o final do vetor;
# (d) swaps, que é o número de trocas realizadas pela funcao.

# Objetivo:

# um número aleatório é escolhido para ser usado como pivô.

def numero_randomico(vetor, inicio, fim, swaps):
    global SWAPS
    randomico = r.randint(inicio, fim)
    vetor[randomico], vetor[fim] = vetor[fim], vetor[randomico]
    SWAPS += 1

# Entradas:

# (a) vetor, que guarda os elementos lidos a partir do arquivo de entrada;
# (b) inicio, que é o comeco do vetor;
# (c) fim, que é o final do vetor;
# (d) swaps, que é o número de trocas realizadas pela funcao.

# Objetivo:

# um número entre três é escolhido para ser usado como pivô.

def mediana(vetor, inicio, fim, swaps):
    global SWAPS

    meio = (inicio + fim - 1) // 2

    if (vetor[inicio] >= vetor[fim]) and (vetor[fim] >= vetor[meio]):
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        SWAPS += 1
    elif (vetor[inicio] >= vetor[meio]) and (vetor[meio] >= vetor[fim]):
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        SWAPS += 1
    elif (vetor[meio] >= vetor[inicio]) and (vetor[inicio] >= vetor[fim]):
        vetor[meio], vetor[fim] = vetor[fim], vetor[meio]
        SWAPS += 1
    elif (vetor[meio] >= vetor[fim]) and (vetor[fim] >= vetor[inicio]):
        vetor[meio], vetor[fim] = vetor[fim], vetor[meio]
        SWAPS += 1

# Entradas:

# (a) vetor, que guarda os elementos lidos a partir do arquivo de entrada;
# (b) inicio, que é o comeco do vetor;
# (c) fim, que é o final do vetor;
# (d) swaps, que é o número de trocas realizadas pela funcao.

# Objetivo:

# pega o último elemento como pivô e o coloca na posição correta (em um vetor ordenado),
# além disso, agrupa os elementos menores do que o pivô no início do vetor e agrupa os elementos
# maiores do que o pivô no final do vetor.

def lomuto_particao(vetor, inicio, fim, swaps):
    global SWAPS

    # Guarda o elemento que está no final do vetor
    elemento_particao = vetor[fim]

    # Guarda o elemento anterior ao início
    i = (inicio - 1)

    # Percorre o vetor
    for j in range(inicio, fim):
        # Se o elemento particionador for maior ou igual ao elemento corrente, faz as trocas necessárias
        if(vetor[j] <= elemento_particao):
           i += 1
           vetor[i], vetor[j] = vetor[j], vetor[i]
           SWAPS += 1

    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    SWAPS += 1

    # Retorna o elemento a ser usado como particionador
    return (i + 1)

# Entradas:

# (a) vetor, que guarda os elementos lidos a partir do arquivo de entrada;
# (b) inicio, que é o comeco do vetor;
# (c) fim, que é o final do vetor;
# (d) swaps, que é o número de trocas realizadas pela funcao.

# Objetivo:

# organiza um vetor com base em um número aleatório e com base no particionamento de Lomuto.

def lomuto_randomico(vetor, inicio, fim, swaps):
    global RECURSAO
    global SWAPS
    if fim > inicio:
        RECURSAO += 1
        # Chamada da função numero_randomico
        numero_randomico(vetor, inicio, fim, SWAPS)
        # particao guarda o retorno da função lomuto_particao
        particao = lomuto_particao(vetor, inicio, fim, SWAPS)
        # Chamadas recursivas
        lomuto_randomico(vetor, inicio, particao - 1, SWAPS)
        lomuto_randomico(vetor, particao + 1, fim, SWAPS)
        
# Entradas:

# (a) vetor, que guarda os elementos lidos a partir do arquivo de entrada;
# (b) inicio, que é o comeco do vetor;
# (c) fim, que é o final do vetor;
# (d) swaps, que é o número de trocas realizadas pela funcao.

# Objetivo:

# organizar um vetor com base em um número escolhido entre três e com base no particionamento de Lomuto.

def lomuto_mediana(vetor, inicio, fim, swaps):
    global RECURSAO
    global SWAPS
    if fim > inicio:
        RECURSAO += 1
        # Chamada da função mediana
        mediana(vetor, inicio, fim, SWAPS)
        # particao guarda o retorno da função lomuto_particao
        particao = lomuto_particao(vetor, inicio, fim, SWAPS)
        # Chamadas recursivas
        lomuto_randomico(vetor, inicio, particao - 1, SWAPS)
        lomuto_randomico(vetor, particao + 1, fim, SWAPS)


# -----------------------------------------------------------------------------------------------
#                                       LOMUTO RANDOMICO
# -----------------------------------------------------------------------------------------------
    

# Abertura do primeiro arquivo de saida
saida1 = open(ARQUIVOS.get('OUTPUT_1'), 'w+')

with open(ARQUIVOS.get('INPUT_1'), 'r') as entrada:

    # Lê o total de linhas do arquivo de entrada
    total_linhas = entrada.readlines()

    # Loop que percorre todas as linhas do arquivo
    for linha in total_linhas:
        # Transforma a linha lida em uma lista
        vetor = list(map(int, linha.split()))
        # Exclui o primeiro elemento da linha, que é a quantidade de elementos do vetor
        del vetor[0]
        # Guarda o tamanho do vetor
        tamanho = len(vetor)

        # Cronometra o tempo inicial
        tempo_inicial = t.time()
        # Chamada da função criada
        lomuto_randomico(vetor, 0, tamanho - 1, SWAPS)
        # Cronometra o tempo final
        tempo_final = t.time() - tempo_inicial
        # Escrita no arquivo de saida
        saida1.write("TAMANHO ENTRADA " + str(tamanho) + "\nSWAPS " + str(SWAPS) + "\nRECURSOES "+ str(RECURSAO) + "\nTEMPO " + str("{:.7f}".format(tempo_final)) + "\n")
        # Zera as variáveis globais
        SWAPS = 0
        RECURSAO = 0
        
# Fechamento do primeiro arquivo de saída
saida1.close()

# Garantia que as variáveis globais foram zeradas
SWAPS = 0
RECURSAO = 0

# -----------------------------------------------------------------------------------------------
#                                       LOMUTO MEDIANA
# -----------------------------------------------------------------------------------------------

# Abertura do segundo arquivo de saida
saida2 = open(ARQUIVOS.get('OUTPUT_2'), 'w+')

with open(ARQUIVOS.get('INPUT_1'), 'r') as entrada:

    # Lê o total de linhas do arquivo de entrada
    total_linhas = entrada.readlines()

    # Loop que percorre todas as linhas do arquivo
    for linha in total_linhas:
        # Transforma a linha lida em uma lista
        vetor = list(map(int, linha.split()))
        # Exclui o primeiro elemento da linha, que é a quantidade de elementos do vetor
        del vetor[0]
        # Guarda o tamanho do vetor
        tamanho = len(vetor)

        # Cronometra o tempo inicial
        tempo_inicial = t.time()
        # Chamada da função criada
        lomuto_mediana(vetor, 0, tamanho - 1, SWAPS)
        # Cronometra o tempo final
        tempo_final = t.time() - tempo_inicial
        # Escrita no arquivo de saída
        saida2.write("TAMANHO ENTRADA " + str(tamanho) + "\nSWAPS " + str(SWAPS) + "\nRECURSOES "+ str(RECURSAO) + "\nTEMPO " + str("{:.7f}".format(tempo_final)) + "\n")
        # Zera as variáveis globais
        SWAPS = 0
        RECURSAO = 0
        
# Fechamento do segundo arquivo de saída
saida2.close()
