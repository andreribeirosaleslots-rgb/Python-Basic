numero = int(input("Digite um número: "))

n1 = numero - 1
n2 = numero + 1
n3 = numero * 2
n4 = numero / 2
n5 = numero ** 2
n6 = numero ** 3
n7 = numero ** 0.5


print("O antecessor de {} é {} e o sucessor é {}".format(numero, n1, n2))
print("O dobro de {} é {} e a metade é {}".format(numero, n3, n4))
print("O quadrado de {} é {} e o cubo é {}".format(numero, n5, n6))
print("A raiz quadrada de {} é {:.2f}".format(numero, n7))