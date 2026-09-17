class Soldado:
    def __init__(self, nombre:str, vida: int = 1):
        self.nombre = nombre
        self.vida = vida

    def disparar(self, objetivo: 'Soldado') -> bool:
        print(f" {self.nombre} dispara a {objetivo.nombre}")
        print(f"vida restante de {objetivo.nombre} = {objetivo.vida} ")
        objetivo.recibir_disparo(self.danio)

        return True

    def recibir_disparo(self, dano: int) -> int:
        self.vida = max(0, self.vida)
        return self.vida
    
    