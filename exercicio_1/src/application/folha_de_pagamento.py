from dataclasses import dataclass
# from src.application.input import InfoCalculoSalario
from src.application.config import Imposto

@dataclass
class Salario:
    salario_bruto:float = 0
    def __init__(self,salario_bruto:float) -> None:
        if salario_bruto < 0:
            raise Exception("Salario não pode ser menor que zero!")
        self.salario_bruto = salario_bruto
    
    def valor_imposto_renda(self): return round(self.salario_bruto * Imposto.IMPOSTO_RENDA,2)
    def valor_inss(self): return round(self.salario_bruto * Imposto.INSS, 2)
    def valor_sindicato(self): return round(self.salario_bruto * Imposto.SINDICATO, 2)
    def salario_liquido(self): return self.salario_bruto - self.valor_imposto_renda() - self.valor_inss() - self.valor_sindicato()


""" 
def calcula_salario(info_salario:InfoCalculoSalario)->float:
    salario = Salario()
    salario.salario_bruto = float(info_salario.salario_hora * info_salario.horas_trabalho)
    salario.valor_imposto_renda = round(salario.salario_bruto * IMPOSTO_RENDA, 2)
    salario.valor_inss = round(salario.salario_bruto * INSS, 2)
    salario.valor_sindicato = round(salario.salario_bruto * SINDICATO, 2)
    salario.descontos = salario.valor_imposto_renda + salario.valor_inss + salario.valor_sindicato
    salario.salario_liquido = salario.salario_bruto - salario.descontos
    return salario """


