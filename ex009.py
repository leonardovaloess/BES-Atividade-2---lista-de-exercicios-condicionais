idade = int(input('Informe sua idade: '))
tempoServico = int(input('Informe o tempo de serviço (em anos): '))

#Verificar aposentadoria

if idade >= 65:
    print("Pode se aposentar")
elif tempoServico >= 30:
    print("Pode se aposentar")
elif idade >= 60 and tempoServico >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")