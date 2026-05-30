valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))
valor3 = int(input("Digite mais um número: "))
valor4 = int(input("Digite o último número: "))

numeros = (valor1, valor2, valor3, valor4)

print(f"Você digitou os números: {numeros}")
print(f"O valor nove apareceu {numeros.count(9)} vezes")
print(f"O primeiro valor 3 apareceu na posição {numeros.index(3) + 1} " if 3 in numeros else "O valor 3 não foi digitado")
print(f"Os números pares são: ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")