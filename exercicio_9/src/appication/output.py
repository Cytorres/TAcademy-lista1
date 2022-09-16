def mostrar_dados_dos_saltos(saltos:float,nome:str,melhor_salto:float,pior_salto:float,media_dos_demais_saltos:float)-> None:
    print(saltos)
    print(f'Atleta: {nome}')
    for i in range(1, 6):
        print (f'{i}º salto: {saltos[i-1]}')
    print(f'Melhor salto:{melhor_salto} m')
    print(f'Pior salto:{pior_salto} m')
    print('Resultado final: ')
    print(f'{nome} : {media_dos_demais_saltos} m')