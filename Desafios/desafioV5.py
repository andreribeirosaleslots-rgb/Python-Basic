valordacompra = 0
produtovale = 0
produtomaisbarato = 0

while True:
    nomeproduto = str(input("Digite o nome do produto: "))
    valorproduto = float(input("Digite o valor do produto: R$ "))
    valordacompra += valorproduto
    produtovale += 1
    if valorproduto > 1000:
        produtomaisbarato += 1
    if produtomaisbarato == 0 or valorproduto < produtomaisbarato:
        produtomaisbarato = valorproduto
        nomeprodutomaisbarato = nomeproduto
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == 'N':
        break

print(f"O total da compra foi R$ {valordacompra:.2f}")
print(f"Temos {produtovale} produtos custando mais de R$ 1000.00")
print(f"O produto mais barato foi {nomeprodutomaisbarato} que custa R$ {produtomaisbarato:.2f}")