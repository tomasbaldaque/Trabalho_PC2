from classes.gclass import Gclass

class Pedido(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_code', '_cliente']
    
    header = 'Pedido'
    
    des = ['Code', 'Cliente']

    def __init__(self, code, cliente):
        super().__init__()
        self._code = Pedido.auto_number
        Pedido.auto_number += 1
        self._cliente = cliente
        self._itens = []

        Pedido.obj[self._code] = self
        Pedido.lst.append(self._code)
    
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    def adicionar_item(self, item):    # método para adicionar item do menu ao pedido
        self._itens.append(item)
    
    def remover_item(self, item):       #método para remover um item do pedido  caso o cliente mude de ideias(exemplo)
        if item in self._itens:
            self._itens.remove(item)
        else:
            print("Item não encontrado no pedido.")
    
    def calcular_total(self):          #método para calcular o total de itens do pedido 
        return sum(item.get_preco() for item in self._itens)
    
    def __str__(self):       #método mágico
        return f"Pedido(Code: {self._code}, Cliente: {self._cliente}, DataHora: {self._data_hora}, Status: {self._status}, Total: {self.calcular_total()})"
    
    def __repr__(self):
        return self.__str__()

    @classmethod                       #método da classe para formar uma lista cm os itens e levar a lista do pedido para a cozinha
    def listar_pedidos(cls):
        return [cls.obj[key] for key in cls.lst]

# Exemplo de uma classe Item para usar com Pedido
class Item:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def get_nome(self):
        return self._nome
    
    def get_preco(self):
        return self._preco
    
    def __str__(self):
        return f"Item(Nome: {self._nome}, Preço: {self._preco})"
    
    def __repr__(self):
        return self.__str__()


