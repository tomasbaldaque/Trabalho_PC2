# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:26:03 2024

@author: Tomás
"""

class Fornecedor:
    def __init__(self, nome: str, contato: str):
        self.nome = nome
        self.contato = contato
        self.produtosFornecidos = []

    def adicionarProdutoFornecido(self, produto):
        self.produtosFornecidos.append(produto)

    def removerProdutoFornecido(self, produto):
        self.produtosFornecidos.remove(produto)