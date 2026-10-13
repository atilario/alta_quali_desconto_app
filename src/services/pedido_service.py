from src.models.pedido import Pedido

class PedidoService:
    """classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self, repository):
        self.repository = repository

    def adicionar_pedido(self, pedido: Pedido):
        self.repository.adicionar_pedido(pedido)

    def processar_pedidos(self):
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")