def recebe_gabarito(numero_respostas):
    gabarito = []
    for numero_questao in range(numero_respostas):
        gabarito.append(input(f'Digite o gabarito da questão {numero_questao+1}: ').upper().strip())

    return gabarito

def pega_respostas_aluno(numero_respostas):
    resposta_aluno = []
    nome = input('Nome do Aluno: ')
    for indice in range(1, numero_respostas + 1):
        resposta = input(f'Digite a resposta da questão {indice}: ').upper().strip()
        resposta_aluno.append(resposta)

    return nome, resposta_aluno

def recebe_respostas(gabarito):
    pontos_aluno = 0
    resposta_aluno = []
    nome = input('Nome do Aluno: ')
    for indice in len(gabarito):
        resposta = input(f'Digite a resposta da questão {indice+1}: ').upper().strip()
        resposta_aluno.append(resposta)
        
    for indice in range(len(Lista.gabarito_da_prova)):
        if gabarito[indice] == resposta_aluno[indice]:
            pontos_aluno+=1

def saida_de_notas(resposta_aluno, total_de_alunos, media, maior_nota, menor_nota):
    print(f'Resposta do último aluno{resposta_aluno}.')
    print(f'Total de alunos{total_de_alunos}.')
    print(f'Media da notas {media}.')
    print(f'Maior nota {maior_nota}')
    print(f'Menor nota {menor_nota}.')