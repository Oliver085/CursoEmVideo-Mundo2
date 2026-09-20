valorCasa=int(input("Digite o valor da casa: "))
salario=int(input("Digite o valor do seu salário: "))
anos=int(input("Digite em quantos anos você deseja pagar: "))
prestacao=valorCasa/(anos*12)
if prestacao>salario*0.3:
    print("Empréstimo negado! A prestação mensal de R${:.2f} excede '30%' do seu salário.".format(prestacao))
else:
    print("Empréstimo aprovado! A prestação mensal será de R${:.2f}.".format(prestacao))