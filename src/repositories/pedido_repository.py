from src.models.pedido import Pedido

class PedidoRepository:
    """classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.pedidos
