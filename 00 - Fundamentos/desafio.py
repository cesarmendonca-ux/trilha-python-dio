from datetime import date

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.saques = {}  

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        hoje = date.today()
        
    
        if hoje not in self.saques:
            self.saques[hoje] = []

        
        if len(self.saques[hoje]) >= 3:
            print("Limite de 3 saques diários atingido.")
            return
        
        
        if valor > 500:
            print("O limite máximo por saque é R$ 500,00.")
            return
        
        
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.saques[hoje].append(valor)
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Não será possível sacar o dinheiro por falta de saldo.")

    def extrato(self):
        print(f"\nExtrato da conta - Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("Histórico de saques:")
        if not self.saques:
            print("Nenhum saque realizado.")
        else:
            for data, lista_saques in self.saques.items():
                print(f"Data: {data}")
                for i, valor in enumerate(lista_saques, 1):
                    print(f"  Saque {i}: R${valor:.2f}")
        print("-" * 30)


def menu():
    titular = input("Digite o nome do titular da conta: ")
    conta = Conta(titular)  
    
    while True:
        print(f"\n--- Sistema Bancário - {conta.titular} ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Digite um valor numérico válido.")

        elif opcao == "2":
            try:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Digite um valor numérico válido.")

        elif opcao == "3":
            conta.extrato()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
