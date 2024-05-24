from classes.gclass import Gclass  #importar a Gclass

class Reserva(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1  
    nkey = 1
    
    att = ['_cliente', '_dataHora', '_status']
    
    header = 'reserva'
   
    des = ['cliente', 'dataHora', 'status']
    
    def __init__(self, Cliente, dataHora: str, status: str):
        super().__init__()
        self._Cliente = Cliente
        self._dataHora = dataHora
        self._status = status
        
        Reserva.obj[str(Cliente)] = self
        Reserva.lst.append(str(Cliente))
      
    @property 
    def Cliente(self):
        return self._Cliente 
    
    @Cliente.setter
    def Cliente(self, Cliente):
        self._Cliente = Cliente
        
    @property
    def DataHora(self):
        return self._dataHora
    
    @DataHora.setter 
    def DataHora(self, dataHora):
        self._dataHora = dataHora

    @property 
    def status(self):
        return self._status
    
    @status.setter 
    def status(self, status):
        self._status = status

<<<<<<< Updated upstream

    def listar_reservas():
        for cliente, reserva in Reserva.obj.items():
            print(f"Cliente: {cliente}, DataHora: {reserva.DataHora}, Status: {reserva.status}")
    
    
    def criar_reserva(cliente, dataHora, status):   #método para criar uma reserva 
        return Reserva(cliente, dataHora, status)
    
    
    def alterar_reserva(cliente, dataHora=None, status=None):  #método para alterar uma reserva
        reserva = Reserva.obj.get(cliente)
        if reserva:
            if dataHora:
                reserva.DataHora = dataHora  #hora da reserva
            if status:
                reserva.status = status  #estado da reserva
=======
    def listar_reservas():
        for cliente, reserva in Reserva.obj.items():
            print(f"Cliente: {cliente}, DataHora: {reserva.DataHora}, Status: {reserva.status}")


    def criar_reserva(cliente, dataHora, status):
        return Reserva(cliente, dataHora, status)


    def alterar_reserva(cliente, dataHora=None, status=None):
        reserva = Reserva.obj.get(cliente)
        if reserva:
            if dataHora:
                reserva.DataHora = dataHora
            if status:
                reserva.status = status
>>>>>>> Stashed changes
            print(f"Reserva atualizada: Cliente: {cliente}, DataHora: {reserva.DataHora}, Status: {reserva.status}")
        else:
            print(f"Reserva para o cliente {cliente} não encontrada.")
    
    
<<<<<<< Updated upstream
    def exibir_reserva(cliente):      #método para mostrar em que estado está a reserva do cliente
=======
    def exibir_reserva(cliente):
>>>>>>> Stashed changes
        reserva = Reserva.obj.get(cliente)
        if reserva:
            print(f"Cliente: {cliente}, DataHora: {reserva.DataHora}, Status: {reserva.status}")
        else:
            print(f"Reserva para o cliente {cliente} não encontrada.")
    
<<<<<<< Updated upstream
=======



>>>>>>> Stashed changes
