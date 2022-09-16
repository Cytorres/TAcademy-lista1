from src.appication.input import entrada_de_dados 
from src.appication.domain import calculo_velocidade
from src.appication.output import saida_do_resultado

if __name__=='__main__':
   arquivo,velocidade_mbps = entrada_de_dados()
   tempo_em_minutos_arredondado,tempo_download_segundos=calculo_velocidade(arquivo,velocidade_mbps)
   saida_do_resultado(tempo_em_minutos_arredondado,tempo_download_segundos)



