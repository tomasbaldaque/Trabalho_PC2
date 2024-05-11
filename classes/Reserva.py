# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:21:54 2024

@author: Tomás
"""

class Reserva:
    def __init__(self, cliente: Cliente, dataHora: str, status: str):
        self.cliente = cliente
        self.dataHora = dataHora
        self.status = status

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getDataHora(self):
        return self.dataHora

    def setDataHora(self, dataHora):
        self.dataHora = dataHora

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status