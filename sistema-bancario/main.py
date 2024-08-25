class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saques_diarios = 3
        self.saques_realizados_hoje = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("\nValor de depósito inválido.")

    def sacar(self, valor):
        if self.saques_realizados_hoje >= self.limite_saques_diarios:
            print("\nLimite de saques diários atingido.")
        elif valor > 500:
            print("\nO valor máximo para saque é de R$ 500.00.")
        elif valor > self.saldo:
            print("\nSaldo insuficiente para realizar o saque.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_realizados_hoje += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("\nValor de saque inválido.")

    def exibir_extrato(self):
        if not self.extrato:
            print("\nNão foram realizadas movimentações.")
        else:
            print("\nExtrato:")
            for movimento in self.extrato:
                print(movimento)
            print(f"Saldo atual: R$ {self.saldo:.2f}")

def exibir_menu():
    print("\n=== Sistema Bancário ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Extrato")
    print("4. Sair")

def main():
    sistema = SistemaBancario()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            valor = float(input("\nDigite o valor para depósito: R$ "))
            sistema.depositar(valor)
        elif opcao == '2':
            valor = float(input("\nDigite o valor para saque: R$ "))
            sistema.sacar(valor)
        elif opcao == '3':
            sistema.exibir_extrato()
        elif opcao == '4':
            print("\nObrigado por utilizar o sistema bancário. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
