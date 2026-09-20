class Soldado:
    def __init__(self, vida = 1):
        self.vida = vida

    def esta_vivo(self):
        return self.vida != 0

    def recibir_disparo(self):
        self.vida -= 1