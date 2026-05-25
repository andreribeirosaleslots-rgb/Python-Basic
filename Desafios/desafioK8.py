produto = float(input("Digite o preço do produto: R$ "))
desconto = produto * 0.05
preco_final = produto - desconto

print("O preço do produto com 5% de desconto é: R$ {:.2f}".format(preco_final))