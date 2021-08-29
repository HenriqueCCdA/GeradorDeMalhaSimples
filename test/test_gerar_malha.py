from unittest.case import TestCase
from malha.gerador_malha import numero_nos, dy_dx_elemento, gerando_coordenadas
from numpy.testing import assert_almost_equal
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
          [1.00, 1.00000000]
          ]



class GeradorMalha(TestCase):

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
