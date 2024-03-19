idade = int(input("Informe sua idade para verificar se está apto à votar: "))

if idade < 16:
    print("Não é eleitor")
elif idade >= 16 and idade < 18 or idade > 65:
    print("Eleitor facultativo")
elif idade >= 18 or idade <= 65:
    print("Eleitor obrigatório")

