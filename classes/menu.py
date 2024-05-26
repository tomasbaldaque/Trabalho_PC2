from classes.gclass import Gclass
import pandas as pd

class Menu(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    

    att = ['_code','_nome','_descricao','_preco', '_imagem']

    header = 'Menu'

    des = ['Code','Nome','Descricao','Preco', 'Imagem']
    

    def __init__(self, code, nome, descricao, preco, imagem):
        super().__init__()
        self._code = code
        self._nome = nome
        self._descricao = descricao
        self._preco = preco
        self._imagem = imagem

        Menu.obj[code] = self
        Menu.lst.append(code)
    
    @property 
    def code(self):
        return self._code
    
    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao
    
    @property 
    def preco(self):
        return self._preco
    
    @property 
    def imagem(self):
        return self._imagem
    
    @code.setter 
    def code(self, code):
        self._code = code

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        
    @imagem.setter 
    def imagem(self, imagem):
        self._imagem = imagem
        
    @classmethod 
    def find(cls, nome):
        for menu in Menu.obj.values():
            if menu.nome.lower() == nome.lower():
                return menu
        return None

        
    def to_dict(self):
        return {
            'Code': self._code,
            'Nome': self._nome,
            'Descricao': self._descricao,
            'Preco': self._preco,
            'Imagem': self._imagem
        }

from manage_db import df2SQL
if __name__ == "__main__":     
    menu_items = [
     Menu('001', 'Bruschetta', 'Pão torrado com tomate, azeite e alho', 7.0, '/static/imagens/bruschetta.jpg'),
     Menu('002', 'Salada Caprese', 'Mozzarella fresca, tomates e manjericão', 8.5, '/static/imagens/saladacaprese.jpg'),
     Menu('003', 'Arancini', 'Bolas de arroz fritas com recheio de queijo e carne', 9.0, '/static/imagens/arancini.jpg'),
     Menu('004', 'Calamari Fritti', 'Lula frita com molho marinara', 10.0, '/static/imagens/calamarifritti.jpg'),
     Menu('005', 'Pizza Margherita', 'Clássica Pizza Margherita', 10.5, '/static/imagens/pizzamargherita.jpg'),
     Menu('006', 'Pizza Quattro Stagioni', 'Pizza com quatro secções, cada uma com diferentes ingredientes', 13.0, '/static/imagens/pizzaquatroestacoes.jpg'),
     Menu('007', 'Lasagna', 'Massa com camadas de carne, queijo e molho de tomate', 12.5, '/static/imagens/lasanha.jpg'),
     Menu('008', 'Esparguete Carbonara', 'Massa com molho cremoso e bacon', 12.0, '/static/imagens/esparguetecarbonara.jpg'),
     Menu('009', 'Penne Arrabbiata', 'Massa Penne com molho de tomate picante', 11.0, '/static/imagens/pennearrabbiata.jpg'),
     Menu('010', 'Risotto alla Milanese', 'Risotto cremoso com açafrão e queijo Parmesão', 14.0, '/static/imagens/risottoallamilanese.jpg'),
     Menu('011', 'Fettuccine Alfredo', 'Massa com natas e molho Parmesão', 12.5, '/static/imagens/fettuccinealfredo.jpg'),
     Menu('012', 'Frango Parmigiano', 'Frango empanado com marinara e mozzarella', 15.0, '/static/imagens/frangoparmigiano.jpg'),
     Menu('013', 'Bistecca alla Fiorentina', 'Bisteca grelhada ao estilo Florentino', 25.0, '/static/imagens/bisteccaallafiorentina.jpg'),
     Menu('014', 'Vitela Marsala', 'Vitela cozinhada com vinho Marsala e cogumelos', 18.0, '/static/imagens/vitelamarsala.jpg'),
     Menu('015', 'Seafood Linguine', 'Massa Linguine com mistura de marisco em molho de tomate', 17.0, '/static/imagens/seafoodlinguine.jpg'),
     Menu('016', 'Tiramisu', 'Sobremesa Italiana tradicional com mascarpone e café', 6.5, '/static/imagens/tiramisu.jpg'),
     Menu('017', 'Cannoli', 'Conchas doces recheadas com queijo ricotta doce', 5.5, '/static/imagens/cannoli.jpg'),
     Menu('018', 'Panna Cotta', 'Pudim de baunilha cremosa com doce de frutos silvestres', 6.0, '/static/imagens/pannacota.jpg'),
     Menu('019', 'Gelato', 'Gelado ao estilo italiano, vários sabores', 4.5, '/static/imagens/gelato.jpg'),
     Menu('020', 'Affogato', 'Gelado de baunilha com uma ponta de café expresso', 5.0, '/static/imagens/affogato.jpg'),
     Menu('021', 'Sorvete de Limão', 'Sorvete de limão refrescante', 4.0, '/static/imagens/sorvetedelimao.jpg'),
     Menu('022', 'Fondant de chocolate', 'Bolo de chocolate, quente', 7.0, '/static/imagens/fondantdechocolate.jpg')
    ]
 
    menu_data = [item.to_dict() for item in menu_items]
    df = pd.DataFrame(menu_data)
 
    database_file = '../data/restaurante.db'
    table_name = 'Menu'
    df2SQL(df, database_file, table_name)
    Menu.first()
    
    print(Menu.first())