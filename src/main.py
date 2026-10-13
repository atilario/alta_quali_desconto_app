from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium

if __name__ == "__main__":
    # Configuração do repositório e serviço
    repo = PedidoRepository()

    # Criando um pedido com desconto
    pedido1 = Pedido(cliente="Leonardo", desconto=DescontoNormal())
    pedido1.valor_original = 100.0

    # Criando um pedido com desconto
    pedido2 = Pedido(cliente="Cardia", desconto=DescontoVIP())
    pedido2.valor_original = 100.0

    # Criando um pedido com desconto
    pedido3 = Pedido(cliente="Da Cruz", desconto=DescontoPremium())
    pedido3.valor_original = 100.0

    # Salvamento dos pedidos no repositório
    repo.adicionar_pedido(pedido1)
    repo.adicionar_pedido(pedido2)
    repo.adicionar_pedido(pedido3)

    # Adicionando o pedido ao serviço
    pedidos = repo.listar_pedidos()

    # Processando os pedidos
    for pedido in pedidos:
        print(f"cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
