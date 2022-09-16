from typing import List

def mostra_resumo_notas_atleta(nome:str,notas_dos_jurados:List[float],maior_nota:float,menor_nota:float,media:float):
    print(f'Atleta : {nome}')
    for i in len(notas_dos_jurados):
        print(f'Nota: {notas_dos_jurados[i]}')
    print(f'Melhor nota: {maior_nota} ')
    print(f'Pior nota: {menor_nota}')
    print(f'Media: {media}')
