from typing import Tuple


def resultado_dos_votos(candidatos:any)->None:
    for i in range(len(candidatos)):
        print(f'{candidatos[i].nome} ==> {candidatos[i].numero_votos} voto(s)')

    #print(f'Porcentagem de votos NULOS = {nulo_porc}%')
    #print(f'Porcentagem de votos em BRANCO = {branco_porc}%')