import numpy as np


# *****************************************************************************
def numero_de_elementos(n_el_y: int, n_el_x: int) -> int:
    '''
    ----------------------------------------------------------------------------
    Gera as coordenadas da malha
    ----------------------------------------------------------------------------
    @param n_el_y - Numero de divisoes na direcao y
    @param n_el_x - NUmero de divisoes na direcao x
    ----------------------------------------------------------------------------
    @return Retorna o numero de elementos
    ----------------------------------------------------------------------------
    '''

    return n_el_y * n_el_x


# *****************************************************************************

# *****************************************************************************
def numero_nos(n_el_y: int, n_el_x: int):
    '''
    ----------------------------------------------------------------------------
    Gera as coordenadas da malha
    ----------------------------------------------------------------------------
    @param n_el_y - Numero de divisoes na direcao y
    @param n_el_x - NUmero de divisoes na direcao x
    ----------------------------------------------------------------------------
    @return Retorna uma tupla (a, b, c):
       a : Numero de nos na direcao y
       b : Numero de nos na direcao x
       c : Numero total de nos
    ----------------------------------------------------------------------------
    '''
    n_nos_y = n_el_y + 1
    n_nos_x = n_el_x + 1

    numero_de_nos = n_nos_x * n_nos_y

    return n_nos_y, n_nos_x, numero_de_nos


# *****************************************************************************

# *****************************************************************************
def dy_dx_elemento(n_el_y: int, n_el_x: int, L_y: float, L_x: float):
    '''
    ----------------------------------------------------------------------------
    Calcula a aresta dos elementos
    ----------------------------------------------------------------------------
    @param n_el_y - Numero de divisoes na direcao y
    @param n_el_x - Numero de divisoes na direcao x
    @param L_y    - Dimensao y do retangulo
    @param L_x    - Dimensao x do retangulo
    ----------------------------------------------------------------------------
    @return Retorna uma tupla (dy, dx):
       dy : aresta na direcao y do elemento
       dx : aresta na direcao y do elemento
    ----------------------------------------------------------------------------
    '''
    return L_y / n_el_y, L_x / n_el_x


# *****************************************************************************

# *****************************************************************************
def gerando_coordenadas(numero_de_nos: int, n_nos_y: int, n_nos_x: int,
                        L_y: float, L_x: float, dy: float, dx: float):
    '''
    ----------------------------------------------------------------------------
    Gera as coordenadas da malha
    ----------------------------------------------------------------------------
    @param numero_de_nos - Numero de nos da malha
    @param n_nos_y       - Numero de nos na direcao y
    @param n_nos_x       - Numero de nos da direcao x
    @param L_y           - Dimenção na direcao y
    @param L_x           - Dimenção na direcao x
    @param dy            - Discretizacao na direcao y
    @param dx            - Discretizacao na direcao x
    ----------------------------------------------------------------------------
    @return Retorna as coordendas da malha na forma:
       |x1,y1|
       |x2,y2|
       ...
       |xn,yn|
    ----------------------------------------------------------------------------
    '''

    # gerando as coordendas
    x = np.ndarray((numero_de_nos, 2), dtype=float)

    linha_x = np.ndarray(n_nos_x, dtype=float)  # x
    linha_y = np.ndarray(n_nos_y, dtype=float)  # y

    # divisao da linha horizontal
    linha_x[0] = 0.0
    linha_x[-1] = L_x
    for i in range(1, n_nos_x):
        linha_x[i] = linha_x[i - 1] + dx

    # divisao da linha vertical
    linha_y[0] = 0.0
    linha_y[-1] = L_y
    for i in range(1, n_nos_y):
        linha_y[i] = linha_y[i - 1] + dy

    # gerando a coordenadas
    for i in range(0, n_nos_y):
        y0 = linha_y[i]
        for j in range(0, n_nos_x):
            ipos = i * (n_nos_x) + j
            x[ipos][0] = linha_x[j]
            x[ipos][1] = y0
    return x


# ******************************************************************************

# ******************************************************************************
def gera_as_conectividade(numero_de_el: int, n_div_y: int, n_div_x: int):
    '''
    ----------------------------------------------------------------------------
    Gera as conectividade nodais do elementos
    ----------------------------------------------------------------------------
    @param numero_de_el - Numero de elementos
    @param n_div_y      - numero de divisoes na direcao y
    @param n_div_x      - numero de divisoes na direcao x
    ----------------------------------------------------------------------------
    @return Retorna as coordendas da malha na forma:
       |x1,y1|
       |x2,y2|
       ...
       |xn,yn|
    ----------------------------------------------------------------------------
    '''
    el = np.ndarray((numero_de_el, 4), dtype=int)

    id = 0
    n_nos_x = n_div_x + 1
    for linha in range(0, n_div_y):
        for coluna in range(0, n_div_x):
            no1 = linha * (n_nos_x) + coluna
            no2 = no1 + 1
            no3 = no2 + n_nos_x
            no4 = no3 - 1
            el[id][0] = no1
            el[id][1] = no2
            el[id][2] = no3
            el[id][3] = no4
            id += 1

    return el


# ******************************************************************************

