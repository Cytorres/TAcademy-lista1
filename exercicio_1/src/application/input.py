from dataclasses import dataclass

@dataclass()
class InfoCalculoSalario:
    salario_hora:float = 0
    horas_trabalho:float = 0

def pega_dados_para_calculo_do_salario():
    info_calculo_salario = InfoCalculoSalario()
    info_calculo_salario.salario_hora = float(input('Informe o seu salário por hora: '))
    info_calculo_salario.horas_trabalho = float(input('Horas trabalhadas no mês: '))
    return info_calculo_salario
    # return InfoCalculoSalario(salario_hora = salario_hora, horas_trabalho = horas_trabalho)