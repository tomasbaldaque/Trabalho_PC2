class Gclass:
    def __init__(self):
        pass

class Mesa(Gclass):
    def __init__(self, numero_mesa, capacidade, status):
        super().__init__()
        self.__numero_mesa = numero_mesa
        self.__capacidade = capacidade
        self.__status = status

    def get_numero_mesa(self):
        return self.__numero_mesa
  
    def set_numero_mesa(self, numero_mesa):
        self.__numero_mesa = numero_mesa
   
    def get_capacidade(self):
        return self.__capacidade
  
    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade
    
    def get_status(self):
        return self.__status
 
    def set_status(self, status):
        self.__status = status


