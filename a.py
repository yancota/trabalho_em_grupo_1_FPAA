import heapq

def encontrar_inicio_fim(labirinto):
    inicio = fim = None
    for i, linha in enumerate(labirinto):
        for j, valor in enumerate(linha):
            if valor == 'S':
                inicio = (i, j)
            elif valor == 'E':
                fim = (i, j)
    return inicio, fim

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_estrela(labirinto):
    inicio, fim = encontrar_inicio_fim(labirinto)
    if not inicio or not fim:
        return "Erro: 'S' ou 'E' não encontrados."

    linhas, colunas = len(labirinto), len(labirinto[0])
    fila = []
    heapq.heappush(fila, (0, inicio))
    
    veio_de = {inicio: None}
    custo_ate_agora = {inicio: 0}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.reverse()
            return caminho

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            vizinho = (atual[0] + dx, atual[1] + dy)
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if labirinto[vizinho[0]][vizinho[1]] != '1':
                    novo_custo = custo_ate_agora[atual] + 1
                    if vizinho not in custo_ate_agora or novo_custo < custo_ate_agora[vizinho]:
                        custo_ate_agora[vizinho] = novo_custo
                        prioridade = novo_custo + heuristica(fim, vizinho)
                        heapq.heappush(fila, (prioridade, vizinho))
                        veio_de[vizinho] = atual

    return "Sem solução"

def destacar_caminho(labirinto, caminho):
    labirinto_copia = [linha[:] for linha in labirinto]
    for i, j in caminho[1:-1]:
        labirinto_copia[i][j] = '*'
    return labirinto_copia

def exibir_labirinto(labirinto):
    for linha in labirinto:
        print(' '.join(str(c) for c in linha))

labirinto = [
    ['S', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', 'E']
]

print("Labirinto original:")
exibir_labirinto(labirinto)

caminho = a_estrela(labirinto)
if isinstance(caminho, str):
    print(caminho)
else:
    print("\nMenor caminho (em coordenadas):")
    print(['s' if (i == caminho[0]) else 'e' if (i == caminho[-1]) else i for i in caminho])
    print("\nLabirinto com o caminho destacado:")
    labirinto_destacado = destacar_caminho(labirinto, caminho)
    exibir_labirinto(labirinto_destacado)
