#Esse exercicio tem como proposta uma validação simples de dados usando while

sexo = str(input("informe seu sexo: [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados invalidos, Por favor, informe o sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado como sucesso!")