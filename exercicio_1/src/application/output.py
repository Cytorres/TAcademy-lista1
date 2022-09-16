
from src.application.folha_de_pagamento import Salario


def mostra_salario(salario:Salario):
    print(f'+ Salário Bruto : R${salario.salario_bruto}')
    print(f'- IR (11%) : R${salario.valor_imposto_renda()}')
    print(f'- INSS (8%) : R${salario.valor_inss()}')
    print(f'- Sindicato (5%) : R${salario.valor_sindicato()}')
    print(f'= Salário Liquido : R${salario.salario_liquido()}')