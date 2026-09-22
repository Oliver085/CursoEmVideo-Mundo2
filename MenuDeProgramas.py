#Menu de Programas simples em Python
print("Escolha um programa para executar:")
print("Soma de dois números: 1")
print("Contagem Regressiva: 2")
print("Sair: 3")
escolha = input("Digite o número do programa desejado: ")
while escolha not in ["1", "2", "3"]:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    escolha = input("Digite o número do programa desejado: ")
if escolha == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("A soma de {} e {} é {}".format(num1, num2, num1 + num2))
elif escolha == "2":
    from time import sleep
    for c in range(10,-1,-1):
        sleep(1)
        print(c)
    print("Feliz Ano Novo!")
elif escolha == "3":
    print("Saindo do programa...")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
