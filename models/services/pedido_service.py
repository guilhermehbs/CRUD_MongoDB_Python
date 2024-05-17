import string
import datetime
from models.entities.pedido import Pedido

class PedidoService:
    def criar_pedido(self, itens: list, observacoes: string) -> dict:
        data = datetime.datetime.now()
        data_string = data.strftime('%Y-%m-%d')
        pedido = Pedido(data_string, itens, observacoes)

        pedido_data = {"data_hora": pedido.data, "itens": pedido.itens,
                        "status": "recebido", "observacoes": observacoes,
                       "valor_total": self.__calcular_valor_total(itens)}

        return pedido_data

    def __calcular_valor_total(self, itens: dict) -> int:
        valor_total = 0

        for valor in itens.values():
            valor_total += valor

        return valor_total
