import unittest
from tropas import Soldado, Tanque, Buque

class TestSoldado(unittest.TestCase):

    def test_soldado_inicia_vivo(self):
        soldado = Soldado()
        self.assertTrue(soldado.esta_vivo())

    def test_soldado_muere_al_recibir_disparo(self):
        soldado = Soldado()
        soldado.recibir_disparo()
        self.assertFalse(soldado.esta_vivo())

    def test_soldado_dispara_a_tanque(self):
        soldado = Soldado()
        tanque = Tanque()
        soldado.disparar(tanque)
        self.assertTrue(tanque.esta_vivo())

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

    def test_tanque_mata_a_tanque(self):
        tanque1 = Tanque()
        tanque2 = Tanque()
        tanque1.disparar(tanque2)
        self.assertFalse(tanque2.esta_vivo())

class TestBuque(unittest.TestCase):

    def test_buque_inicia_vivo(self):
        buque = Buque()
        self.assertTrue(buque.esta_vivo())

    def test_buque_sobrevive_dos_disparos(self):
        buque = Buque()
        buque.recibir_disparo()
        buque.recibir_disparo()
        self.assertTrue(buque.esta_vivo())

    def test_buque_sobrevive_daño_letal(self):
        buque = Buque()
        for i in range(3):
            buque.recibir_disparo()
        self.assertFalse(buque.esta_vivo())



if __name__ == '__main__':
    unittest.main()