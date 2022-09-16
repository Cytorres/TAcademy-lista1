def calculo_velocidade(arquivo,velocidade_mbps):
    megabytes = float(velocidade_mbps)/ 8
    tempo_download_segundos = float(arquivo) / megabytes
    tempo_minutos = (tempo_download_segundos /60)
    tempo_em_minutos_arredondado = round(tempo_minutos,1)
    return tempo_em_minutos_arredondado,tempo_download_segundos




