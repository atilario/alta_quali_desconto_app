from src.models.desconto import DescontoVIP
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVIP())
    valor_final = pedido.valor_final(100.0)
    pedido_service = PedidoService()
    pedido_service.adicionar_pedido(pedido)
    pedido_service.processar_pedidos()
