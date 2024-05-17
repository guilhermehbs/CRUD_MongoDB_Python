import string
from bson import ObjectId

class Pedido:
    def __init__(self, data: string, itens: list, observacoes: string):
        self.id = ObjectId()
        self.data = data
        self. itens = itens
        self.observacoes = observacoes

    def __str__(self):
        return (f"Pedido(ID={self.id}, "
                f"Data={self.data}, "
                f"Cliente={self.cliente.nome}")