# ******************************************************************************
def obtem_os_nos_do_contorno(n_nos_y: int, n_nos_x: int):
    '''
    ----------------------------------------------------------------------------
    Obtem os nos do contorno
    ----------------------------------------------------------------------------
    @param n_nos_y       - numero de nos na direcao y
    @param n_nos_x       - numero de nos da direcao x
    ----------------------------------------------------------------------------
    @return Retorna um tupla (a, b, c, d):
       a - Lista de nos da linha de baixo
       b - Lista de nos da linha de cima
       c - Lista de nos da linha da esquerda
       d - Lista de nos da linha da direita
    ----------------------------------------------------------------------------
    '''

    # linha de baixo
    nos_de_baixo = np.ndarray(n_nos_x, dtype=int)
    for i in range(0, n_nos_x):
        nos_de_baixo[i] = i

    # linha de cima
    nos_de_cima = np.ndarray(n_nos_x, dtype=int)
    for i in range(0, n_nos_x):
        nos_de_cima[i] = i + (n_nos_y - 1) * n_nos_x

        # linha da esquerda
    nos_de_esquerda = np.ndarray(n_nos_y, dtype=int)
    for i in range(0, n_nos_y):
        nos_de_esquerda[i] = i * n_nos_x

    # linha da direita
    nos_de_direita = np.ndarray(n_nos_y, dtype=int)
    for i in range(0, n_nos_y):
        nos_de_direita[i] = i * n_nos_x + n_nos_x - 1

    return nos_de_baixo, nos_de_cima, nos_de_esquerda, nos_de_direita


# ******************************************************************************

# ******************************************************************************
def escreve_arquivo_txt(prefixo: str, numero_de_nos: int, numero_de_el: int, x,
                        el):
    '''
    ----------------------------------------------------------------------------
    Escreve a malha no formato .txt
    ----------------------------------------------------------------------------
    @param numero_de_nos   - Numero de nos da malha
    @param numero_de_el    - Numero de elementos
    @param x               - Coordenadas do nos
    @param el              - Connectividade nodal
    @param nos_de_baixo    - Lista de nos da linha de baixo
    ----------------------------------------------------------------------------
    '''
    with open(prefixo + '.txt', 'w') as file:
        file.writelines(f'nnode {numero_de_nos} nel {numero_de_el}\n')

        file.writelines('Coordenadas\n')
        for no, (xi, yi) in enumerate(x, start=1):
            file.writelines(f'{no:4} {xi:.6f} {yi:.6f}\n')

        file.writelines('Elementos\n')
        for eli, (no1, no2, no3, no4) in enumerate(el, start=1):
            file.writelines(f'{eli:4} {no1:4} {no2:4} {no3:4} {no4:4}\n')
        # ******************************************************************************


# ******************************************************************************
def escreve_arquivo_vtk(prefixo: str, numero_de_nos: int, numero_de_el: int,
                        x, el, nos_de_baixo, nos_de_cima,
                        nos_da_esquerda, nos_da_direita):
    '''
    ----------------------------------------------------------------------------
    Escreve a malha no formato .txt
    ----------------------------------------------------------------------------
    @param numero_de_nos   - Numero de nos da malha
    @param numero_de_el    - Numero de elementos
    @param x               - Coordenadas do nos
    @param el              - Connectividade nodal
    @param nos_de_baixo    - Lista de nos da linha de baixo
    @param nos_de_cima     - Lista de nos da linha de cima
    @param nos_da_esquerda - Lista de nos da linha da esquerda
    @param nos_da_direita  - Lista de nos da linha da direita
    ----------------------------------------------------------------------------
    '''
    with open(prefixo + '.vtk', 'w') as file:
        file.writelines('# vtk DataFile Version 3.0\n')
        file.writelines('teste\n')
        file.writelines('ASCII\n')
        file.writelines('DATASET UNSTRUCTURED_GRID\n')

        file.writelines(f'POINTS  {numero_de_nos}  double\n')
        for xi, yi in x:
            file.writelines(f'{xi:.6f} {yi:.6f} 0.0\n')

        file.writelines(f'CELLS {numero_de_el} {5 * numero_de_el}\n')
        for no1, no2, no3, no4 in el:
            file.writelines(f'4 {no1:4} {no2:4} {no3:4} {no4:4}\n')

        file.writelines(f'CELL_TYPES {numero_de_el}\n')
        for _ in range(numero_de_el):
            file.writelines('9\n')

        file.writelines(f'POINT_DATA {numero_de_nos}\n')

        file.writelines('SCALARS linha_de_baixo int 1\n')
        file.writelines('LOOKUP_TABLE my_table\n')
        for no in range(numero_de_nos):
            if no in nos_de_baixo:
                file.writelines('1\n')
            else:
                file.writelines('0\n')

        file.writelines('SCALARS linha_de_cima int 1\n')
        file.writelines('LOOKUP_TABLE my_table\n')
        for no in range(numero_de_nos):
            if no in nos_de_cima:
                file.writelines('1\n')
            else:
                file.writelines('0\n')

        file.writelines('SCALARS linha_da_esquerda int 1\n')
        file.writelines('LOOKUP_TABLE my_table\n')
        for no in range(numero_de_nos):
            if no in nos_da_esquerda:
                file.writelines('1\n')
            else:
                file.writelines('0\n')

        file.writelines('SCALARS linha_da_direita int 1\n')
        file.writelines('LOOKUP_TABLE my_table\n')
        for no in range(numero_de_nos):
            if no in nos_da_direita:
                file.writelines('1\n')
            else:
                file.writelines('0\n')
