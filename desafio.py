# Listas para armazenar saldo, depósitos e saques
saldo = [500]  # Iniciar com saldo de R$ 500
depositos = []
saques = []

# Menu de escolha
while True:
    print("\nSelecione uma opção:")
    print("1. Realizar depósito")
    print("2. Realizar saque")
    print("3. Exibir extrato")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo.append(valor_deposito)
            depositos.append(valor_deposito)
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        if len(saques) < 3 and valor_saque <= 500 and sum(saldo) >= valor_saque:
            saldo.append(-valor_saque)
            saques.append(valor_saque)
            print(f'Saque de R${valor_saque:.2f} realizado com sucesso.')
        elif sum(saldo) < valor_saque:
            print('Saldo insuficiente para realizar o saque.')
        else:
            print('Limite de saques diários excedido ou valor de saque inválido.')

    elif opcao == "3":
        print('--- Extrato ---')
        print('Depósitos:')
        for deposito in depositos:
            print(f'Depósito: R${deposito:.2f}')
        print('Saques:')
        for saque in saques:
            print(f'Saque: R${saque:.2f}')
        print(f'Saldo atual: R${sum(saldo):.2f}')

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
