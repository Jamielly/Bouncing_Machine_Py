class B_Machine
def maquina_saltitante(instrucoes):
    # Encontrando as dimensões do tabuleiro e a posição inicial
    x_min, x_max, y_min, y_max = 0, 0, 0, 0
    x, y = 0, 0

    for instrucao in instrucoes:
        direcao, passos = instrucao[0], int(instrucao[2])

        if direcao == 'C':
            y -= passos
            y_min = min(y_min, y)
        elif direcao == 'B':
            y += passos
            y_max = max(y_max, y)
        elif direcao == 'E':
            x -= passos
            x_min = min(x_min, x)
        elif direcao == 'D':
            x += passos
            x_max = max(x_max, x)

    # Calculo das dimensões do mapa final
    width = x_max - x_min + 1
    height = y_max - y_min + 1

    # Crie um mapa vazio preenchido com 'O'
    mapa = [['O'] * width for _ in range(height)]

    # Reposicionamento da máquina na posição inicial
    x_offset = -x_min
    y_offset = -y_min

    for instrucao in instrucoes:
        direcao, passos = instrucao[0], int(instrucao[2])

        if direcao == 'C':
            for i in range(passos):
                mapa[y_offset - i][x_offset] = 'X'
            y_offset -= passos
        elif direcao == 'B':
            for i in range(passos):
                mapa[y_offset + i][x_offset] = 'X'
            y_offset += passos
        elif direcao == 'E':
            for i in range(passos):
                mapa[y_offset][x_offset - i] = 'X'
            x_offset -= passos
        elif direcao == 'D':
            for i in range(passos):
                mapa[y_offset][x_offset + i] = 'X'
            x_offset += passos

    return mapa
