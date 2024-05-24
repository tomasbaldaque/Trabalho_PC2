from classes.gclass import Gclass

class Sala(Gclass):
    def __init__(self, numero: int, capacidade: int, tipo: str):
        super().__init__()
        self.__numero = numero
        self.__capacidade = capacidade
        self.__tipo = tipo

    def getNumero(self) -> int:
        return self.__numero

    def setNumero(self, numero: int):
        self.__numero = numero

    def getCapacidade(self) -> int:
        return self.__capacidade

    def setCapacidade(self, capacidade: int):
        self.__capacidade = capacidade

    def getTipo(self) -> str:
        return self.__tipo

    def setTipo(self, tipo: str):
        self.__tipo = tipo

# Exemplo de uso:
if __name__ == "__main__":
    sala1 = Sala(101, 30, "Conferência")
    print(f"Sala número: {sala1.getNumero()}")
    print(f"Capacidade: {sala1.getCapacidade()}")
    print(f"Tipo: {sala1.getTipo()}")

    sala1.setNumero(102)
    sala1.setCapacidade(40)
    sala1.setTipo("Reunião")

    print("Atualizando informações da sala...")

    print(f"Sala número: {sala1.getNumero()}")
    print(f"Capacidade: {sala1.getCapacidade()}")
    print(f"Tipo: {sala1.getTipo()}")