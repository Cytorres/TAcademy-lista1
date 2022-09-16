from src.appication.domain import Armazem

def saida_de_pedidos(valor_final: float) -> str:
    return f'Total do pedido: R${valor_final:.2f}'