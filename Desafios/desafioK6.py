carteira = float(input("Digite o valor da sua carteira: R$ "))

dolar = carteira / 5.25

print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(carteira, dolar))
