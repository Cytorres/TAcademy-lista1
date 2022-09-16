from dataclasses import dataclass
from math import ceil
from src.application.resultado_orcamento import ResultadoOrcamento
from src.application.config import PRECO_DO_BALDE,METRAGEM_POR_BALDE
@dataclass
class OrcamentoPintura:
    def __init__(self,area:float) -> None:
        self.area = area

    
    def calcula(self)->ResultadoOrcamento:
        quantidade_lata_tinta = ceil(self.area / METRAGEM_POR_BALDE) 
        preco_total = PRECO_DO_BALDE * quantidade_lata_tinta
        return ResultadoOrcamento(preco_total,quantidade_lata_tinta)
    
    

