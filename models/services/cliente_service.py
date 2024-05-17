from models.entities.cliente import Cliente

class ClienteService:
    def cadastrar_cliente(self, nome: str, email: str, telefone: str, endereco: str) -> dict:
        cliente = Cliente(nome, email, telefone, endereco)
        cliente_data = {
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone,
            "endereco": cliente.endereco,
            "pedido": {}
        }
        return cliente_data
