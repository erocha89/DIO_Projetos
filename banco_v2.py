import textwrap


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print('Operação falhou! Limite insuficiente.')

    elif excedeu_limite:
        print('Operação falhou! O valor de saque excede o limite.')

    elif excedeu_saques:
        print('Operação falhou! Número de saques excedidos.')

    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n*** Saque realizado com sucesso {valor:.2f} ***")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido @@@")
    
    return saldo, extrato

def deposito(saldo, valor, extrato, /):

    if valor > 0:

        saldo += valor

        print(f'\n*** Valor do depositado: R${valor:.2f}. ***')

        extrato = f"Depósito realizado:\t R$ {valor:.2f}\n"

    else: 
        print(f'\n@@@ Valor R${valor:.2f} não é aceito, como deposito! @@@')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    linha = '#'

    print(f"\n{linha * 30} EXTRATO {linha * 30}")
    print("\nNão foram realizadas movimentações."  if not extrato else extrato)
    print(f'\n*** Saldo: R$ {saldo:.2f} ***')
    print("\n"+linha * 69)

def criar_usuario(usuarios):


    cpf = input("Digite os números do CPF sem . e sem - : ")
    usuario = filtrar_usuarios(cpf, usuarios)


    if usuario:
        print("\n@@@ CPF já esta cadastrado!, @@@")
        return
    else:

        nome = input("Digite o nome do cliente: ")
        data_nasc = input("Digita a data de nascimento do cliente DD-MM-YYYY: ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "Data_nascimento": data_nasc, "cpf": cpf, "Endereco": endereco})
            
        print("*** Usuário criado com sucesso! ***")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuarios:
        print("\n*** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))



def menu():
    menu = """\n
    ************* MENU *************
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tLista de Contas
    [6]\tNovo Usuário
    [0]\tSair
    ********************************
    =>
        """
    
    return input(textwrap.dedent(menu))
        
def main():
    AGENCIA = "0001"
    LIMITE_SAQUE = 3

    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    contas = []
    usuarios = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUE
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            lista_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()