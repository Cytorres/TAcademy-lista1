from src.appication.input import entrada_dos_saltos
from src.appication.calcula_saltos import calculo_dos_saltos
from src.appication.output import mostrar_dados_dos_saltos

if (__name__=='__main__'):
    saltos,nome = entrada_dos_saltos()
    melhor_salto, pior_salto, media_dos_demais_saltos = calculo_dos_saltos(saltos)
    mostrar_dados_dos_saltos(saltos,nome,melhor_salto,pior_salto,media_dos_demais_saltos)