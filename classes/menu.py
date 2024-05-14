# -*- coding: utf-8 -*-

from classes.gclass import Gclass
import pandas as pd

class Menu(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    

    att = ['_code','_nome','_descricao','_preco']

    header = 'Menu'

    des = ['Code','Nome','Descricao','Preco']
    

    def __init__(self, code, nome, descricao, preco):
        super().__init__()
        self._code = code
        self._nome = nome
        self._descricao = descricao
        self._preco = preco


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
    
    @code.setter 
    def code(self, code):
        self._code = code

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        
    def to_dict(self):
        return {
            'Code': self._code,
            'Nome': self._nome,
            'Descricao': self._descricao,
            'Preco': self._preco
        }

from manage_db import df2SQL
if __name__ == "__main__":     
    menu_items = [
     Menu('001', 'Pizza Margherita', 'Classic Margherita Pizza', 10.5),
     Menu('002', 'Spaghetti Carbonara', 'Pasta with creamy sauce and bacon', 12.0),
     Menu('003', 'Tiramisu', 'Traditional Italian dessert', 6.5)
    ]
 
    menu_data = [item.to_dict() for item in menu_items]
    df = pd.DataFrame(menu_data)
 
    database_file = '../data/restaurante.db'
    table_name = 'Menu'
    df2SQL(df, database_file, table_name)
    Menu.first()