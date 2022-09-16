from src.application.input import pega_area_pintura
from src.application.orcamento_pintura import  OrcamentoPintura
from src.application.output import mostra_orcamento

if __name__== '__main__':
   area_pintura = pega_area_pintura()
   orcamento = OrcamentoPintura(area_pintura)
   retorno = orcamento.calcula()
   a = retorno.preco_total
   b = retorno.quantidade_lata_tinta
   mostra_orcamento(a,b)