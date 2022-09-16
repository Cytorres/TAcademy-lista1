from typing import List


def pega_nome_usuario()->str:
    nome = input('Nome do Atleta: ')
    return nome

def pega_notas(total_notas: int)->List[float]:
    notas_dos_jurados = []
    for i in range(total_notas):
        notas = float(input(f'Nota do {i}º Jurado: '))
        notas_dos_jurados.append(notas)
    return notas_dos_jurados