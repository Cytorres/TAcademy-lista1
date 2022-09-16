from typing import List, Tuple

def processamento_das_notas(notas_dos_jurados:List[float])->Tuple(float, float, float):      
    copia_das_notas = notas_dos_jurados.copy()
    maior_nota = max(copia_das_notas)
    menor_nota = min(copia_das_notas)
    copia_das_notas.remove(maior_nota)
    copia_das_notas.remove(menor_nota)
    if (len(copia_das_notas)==0): return maior_nota, menor_nota, 0
    
    soma = sum(copia_das_notas)
    media = soma/len(copia_das_notas)
    return maior_nota, menor_nota, media

