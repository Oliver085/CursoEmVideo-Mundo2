pessoa=int(input("Digite seu ano de nascimento: "))
anoatual=2026
idade=anoatual-pessoa

if idade >= 18:
    print("Você é maior de idade, está apto para se alistar.")
elif idade == 18:
    print("Você possui {} anos, está no ano de alistamento.".format(idade))
else:
    print("Você possui {} anos, ainda não está apto para se alistar, faltam {} anos.".format(idade, 18-idade))
