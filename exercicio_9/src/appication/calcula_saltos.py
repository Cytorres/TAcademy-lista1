
def calculo_dos_saltos(saltos:float)->float:
    copia_dos_saltos = saltos.copy()
    melhor_salto = max(copia_dos_saltos)
    pior_salto = min(copia_dos_saltos)
    copia_dos_saltos.remove(melhor_salto)
    copia_dos_saltos.remove(pior_salto)
    soma = sum(copia_dos_saltos)

    lista_removida = len(copia_dos_saltos)
    media_dos_demais_saltos = soma/lista_removida
    return melhor_salto, pior_salto, media_dos_demais_saltos



