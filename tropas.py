from abc import ABC, abstractmethod

class Tropa(ABC):
    def __init__(self, vida):
            self.vida = vida
    
    def esta_vivo(self):
            return self.vida != 0
    
    def recibir_disparo(self, danio=1):
            self.vida -= danio

    @abstractmethod
    def disparar(self, objetivo):
           pass

class Soldado(Tropa):
       def __init__(self):
              super().__init__(1)

       def disparar(self, objetivo):
              objetivo.recibir_disparo(1)

class Tanque(Tropa):
       def __init__(self):
              super().__init__(2)
       def disparar(self, objetivo):
              objetivo.recibir_disparo(2)

class Buque(Tropa):
       def __init__(self):
              super().__init__(3)
       def disparar(self, objetivo):
              objetivo.recibir_disparo(3)