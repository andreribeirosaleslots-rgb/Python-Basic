from random import randint

numero = (
    randint(0,10),
    randint(0,10),
    randint(0,10),
    randint(0,10),
    randint(0,10)
)
print(numero)
print(f"O maior número é {max(numero)}")
print(f"O menor número é {min(numero)}")