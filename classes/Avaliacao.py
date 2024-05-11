# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:22:42 2024

@author: Tomás
"""

class Avaliação:
    def __init__(self, cliente: str, dataHora: str, pontuacao: int, comentario: str):
        self.cliente = cliente
        self.dataHora = dataHora
        self.pontuacao = pontuacao
        self.comentario = comentario

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getDataHora(self):
        return self.dataHora

    def setDataHora(self, dataHora):
        self.dataHora = dataHora

    def getPontuacao(self):
        return self.pontuacao

    def setPontuacao(self, pontuacao):
        self.pontuacao = pontuacao

    def getComentario(self):
        return self.comentario

    def setComentario(self, comentario):
        self.comentario = comentario