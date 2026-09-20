import unittest
from tropas import Soldado

class TestSoldado(unittest.TestCase):

    def test_soldado_inicia_vivo(self):
        soldado = Soldado()
        self.assertTrue(soldado.esta_vivo())


if __name__ == '__main__':
    unittest.main()