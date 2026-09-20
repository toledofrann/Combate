import unittest
from tropas import Soldado

class TestSoldado(unittest.TestCase):

    def test_soldado_inicia_vivo(self):
        soldado = Soldado()
        self.assertTrue(soldado.esta_vivo())

    def test_soldado_muere_al_recibir_disparo(self):
        soldado = Soldado()
        soldado.recibir_disparo()
        self.assertFalse(soldado.esta_vivo())


if __name__ == '__main__':
    unittest.main()