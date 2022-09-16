def pega_voto(candidatos:any)->int:
    print('-'*100)
    print('Eleição Presidencial')
    print('-'*100)
    for i in range(len(candidatos)):
        print(f'{i+1} - {candidatos[i].nome} ')
        
    #5 - Nulo\n 6 - Branco' )
    print('_'*100)
    voto = int(input('Entre com o código do candidato e aperte ENTER para confirmar: '))
    print('_'*100)
    return voto
