import unittest
from tropas import Soldado, Tanque

class TestSoldado(unittest.TestCase):

    def test_soldado_inicia_vivo(self):
        soldado = Soldado()
        self.assertTrue(soldado.esta_vivo())

    def test_soldado_muere_al_recibir_disparo(self):
        soldado = Soldado()
        soldado.recibir_disparo()
        self.assertFalse(soldado.esta_vivo())

class TestTanque(unittest.TestCase):

    def test_tanque_inicia_vivo(self):
        tanque = Tanque()
        self.assertTrue(tanque.esta_vivo())

    def test_tanque_sobrevive_un_disparo(self):
        tanque = Tanque()
        tanque.recibir_disparo()
        self.assertTrue(tanque.esta_vivo())

    def test_tanque_muere_al_recibir_daño_fatal(self):
        tanque = Tanque()
        tanque.recibir_disparo()
        tanque.recibir_disparo()
        self.assertFalse(tanque.esta_vivo())

if __name__ == '__main__':
    unittest.main()