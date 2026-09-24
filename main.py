from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

if __name__ == "__main__":

    service = PedidoService()

    """Criando pedidos e aplicando descontos"""

    pedido1 = Pedido("Alice", DescontoNormal())
    pedido1.valor_original = 100.0 #definindo valor original do pedido 1

    pedido2 = Pedido("Bob", DescontoVIP())
    pedido2.valor_original = 200.0 #definindo valor original do pedido 2

    pedido3 = Pedido("Eva", DescontoPremium())
    pedido3.valor_original = 300.0 #definindo valor original do pedido 3

    #Criando instâncias de pedidos e adicionando ao serviço para aplicação dos descontos

    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)


    service.processar_pedidos()