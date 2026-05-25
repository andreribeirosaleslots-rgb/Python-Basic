salario = float(input("Digite o salário do funcionário: R$ "))

aumento = salario * 0.15
salario_final = salario + aumento

print("O salário do funcionário com 15% de aumento é: R$ {:.2f}".format(salario_final))