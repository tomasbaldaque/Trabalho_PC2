#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:01:29 2024

@author: antoniooandree
"""

class Gclass:
    def __init__(self):
        pass

class Pedido(Gclass):
    def __init__(self, cliente, data_hora, status):
        super().__init__()
        self.__cliente = cliente
        self.__itens = []  
        self.__data_hora = data_hora
        self.__status = status
   
    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_data_hora(self):
        return self.__data_hora

    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def adicionar_item(self, item):
        self.__itens.append(item)

    def remover_item(self, item):
        if item in self.__itens:
            self.__itens.remove(item)
        else:
            print("Item não encontrado no pedido.")

  
    def calcular_total(self):
        total = 0
        for item in self.__itens:
            total += item.get_preco()
        return total

