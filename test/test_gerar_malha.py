from unittest.case import TestCase
from malha.gerador_malha import numero_nos, dy_dx_elemento, gerando_coordenadas,\
                                numero_de_elementos, gera_as_conectividade, \
                                obtem_os_nos_do_contorno
from numpy.testing import assert_almost_equal, assert_array_equal
import numpy as np

X_ALVO = [[0.00, 0.00000000],
          [0.25, 0.00000000],
          [0.50, 0.00000000],
          [0.75, 0.00000000],
          [1.00, 0.00000000],
          [0.00, 0.33333333],
          [0.25, 0.33333333],
          [0.50, 0.33333333],
          [0.75, 0.33333333],
          [1.00, 0.33333333],
          [0.00, 0.66666667],
          [0.25, 0.66666667],
          [0.50, 0.66666667],
          [0.75, 0.66666667],
          [1.00, 0.66666667],
          [0.00, 1.00000000],
          [0.25, 1.00000000],
          [0.50, 1.00000000],
          [0.75, 1.00000000],
          [1.00, 1.00000000]]

EL_ALVO = [[ 0,  1,  6,  5],
           [ 1,  2,  7,  6],
           [ 2,  3,  8,  7],
           [ 3,  4,  9,  8],
           [ 5,  6, 11, 10],
           [ 6,  7, 12, 11],
           [ 7,  8, 13, 12],
           [ 8,  9, 14, 13],
           [10, 11, 16, 15],
           [11, 12, 17, 16],
           [12, 13, 18, 17],
           [13, 14, 19, 18]]

LINHA_DE_BAIXO = (0, 1, 2, 3, 4)
LINHA_DE_CIMA = (15, 16, 17, 18, 19)
LINHA_DA_ESQUERDA = (0, 5, 10, 15)
LINHA_DA_DIREITA = (4, 9, 14, 19)

class GeradorMalha(TestCase):

    def test_calculo_do_numero_de_elementos(self):
        nel = numero_de_elementos(3, 4)
        self.assertEqual(3 * 4, nel)

    def test_calculo_do_numero_de_nos(self):
        n_nos_x, n_nos_y, numero_de_nos = numero_nos(3, 4)
        self.assertEqual(4, n_nos_x)
        self.assertEqual(5, n_nos_y)
        self.assertEqual(20, numero_de_nos)

    def test_calculo_do_dy_e_dx_no_elemento(self):
        dy, dx = dy_dx_elemento(3, 8, 3.0, 4.0)
        assert_almost_equal(1.0, dy, decimal=14, err_msg = 'Erro no calculo de dy!')
        assert_almost_equal(0.5, dx, decimal=14, err_msg = 'Erro no calculo de dx!')

    def test_calculo_coordenadas_x(self):
        L_y, L_x = 1.0, 1.0
        n_el_y, n_el_x = 3, 4
        n_nos_y, n_nos_x, numero_de_nos = numero_nos(n_el_y, n_el_x)
        dy, dx = dy_dx_elemento(n_el_y, n_el_x, L_y, L_x)

        x = gerando_coordenadas(numero_de_nos, n_nos_y, n_nos_x,
                                L_y, L_x, dy, dx)

        x_alvo = np.array(X_ALVO)

        #absolute(a - b) <= (atol + rtol * absolute(b))
        resultado = np.allclose(x_alvo, x, rtol=1e-10, atol=1e-07)

        self.assertEqual(True, resultado, 'Coordenadas da malha!' )

    def test_calculo_conetividade(self):

        n_el_y, n_el_x = 3, 4
        nel = numero_de_elementos(3, 4)
        el = gera_as_conectividade(nel, n_el_y, n_el_x)

        el_alvo = np.array(EL_ALVO)

        assert_array_equal(el, el_alvo)


    def test_nos_de_contorno(self):

        '''
        a - Lista de nos da linha de baixo
        b - Lista de nos da linha de cima
        c - Lista de nos da linha da esquerda
        d - Lista de nos da linha da direita
        '''

        n_el_y, n_el_x = 3, 4
        n_nos_y, n_nos_x, _ = numero_nos(n_el_y, n_el_x)

        linha_de_baixo, linha_de_cima, linha_da_esquerda, linha_da_direita =\
            obtem_os_nos_do_contorno(n_nos_y, n_nos_x)

        assert_array_equal(linha_de_baixo   , LINHA_DE_BAIXO, 'Linha de baixo!')
        assert_array_equal(linha_de_cima    , LINHA_DE_CIMA, 'Linha de cima!')
        assert_array_equal(linha_da_esquerda, LINHA_DA_ESQUERDA, 'Linha da esquerda !')
        assert_array_equal(linha_da_direita , LINHA_DA_DIREITA, 'Linha da direita !')