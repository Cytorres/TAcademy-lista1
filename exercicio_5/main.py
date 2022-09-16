from src.appication.input import cardapio,entrada_do_pedido
from src.appication.domain import processamento_do_pedido,soma_pedido
from src.appication.output import saida_de_pedidos

if (__name__ == '__main__'):
    cardapio = cardapio()   
    while True:
        codigo_do_pedido, quantidade = entrada_do_pedido()
        processamento_do_pedido(cardapio,codigo_do_pedido,quantidade)
        continua = input('Você deseja fazer outro pedido? [S/N] ').upper().strip()
        
        if continua == 'S':
            continue
        else:
            print(saida_de_pedidos(soma_pedido()))
            break

    soma_pedido()
    

# Leonardo ajudou com este código colocando a classe, infelizmente eu não salvei o meu original.