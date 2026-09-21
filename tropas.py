from abc import ABC, abstractmethod

class Tropa(ABC):
    def __init__(self, vida):
            self.vida = vida
    
    def esta_vivo(self):
            return self.vida != 0
    
    def recibir_disparo(self):
            self.vida -= 1

    def disparar(self, objetivo):
           objetivo.recibir_disparo()

class Soldado(Tropa):
       def __init__(self):
              super().__init__(1)

class Tanque(Tropa):
       def __init__(self):
              super().__init__(2)

class Buque(Tropa):
       def __init__(self):
              super().__init__(3)