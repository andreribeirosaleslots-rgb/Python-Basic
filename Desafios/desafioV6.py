caixaeletronico = 0
deposito = 0
saque = 0
cedulas = [50, 20, 10, 5, 2, 1]

while True:
    print("Bem-vindo ao caixa eletrônico!")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        valor = float(input("Digite o valor do depósito: "))
        deposito += valor
        caixaeletronico += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    elif escolha == '2':
        valor = float(input("Digite o valor do saque: "))
        if valor > caixaeletronico:
            print("Saldo insuficiente para saque.")
        else:
            saque += valor
            caixaeletronico -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            print("Cedulas entregues:")
            for cedula in cedulas:
                quantidade = int(valor // cedula)
                if quantidade > 0:
                    print(f"{quantidade} x R${cedula}")
                    valor -= quantidade * cedula
    elif escolha == '3':
        print("Obrigado por usar o caixa eletrônico. Volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")