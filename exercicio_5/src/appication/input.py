def cardapio():
    cardapio = {'100':('Cachorro quente', 1.20), 
    '101':('Bauru Simples', 1.30), 
    '102':('Bauru com ovo', 1.50), 
    '103':('Hamburguer', 1.20), 
    '104':('Cheesburguer', 1.20), 
    '105':('Refrigerante', 1.00)}

    return cardapio

def entrada_do_pedido():
    codigo_do_pedido = input('Código do pedido: ')
    quantidade = int(input('Quantidade: '))

    return codigo_do_pedido, quantidade
