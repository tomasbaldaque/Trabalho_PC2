from classes.pedido import Pedido
from classes.menu import Menu
from classes.gclass import Gclass 

class MenuPedido(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 2
    att = ['_codigo_pedido','_codigo_menu','_quantidade','_preco']
    header = 'Pedido'
    des = ['Codigo Pedido', 'Codigo Menu', 'Quantidade', 'Preco']
    
    def __init__(self, codigo_pedido, codigo_menu, quantidade, preco):
        super().__init__()
        if codigo_pedido in Pedido.lst:
            if codigo_menu in Menu.lst:
                self._codigo_pedido = codigo_pedido
                self._codigo_menu = codigo_menu 
                self._quantidade = int(quantidade)
                self._preco = float(preco)
                
                codigo = str(codigo_pedido) + str(codigo_menu)
                MenuPedido.obj[codigo] = self
                MenuPedido.lst.append(codigo)
            else:
                print('Prato', codigo_menu, 'não encontrado')
        else:
            print('Pedido', codigo_pedido,'não encontrado')
    
    @property 
    def codigo_pedido(self):
        return self._codigo_pedido 
    @property 
    def codigo_menu(self):
        return self._codigo_menu 
    @property 
    def quantidade(self):
        return self._quantidade 
    @quantidade.setter 
    def quantidade(self, quantidade):
        self._quantidade = float(quantidade)
    @property 
    def preco(self):
        return self._preco 
    @preco.setter 
    def preco(self, preco):
        self._preco = float(preco) 
    
                
     
