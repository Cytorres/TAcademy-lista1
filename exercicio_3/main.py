from src.application.input import pega_area_pintura
from src.application.calcula_galao_e_lata_de_tinta import OrcamentoPintura,calcula_metros_quadrados,calculo_das_latas,calculo_de_galao,calculo_preco_galao_e_latas
from src.application.output import mostra_orcamento 

if __name__ == '__main__':
    area_pintura = pega_area_pintura()
    orcamento = OrcamentoPintura(area_pintura)
    ---------------------------------------------
    superficie_metros_quadrados,metros_lata = calcula_metros_quadrados(area_pintura)
    quantidade_latas,valor_total_lata = calculo_das_latas(superficie_metros_quadrados,metros_lata)
    quantidade_galao,metros_galao,valor_total_galao = calculo_de_galao(superficie_metros_quadrados,metros_lata)
    quantidade_latas_em_litros,preco_lata_alternativa3,preco_galao_alternativa3,quantidade_galão_litro = calculo_preco_galao_e_latas(superficie_metros_quadrados)
    mostra_orcamento(quantidade_latas,valor_total_lata,quantidade_galao,valor_total_galao,quantidade_latas_em_litros,preco_lata_alternativa3,quantidade_galão_litro,preco_galao_alternativa3)