from classes.gclass import Gclass  #importar a Gclass

class Reserva(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0  
    nkey = 1
    
    att = ['_code', '_cliente', '_dataHora', '_status']
    
    header = 'reserva'
   
    des = ['code', 'cliente', 'dataHora', 'status']
    
    def __init__(self, code, cliente, dataHora: str, status: str):
        super().__init__()
        self._code = code
        self._cliente = cliente
        self._dataHora = dataHora
        self._status = status
        
        Reserva.obj[str(code)] = self
        Reserva.lst.append(str(code))
        
    @property 
    def code(self):
        return self._code
        
    @property 
    def cliente(self):
        return self._cliente 
    
    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente
        
    @property
    def DataHora(self):
        return self._dataHora
    
    @code.setter 
    def code(self, code):
        self._code = code
    
    @DataHora.setter 
    def DataHora(self, dataHora):
        self._dataHora = dataHora

    @property 
    def status(self):
        return self._status
    
    @status.setter 
    def status(self, status):
        self._status = status



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

            print(f"Reserva atualizada: Cliente: {cliente}, DataHora: {reserva.DataHora}, Status: {reserva.status}")
        else:
            print(f"Reserva para o cliente {cliente} não encontrada.")

    def exibir_reserva(cliente):      #método para mostrar em que estado está a reserva do cliente

        reserva = Reserva.obj.get(cliente)
        if reserva:
            print(f"Cliente: {cliente}, DataHora: {reserva.DataHora}, Status: {reserva.status}")
        else:
            print(f"Reserva para o cliente {cliente} não encontrada.")
    

