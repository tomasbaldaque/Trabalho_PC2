# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:21:54 2024

@author: Tomás
"""

from classes.gclass import Gclass

class Reserva(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1  
    nkey = 1
    
    att = ['_cliente', '_dataHora', '_status']
    
    header = 'reserva'
   
    des = ['cliente', 'dataHora', 'status']
    
    def __init__(self, Cliente, dataHora: str, status: str):
        super()._init_()
        self._Cliente = Cliente
        self._dataHora = dataHora
        self._status = status
        
        Reserva.obj[str(Cliente)] = self
        Reserva.lst.append(str(Cliente))
      
    @property 
    def getCliente(self):
        return self.Cliente 
    @property
    def getDataHora(self):
        return self.dataHora
    @property
    def getStatus(self):
        return self.status
    @property
    def setStatus(self, status):
        self.status = status
