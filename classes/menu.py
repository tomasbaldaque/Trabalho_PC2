# -*- coding: utf-8 -*-

from classes.gclass import Gclass

class Menu(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    

    att = ['_nome','_descricao','_preco']

    header = 'Menu'

    des = ['Nome','Descricao','Preco']
    

    def __init__(self, nome, descricao, preco):
        super().__init__()
        self._nome = nome
        self._descricao = descricao
        self._preco = preco


        Menu.obj[nome] = self
        Menu.lst.append(nome)

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao
    
    @property 
    def preco(self):
        return self._preco

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

 
if __name__ == "__main__":    
    Menu.read('data/restaurante.db')