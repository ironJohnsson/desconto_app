from src.controllers.pedido_controller import PedidoController
from src.repositories.pedido_repository import PedidoRepository
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService
from src.database.connection import DatabaseConnection

if __name__ == "__main__":
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    """Criando pedidos e aplicando descontos"""

    pedido1 = Pedido(cliente="Alice", desconto=DescontoNormal())
    pedido1.valor_original = 100.0 #definindo valor original do pedido 1

    pedido2 = Pedido(cliente="Bob", desconto=DescontoVIP())
    pedido2.valor_original = 200.0 #definindo valor original do pedido 2

    pedido3 = Pedido(cliente="Eva", desconto=DescontoPremium())
    pedido3.valor_original = 300.0 #definindo valor original do pedido 3

    #salvamento dos pedidos no repositório
    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()  #processando os pedidos e aplicando os descontos