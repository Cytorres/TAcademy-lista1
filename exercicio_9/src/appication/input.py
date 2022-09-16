def entrada_dos_saltos():
    saltos = []
    nome = input('Nome do Atleta: ')
    for i in range(1,6):
        saltos_informados = input(f'Informe o {i}º salto: ')
        saltos_informados = float(saltos_informados)
        saltos.append(saltos_informados)
    return saltos,nome