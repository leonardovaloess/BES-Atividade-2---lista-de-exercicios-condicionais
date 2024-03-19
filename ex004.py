nota = float(input("informe a nota do estudante: \n"))

if nota >= 7:
    print("Está aprovado!")
elif nota >= 4 and nota < 7:
    print("Estudante em recuperação")
else:
    print("reprovado")