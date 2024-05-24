from classes.gclass import Gclass

class Fornecedor:
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1  
    nkey = 1
    
    att = ['_PedidosEspera', '_PedidosPreparo', '_totalVendas']
    
    header = 'Cozinha'
   
    des = ['nome', 'contato', 'produtos_fornecidos']

    def __init__(self, nome: str, contato: str):
        self.nome = nome
        self.contato = contato
        self.produtos_fornecidos = []

    def adicionar_produto_fornecido(self, produto): 
        self.produtos_fornecidos.append(produto)
        print(f"Produto {produto} adicionado ao fornecedor {self.nome}.")

    def remover_produto_fornecido(self, produto):
        if produto in self.produtos_fornecidos:
            self.produtos_fornecidos.remove(produto)
            print(f"Produto {produto} removido do fornecedor {self.nome}.")
        else:
            print(f"Produto {produto} não encontrado na lista de produtos fornecidos por {self.nome}.")

    def listar_produtos_fornecidos(self):
        return self.produtos_fornecidos

    def __str__(self):
        return f"Fornecedor(Nome: {self.nome}, Contato: {self.contato}, Produtos Fornecidos: {self.produtos_fornecidos})"

    def __repr__(self):
        return self.__str__()

