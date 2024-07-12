import textwrap

#Função Menu

def menu():
    menu = """
    ===== MENU PRINCIPAL =====
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [q]\tSair
    => """

    return input(textwrap.dedent(menu))

#Função para depósito de dinheiro
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"

        print("\n***** Depósito realizado com sucesso! *****")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

#Função para sacar dinheiro 
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! saldo insuficiente.")

    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nValor autorizado R$ {valor:.2f}")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

# Função que exibe extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Função principal
def main():

    LIMITE_SAQUES = 3

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0


    while True:
        
        opcao = menu()

        if opcao == "d":
            
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = deposito(saldo, valor, extrato)
   
        elif opcao == "s":  
            valor = float(input("Informe o valor que deseja sacar: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":

            break

        
        else:

            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()