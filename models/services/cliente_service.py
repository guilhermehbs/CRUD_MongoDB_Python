import string
from models.entities.cliente import Cliente

class ClienteService:
    def cadastrar_cliente(self, nome: string, email: string, telefone: string, endereco: string) -> dict:
        cliente = Cliente(nome, email, telefone, endereco)
        cliente_data = {
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone,
            "endereco": cliente.endereco,
            "pedido": {}
        }
        return cliente_data
