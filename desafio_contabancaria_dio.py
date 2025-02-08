
class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []  # Lista para armazenar transações

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor <= 0:
            print("Valor inválido para saque!")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        print("\n=== EXTRATO ===")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("================\n")

# Criando uma conta
conta_cintia = ContaBancaria("Cintia", 20000)

# Menu interativo
while True:
    print("\n=== MENU ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar Extrato")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta_cintia.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta_cintia.sacar(valor)
    elif opcao == "3":
        conta_cintia.mostrar_extrato()
    elif opcao == "4":
        print("Saindo do sistema. Obrigado!")
        break
    else:
        print("Opção inválida! Escolha novamente.")
