from src.application.calculo_notas import pega_respostas_aluno, recebe_gabarito
if(__name__ == '__main__'):
    numero_respostas = 3
    gabarito = recebe_gabarito(numero_respostas)
    total_alunos = 0
    while True:
        total_alunos +=1
        nome, respostas = pega_respostas_aluno(numero_respostas)
        x = [indice for indice in range(len(gabarito)) if gabarito[indice] == respostas[indice]]
        pontuacao = len(x)
        print(f"{nome} {pontuacao}")

        prompt_de_continuacao = input('Deseja continuar? ').upper().strip()
        if (prompt_de_continuacao == 'S'or prompt_de_continuacao == ''):
            continue
        else:
            break
    #saida_de_notas()
    