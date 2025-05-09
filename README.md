# Resolução de Labirinto com A*

### Alunos
- Lucas Henrique Chaves de Barros
- Yan Mariz Magalhães Cota

## Descrição

Implementação do algoritmo A* para encontrar o menor caminho entre dois pontos em um labirinto representado por uma matriz. O labirinto contém obstáculos e permite apenas movimentos ortogonais (cima, baixo, esquerda, direita).

## Introdução

O algoritmo A* é uma técnica de busca heurística que combina:
 - Custo acumulado do caminho percorrido desde o ponto de início.
 - Estimativa da distância restante até o destino, calculada por uma heurística.
Neste projeto, usamos a distância de Manhattan como heurística, adequada para ambientes com movimento apenas horizontal e vertical. Essa abordagem garante um caminho ótimo se a heurística for admissível, como é o caso aqui.

A estratégia do A* permite encontrar o menor caminho mesmo em labirintos complexos com obstáculos.

## Como rodar o projeto

Instalar a última versão do python disponível em: https://www.python.org/downloads/

Necessário rodar o seguinte comando no terminal:
```bash
https://github.com/yancota/CaminhoHamiltoniano.git
```

Rodar o seguinte comando no terminal:
```bash
python main.py
```

## Versão do Python
Este projeto foi desenvolvido na versão 3.13.2 do Python.

## Funcionamento do Algoritmo A*

### Funções

### encontrar_inicio_fim(labirinto)
- Localiza as coordenadas de início ('S') e fim ('E') no labirinto.

### heuristica(a, b)
- Calcula a distância de Manhattan entre dois pontos, utilizada como heurística.

### a_estrela(labirinto)
- Implementa o algoritmo A*, utilizando:
 - g(n): custo do caminho percorrido desde o início até o ponto n.
 - h(n): heurística da distância de Manhattan até o ponto final.
 - f(n) = g(n) + h(n): custo estimado total do caminho passando por n.
- O algoritmo mantém uma fila de prioridade com os caminhos mais promissores, e expande os vizinhos válidos (não obstáculos) buscando sempre o menor f(n).

### destacar_caminho(labirinto, caminho)
- Marca o caminho encontrado com * na matriz do labirinto.

### exibir_labirinto(labirinto)
- Exibe o labirinto no terminal de forma legível.

### Exemplo de Entrada

```bash
labirinto = [
    ['S', '0', '1'],
    ['1', '0', '1'],
    ['1', '0', 'E']
]
```

### Exemplo de Saída

Labirinto Original
```bash
S 0 1
1 0 1
1 0 E
```

Menor Caminho Encontrado
```bash
['s', (0, 1), (1, 1), (2, 1), 'e']
```

Labirinto com Caminho Destacado
```bash
S * 1
1 * 1
1 * E
```