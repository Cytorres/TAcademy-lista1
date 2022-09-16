from dataclasses import dataclass
from src.application.config import LITRO_METRO,LATA,METROS_POR_LATA,PRECO_LATA,GALAO,PRECO_GALAO
from math import ceil
@dataclass

class OrcamentoPintura:
    def __init__(self,area:float) -> None:
        self.area

    def calculo_das_latas(self,METROS_POR_LATA):
        quantidade_latas = ceil(self.area / METROS_POR_LATA)
        valor_total_lata = PRECO_LATA * quantidade_latas
        return quantidade_latas,valor_total_lata

    def calculo_de_galao(self,METROS_POR_LATA):
        metros_galao = GALAO * LITRO_METRO #cada galão faz 21,6 m²
        quantidade_galao = ceil(self.area / METROS_POR_LATA)
        valor_total_galao = PRECO_GALAO * quantidade_galao

        return quantidade_galao,metros_galao,valor_total_galao

    def calculo_preco_galao_e_latas(self):
        superficie_com_folga = self.area +  self.area *(0.10)
        quantidade_em_litros_tinta =  superficie_com_folga / LITRO_METRO
        
        quantidade_latas_em_litros = ceil(quantidade_em_litros_tinta / LATA)
        preco_lata_alternativa3 = quantidade_latas_em_litros * PRECO_LATA
        

        litro_da_lata_inteira = quantidade_latas_em_litros * LATA
        resto_de_tinta = quantidade_em_litros_tinta - litro_da_lata_inteira
        quantidade_galão_litro = ceil(resto_de_tinta / GALAO)
        preco_galao_alternativa3 = quantidade_galão_litro * PRECO_GALAO


        return quantidade_latas_em_litros,preco_lata_alternativa3,preco_galao_alternativa3,quantidade_galão_litro










