
from src.application.input import pega_dados_para_calculo_do_salario
from src.application.folha_de_pagamento import Salario
from src.application.output import mostra_salario
if __name__ == '__main__':
    info = pega_dados_para_calculo_do_salario()
    # sal=calcula_salario(info)
    try:
        salario = Salario(info.horas_trabalho * info.salario_hora)
    except Exception as erro:
        print('ERRO!')
    mostra_salario(salario)
    print(salario.valor_imposto_renda())