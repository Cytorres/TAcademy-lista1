from dataclasses import dataclass
from typing import List

@dataclass
class Armazem:
    valor_total_pedido = []
    controle = 0  

def processamento_do_pedido(cardapio:dict,codigo_do_pedido:int,quantidade:int)->None: 
    # preco = float(cardapio[codigo_do_pedido][1])
    total = cardapio[codigo_do_pedido][1] * quantidade
    Armazem.valor_total_pedido.append(total)
    Armazem.controle += 1
    print(f'Você pediu {quantidade} {cardapio[codigo_do_pedido][0]}. Total = {total:.2f}')
        
def soma_pedido():        
   total_a_pagar = sum(Armazem.valor_total_pedido)
   return total_a_pagar
