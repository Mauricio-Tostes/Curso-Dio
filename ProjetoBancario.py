menu = """
  💸  Bem vindo ao  💸
╔══════════════════════╗
║ 🏦 Banco Bufunfa 🏦  ║
╚══════════════════════╝

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def sacar_valor(valor):
    global saldo, numero_saques, extrato
    if valor <=0:
        print("\nValor invalido! Digite um valor maior do que zero.")
    elif saldo < valor:
        print("\nSaldo insuficiente Verifique seu extrato.")
    elif numero_saques >= LIMITE_SAQUES:
        print("\nLimite diario de saques ultrapassado! Voce pode fazer até 3 saques por dia.")
    elif valor > 500:
        print("\nValor maximo por saque ultrapassado! Voce pode sacar no maximo R$500,00 por saque.")
    else:
        numero_saques += 1
        saldo -= valor
        extrato += (f"Saque...: R$ {valor:.2f}\n")
        print(f"Saque no valor de {valor_saque:.2f} efetuado com sucesso!")

while True:

    opcao = input(menu)

    if opcao == "d":
        print()
        print("Depósito".center(40, "+"))
        valor_deposito = float(input("Informe o valor a ser depositado: ".center(40)))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print()
            print("Depósito realizado com sucesso!")
        else:
            print("\nValor de depósito Invalido! Informe um valor positivo.")

    elif opcao == "s":
        print()
        print("Saque".center(40, "-"))
        valor_saque = float(input("Digite o valor do saque: ".center(40)))
        sacar_valor(valor_saque)

    elif opcao == "e":
        print()
        print("Extrato".center(40, "="))
        print("Conta sem movimentacao!" if not extrato else extrato)
        print(f"\nO saldo atual é de R$ {saldo:.2F}\n")
        print("Fim".center(40, "="))

    elif opcao == "q":
        break

    else:
        print("\nOpcao invalida! Selecione novamente a opcao desejada.")
