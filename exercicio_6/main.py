from collections import namedtuple
from dataclasses import dataclass
from typing import List
from src.application.calcula_votos import acumula_votos

@dataclass
class Candidato:
    nome: str
    numero_votos: int = 0

from src.application.input import pega_voto
from src.application.output import resultado_dos_votos

if __name__ == '__main__':
    lista_candidatos: List[Candidato] = []
    lista_candidatos.append(Candidato('Joaquim', 0))
    lista_candidatos.append(Candidato('Mario', 0))
    lista_candidatos.append(Candidato('Felipe', 0))
    lista_candidatos.append(Candidato('Maria das Dores', 0))
    lista_candidatos.append(Candidato('Brancos', 0))
    lista_candidatos.append(Candidato('Nulos', 0))
    
    votos_validos = [i+1 for i in range(len(lista_candidatos))]
    while True:
        voto = pega_voto(lista_candidatos)
        if (voto == 0):
            break

        if not voto in votos_validos: 
            print('Voto inválido')
            sleep(2)
            continue

        acumula_votos(lista_candidatos, voto)
         
    resultado_dos_votos(lista_candidatos)


        