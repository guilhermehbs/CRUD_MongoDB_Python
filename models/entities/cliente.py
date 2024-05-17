from bson import ObjectId

class Cliente:

    next_id = 1

    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.id = ObjectId()

    def __str__(self):
        return (f"Cliente(ID={self.id}, "
                f"Nome={self.nome}, "
                f"Email={self.email}, "
                f"Telefone={self.telefone})")

