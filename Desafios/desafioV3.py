from random import randint

while True:
    jogador = int(input("Digite um número: "))
    escolha = input("Par ou Ímpar? [P/I] ").upper()

    computador = randint(0, 10)

    total = jogador + computador

    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total} ")

    if total % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    if escolha == resultado:
        print("Você venceu!")
    else:
        print("Você perdeu!")
        break
print("Fim do jogo. Volte sempre!")
