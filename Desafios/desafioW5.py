produtos = ("Arroz", 22.99, "Feijão", 15.99, "Macarrão", 8.99, "Carne", 29.99, "Leite", 6.99)

print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)
for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<30} R$ {produtos[i+1]:>7.2f}")
print("-" * 40)