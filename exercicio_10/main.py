from src.application.input import pega_nome_usuario,pega_notas
from src.application.processa_notas_de_atletas import processamento_das_notas
from src.application.output import mostra_resumo_notas_atleta

if (__name__ =='__main__'):
    total_notas = 7
    nome = pega_nome_usuario()
    notas_dos_jurados = pega_notas(total_notas)
    maior_nota,menor_nota,media = processamento_das_notas(notas_dos_jurados)
    mostra_resumo_notas_atleta(nome,notas_dos_jurados,maior_nota,menor_nota,media)
