menu = """

    1 - Deposito
    2 - Saque
    3 - Extrato
    0 - Sair

    Obrigado, por utilizar nosso sistema.

"""

saldo = 0 
limite = 500
saldo_total = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(f"Escolha uma opção: {menu}"))
    if opcao == 1: 

        valor = float(input('Digite o valor, para deposito: '))

        if valor > 0:
            saldo += valor
            print(f'Valor do depositado: R${valor:.2f}.')
            extrato = f"Depósito realizado: R$ {valor:.2f}"

        else: 
            print(f'Valor R${valor:.2f} não é aceito, como deposito!')

    if opcao == 2:

        valor = float(input('Informe o valor de saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

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
        else:
            print("Operação falhou! O valor informado é inválido")

    if opcao == 3:
        linha = '#'

        print("\n"+linha * 30)
        print("\nNão foram realizadas movimentações!"  if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("\n"+linha * 30 )
        
    if opcao == 0:
        break
    