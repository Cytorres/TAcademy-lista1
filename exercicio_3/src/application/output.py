def mostra_orcamento(quantidade_latas,valor_total_lata,quantidade_galao,valor_total_galao,quantidade_latas_em_litros,preco_lata_alternativa3,quantidade_galão_litro,preco_galao_alternativa3):
    print(f'Opção 1 - Lata (s)')
    print(f'Quantidade de lata(s) de tinta = {quantidade_latas}. \n Preço total = {valor_total_lata}.')
    print(f'Opção 2 - Galão(ões)')
    print(f'Quantidade de galões de tinta = {quantidade_galao}.  \n Preço total = {valor_total_galao} ')
    print(f'Opção 3 - Lata(s) e Galão(ões)')
    print(f'Quantidade de lata {quantidade_latas_em_litros}, preço {preco_lata_alternativa3}')
    print(f'Quantidade de galão {quantidade_galão_litro} preço {preco_galao_alternativa3}')
    print(f'Valor total {preco_lata_alternativa3 + preco_galao_alternativa3}.')