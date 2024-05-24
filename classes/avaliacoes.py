# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:22:42 2024

@author: Tomás
"""
from classes.gclass import Gclass

class Avaliacao(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1  
    nkey = 1
    
    att = ['_cliente', '_dataHora', '_pontuacao', '_comentario']
    
    header = 'Avaliação'
   
    des = ['cliente', 'dataHora', 'pontuacao', 'comentario']

    def __init__(self, cliente: str, dataHora: str, pontuacao: int, comentario: str):
        super().__init__()
        self._cliente = cliente
        self._dataHora = dataHora
        self._pontuacao = pontuacao
        self._comentario = comentario

        Avaliacao.obj[str(cliente)] = self
        Avaliacao.lst.append(str(cliente))

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def dataHora(self):
        return self._dataHora

    @dataHora.setter
    def dataHora(self, dataHora):
        self._dataHora = dataHora

    @property
    def pontuacao(self):
        return self._pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self._pontuacao = pontuacao

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, comentario):
        self._comentario = comentario

    from classes.avaliacao import Avaliacao
    
    def main():
        # Criar algumas avaliações
        avaliacao1 = Avaliacao("Cliente 1", "2023-05-23 10:30", 5, "Excelente serviço!")
        avaliacao2 = Avaliacao("Cliente 2", "2023-05-23 11:00", 4, "Muito bom, mas poderia melhorar.")
        
        # Acessar atributos das avaliações
        print(f"Avaliação de {avaliacao1.cliente}: {avaliacao1.pontuacao} estrelas - {avaliacao1.comentario}")
        print(f"Avaliação de {avaliacao2.cliente}: {avaliacao2.pontuacao} estrelas - {avaliacao2.comentario}")
    
        # Modificar uma avaliação
        avaliacao2.pontuacao = 5
        avaliacao2.comentario = "Revendo minha avaliação, está excelente!"
        print(f"Revisão de {avaliacao2.cliente}: {avaliacao2.pontuacao} estrelas - {avaliacao2.comentario}")
    
    if __name__ == "__main__":
        main()
