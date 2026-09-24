import unittest
from tropas import Tropa, Soldado, Tanque, Buque, Escudo

class TestMecanicasGenerales(unittest.TestCase):

    def test_tropa_clase_abstracta_no_instanciable(self):
        # Verifica que la clase base Tropa no pueda ser instanciada directamente
        with self.assertRaises(TypeError):
            Tropa(10)

    def test_tropa_inicia_sin_escudo(self):
        soldado = Soldado()
        self.assertIsNone(soldado.escudo)

    def test_equipar_y_reemplazar_escudo(self):
        tanque = Tanque()
        escudo_basico = Escudo(0.1)
        escudo_avanzado = Escudo(0.5)

        tanque.equipar_escudo(escudo_basico)
        self.assertEqual(tanque.escudo.porcentaje, 0.1)

        # Reemplazamos el escudo por uno mejor
        tanque.equipar_escudo(escudo_avanzado)
        self.assertEqual(tanque.escudo.porcentaje, 0.5)

    def test_escudo_bloqueo_total(self):
        soldado = Soldado()
        escudo_total = Escudo(1.0)  # 100% de protección
        soldado.equipar_escudo(escudo_total)

        # Recibe un disparo de 1 de daño pero el escudo bloquea el 100%
        soldado.recibir_disparo(1)
        self.assertEqual(soldado.vida, 1)
        self.assertTrue(soldado.esta_vivo())


class TestSoldadoCombate(unittest.TestCase):

    def test_soldado_vida_inicial(self):
        soldado = Soldado()
        self.assertEqual(soldado.vida, 1)

    def test_soldado_con_escudo_parcial_sobrevive_disparo(self):
        soldado = Soldado()
        escudo = Escudo(0.5)  # 50% de mitigación
        soldado.equipar_escudo(escudo)

        soldado_enemigo = Soldado()
        soldado_enemigo.disparar(soldado)

        # Daño recibido: 1 - (1 * 0.5) = 0.5. Vida restante: 1 - 0.5 = 0.5
        self.assertAlmostEqual(soldado.vida, 0.5)
        self.assertTrue(soldado.esta_vivo())

    def test_fuego_concentrado_dos_soldados_destruyen_tanque(self):
        soldado1 = Soldado()
        soldado2 = Soldado()
        tanque = Tanque()

        # Cada soldado inflige 1 de daño; tanque tiene 2 de vida
        soldado1.disparar(tanque)
        self.assertTrue(tanque.esta_vivo())
        self.assertEqual(tanque.vida, 1)

        soldado2.disparar(tanque)
        self.assertFalse(tanque.esta_vivo())
        self.assertEqual(tanque.vida, 0)


class TestTanqueCombate(unittest.TestCase):

    def test_tanque_vida_inicial(self):
        tanque = Tanque()
        self.assertEqual(tanque.vida, 2)

    def test_tanque_destruido_de_un_disparo_por_buque(self):
        tanque = Tanque()
        buque = Buque()

        # El buque hace 3 de daño, suficiente para sobrepasar los 2 de vida del tanque
        buque.disparar(tanque)
        self.assertFalse(tanque.esta_vivo())
        self.assertEqual(tanque.vida, -1)

    def test_tanque_con_escudo_sobrevive_a_otro_tanque(self):
        tanque_defensor = Tanque()
        tanque_atacante = Tanque()
        escudo = Escudo(0.5)
        tanque_defensor.equipar_escudo(escudo)

        # Daño del atacante = 2. Con escudo del 50%, daño recibido = 1.
        tanque_atacante.disparar(tanque_defensor)
        self.assertTrue(tanque_defensor.esta_vivo())
        self.assertEqual(tanque_defensor.vida, 1)

    def test_tanque_con_escudo_alto_resiste_disparo_de_buque(self):
        tanque = Tanque()
        buque = Buque()
        escudo = Escudo(0.6)  # Bloquea 60% de 3 de daño = 1.8 mitigado, recibe 1.2
        tanque.equipar_escudo(escudo)

        buque.disparar(tanque)
        # Vida restante: 2 - 1.2 = 0.8
        self.assertTrue(tanque.esta_vivo())
        self.assertAlmostEqual(tanque.vida, 0.8)


class TestBuqueCombate(unittest.TestCase):

    def test_buque_vida_inicial(self):
        buque = Buque()
        self.assertEqual(buque.vida, 3)

    def test_buque_destruye_otro_buque_sin_escudo(self):
        buque_atacante = Buque()
        buque_defensor = Buque()

        # Daño 3 contra 3 de vida
        buque_atacante.disparar(buque_defensor)
        self.assertFalse(buque_defensor.esta_vivo())
        self.assertEqual(buque_defensor.vida, 0)

    def test_buque_resiste_ataque_combinado_soldado_y_tanque(self):
        buque = Buque()
        soldado = Soldado()
        tanque = Tanque()

        soldado.disparar(buque)  # Recibe 1 de daño -> vida = 2
        self.assertTrue(buque.esta_vivo())
        self.assertEqual(buque.vida, 2)

        tanque.disparar(buque)   # Recibe 2 de daño -> vida = 0
        self.assertFalse(buque.esta_vivo())
        self.assertEqual(buque.vida, 0)

    def test_buque_con_escudo_soporta_multiples_disparos_de_soldado(self):
        buque = Buque()
        escudo = Escudo(0.5)  # Cada disparo de 1 pasa a ser de 0.5
        buque.equipar_escudo(escudo)
        soldado = Soldado()

        # Disparamos 4 veces: 4 * 0.5 = 2 de daño recibido
        for _ in range(4):
            soldado.disparar(buque)

        self.assertTrue(buque.esta_vivo())
        self.assertAlmostEqual(buque.vida, 1.0)


if __name__ == '__main__':
    unittest.main()
