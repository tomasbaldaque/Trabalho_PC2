#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:25:17 2024

@author: miguelanjo
"""

from classes.gclass import Gclass
from classes.Pedido import Pedido

class Cozinha(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1  
    nkey = 1
    
    att = ['_PedidosEspera', '_PedidosPreparo', '_totalVendas']
    
    header = 'Cozinha'
   
    des = ['PedidoEspera', 'PedidoPreparo', 'totalVendas']

    def __init__(self):
        super().__init__()
        self.PedidosEspera = []
        self.PedidosPreparo = []
        self.totalVendas = 0

    def adicionarPedidoEspera(self, pedido):
        self.PedidosEspera.append(pedido)
        print(f"Pedido adicionado à espera: {pedido.get_cliente()} - {pedido.get_data_hora()}")

    def moverPedidoParaPreparo(self, pedido):
        if pedido in self.PedidosEspera:
            self.PedidosEspera.remove(pedido)
            self.PedidosPreparo.append(pedido)
            pedido.set_status('Em Preparo')
            print(f"Pedido movido para preparo: {pedido.get_cliente()} - {pedido.get_data_hora()}")
        else:
            print(f"Pedido não encontrado na lista de espera: {pedido.get_cliente()} - {pedido.get_data_hora()}")

    def marcarPedidoConcluido(self, pedido):
        if pedido in self.PedidosPreparo:
            self.PedidosPreparo.remove(pedido)
            pedido.set_status('Concluído')
            self.totalVendas += 1
            print(f"Pedido concluído: {pedido.get_cliente()} - {pedido.get_data_hora()}. Total de vendas: {self.totalVendas}")
        else:
            print(f"Pedido não encontrado na lista de preparo: {pedido.get_cliente()} - {pedido.get_data_hora()}")
