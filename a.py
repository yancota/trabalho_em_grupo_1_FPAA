import heapq

def a_estrela(labirinto, inicio, fim):
    def heuristica(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    fila_aberta = []
    heapq.heappush(fila_aberta, (0, inicio))  
    veio_de = {}  
    custo_g = {inicio: 0}  
    custo_f = {inicio: heuristica(inicio, fim)} 

    while fila_aberta:
        _, atual = heapq.heappop(fila_aberta)

        if atual == fim:
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            return caminho[::-1]  

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            vizinho = (atual[0] + dx, atual[1] + dy)

            if 0 <= vizinho[0] < len(labirinto) and 0 <= vizinho[1] < len(labirinto[0]) and labirinto[vizinho[0]][vizinho[1]] != 1:
                custo_g_tentativo = custo_g[atual] + 1  

                if vizinho not in custo_g or custo_g_tentativo < custo_g[vizinho]:
                    veio_de[vizinho] = atual
                    custo_g[vizinho] = custo_g_tentativo
                    custo_f[vizinho] = custo_g_tentativo + heuristica(vizinho, fim)
                    heapq.heappush(fila_aberta, (custo_f[vizinho], vizinho))

    return None

def imprimir_labirinto_com_caminho(labirinto, caminho):
    labirinto_com_caminho = [linha[:] for linha in labirinto]  
    for x, y in caminho:
        if labirinto_com_caminho[x][y] == 0:  
            labirinto_com_caminho[x][y] = '*'
    for linha in labirinto_com_caminho:
        print(' '.join(str(celula) for celula in linha))

def processar_labirinto(labirinto):
    inicio, fim = None, None
    labirinto_numerico = []
    for i, linha in enumerate(labirinto):
        nova_linha = []
        for j, celula in enumerate(linha):
            if celula == 'S':
                inicio = (i, j)
                nova_linha.append(0)
            elif celula == 'E':
                fim = (i, j)
                nova_linha.append(0)
            elif celula == 0 or celula == 1:
                nova_linha.append(celula)
            else:
                raise ValueError("Labirinto contém valores inválidos.")
        labirinto_numerico.append(nova_linha)
    if inicio is None or fim is None:
        raise ValueError("Labirinto deve conter um ponto inicial 'S' e um ponto final 'E'.")
    return labirinto_numerico, inicio, fim

labirinto = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 'E', 1]
]

labirinto_numerico, inicio, fim = processar_labirinto(labirinto)

caminho = a_estrela(labirinto_numerico, inicio, fim)

if caminho:
    print("Caminho encontrado:")
    print(caminho)
    print("\nLabirinto com o caminho:")
    imprimir_labirinto_com_caminho(labirinto_numerico, caminho)
else:
    print("Nenhum caminho encontrado.")

    if __name__ == "__main__":
        try:
            labirinto_numerico, inicio, fim = processar_labirinto(labirinto)
            caminho = a_estrela(labirinto_numerico, inicio, fim)

            if caminho:
                print("Caminho encontrado:")
                print(caminho)
                print("\nLabirinto com o caminho:")
                imprimir_labirinto_com_caminho(labirinto_numerico, caminho)
            else:
                print("Nenhum caminho encontrado.")
        except ValueError as e:
            print(f"Erro: {e}")
