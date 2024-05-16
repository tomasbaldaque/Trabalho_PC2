#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:25:17 2024

@author: miguelanjo
"""

class Gclass:
    def __init__(self):
        pass

class Cozinha(Gclass):
    def __init__(self):
        super().__init__()
        self.PedidosEspera: List[Pedido] = []
        self.PedidosPreparo: List[Pedido] = []
        self.totalVendas: int = 0

    def adicionarPedidoEspera(self, pedido: Pedido):
        self.PedidosEspera.append(pedido)
        print(f"Pedido adicionado à espera: {pedido.get_cliente()} - {pedido.get_data_hora()}")

    def moverPedidoParaPreparo(self, pedido: Pedido):
        if pedido in self.PedidosEspera:
            self.PedidosEspera.remove(pedido)
            self.PedidosPreparo.append(pedido)
            pedido.set_status('Em Preparo')
            print(f"Pedido movido para preparo: {pedido.get_cliente()} - {pedido.get_data_hora()}")
        else:
            print(f"Pedido não encontrado na lista de espera: {pedido.get_cliente()} - {pedido.get_data_hora()}")

    def marcarPedidoConcluido(self, pedido: Pedido):
        if pedido in self.PedidosPreparo:
            self.PedidosPreparo.remove(pedido)
            pedido.set_status('Concluído')
            self.totalVendas += 1
            print(f"Pedido concluído: {pedido.get_cliente()} - {pedido.get_data_hora()}. Total de vendas: {self.totalVendas}")
        else:
            print(f"Pedido não encontrado na lista de preparo: {pedido.get_cliente()} - {pedido.get_data_hora()}")