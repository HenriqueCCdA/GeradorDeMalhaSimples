from malha.gerador_malha import numero_nos, dy_dx_elemento, \
    gerando_coordenadas, \
    numero_de_elementos, gera_as_conectividade, \
    obtem_os_nos_do_contorno, escreve_arquivo_vtk, escreve_arquivo_txt


def gera_malha(prefixo: str, L_y: float, L_x: float, n_el_y: int, n_el_x: int):
    '''
    ---------------------------------------------------------------------------
    Gera a malha
    ---------------------------------------------------------------------------
    :param prefixo: Prefixo do nome do arquivo de saida
    :param L_y: Dimensão do retangulo na direcao y
    :param L_x: Dimensao do retangulo na direcao x
    :param n_el_y: Número de divisões na direção y
    :param n_el_x: Número de divisões na direção x
    ---------------------------------------------------------------------------
    :return:
    ---------------------------------------------------------------------------
    '''
    # Divisoes de nos
    n_nos_y, n_nos_x, nnodes = numero_nos(n_el_y, n_el_x)

    #  Espaçamento da malha
    dy, dx = dy_dx_elemento(n_el_y, n_el_x, L_y, L_x)

    # Numero de elementos
    nel = numero_de_elementos(n_el_y, n_el_x)

    # Gerando as coordenadas
    x = gerando_coordenadas(nnodes, n_nos_y, n_nos_x,
                            L_y, L_x, dy, dx)

    # Gerando as connetividades
    el = gera_as_conectividade(nel, n_el_y, n_el_x)

    # nos do contorno
    linha_de_baixo, linha_de_cima, linha_da_esquerda, linha_da_direita = \
        obtem_os_nos_do_contorno(n_nos_y, n_nos_x)

    # Escreve o arquivo no formato .dat
    escreve_arquivo_txt(prefixo, nnodes, nel, x, el)

    # Escreve o arquivo de vtk
    escreve_arquivo_vtk(prefixo, nnodes, nel, x, el,
                        linha_de_baixo, linha_de_cima, linha_da_esquerda,
                        linha_da_direita)


if __name__ == '__main__':
    gera_malha('malha', L_y=1.0, L_x=1.0, n_el_y=10, n_el_x=10)
