numero = int(input("Digite um número: "))

print("a tabuada de {} é:".format(numero))
for i in range(0, 11):
    print("{} x {} = {}".format(numero, i, numero * i))
