menu = """
==============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==============
=>\r
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    operacao = input(menu)

    if operacao == "d":
        
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f} \n")
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido!")
        
        
    elif operacao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= saldo and valor <= limite and numero_saques < LIMITE_SAQUES and valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f} \n")
            numero_saques += 1
            print("Saque realizado com sucesso! Total de operações de saque no dia: ", numero_saques)            
        elif valor > saldo:
            print("Operação falhou. Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou. O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falou. Número máximo de saques excedidos.")
        elif valor < 0:
            print("Operação falhou! O valor informado é inválido!")
        else:
            print("Algo deu errado!")

            
    elif operacao == "e":
        print("\n==========EXTRATO==========")        
        print(" Não foram realizadas movimentações. " if not extrato else extrato)        

    elif operacao == "q":
        print("Agradecemos a preferência")
        break

    else:
        print("Opção Inválida!")
        continue
    
    print("===========SALDO===========")    
    print(f"\nSaldo atualizado: R$ {saldo:.2f}")
    print("\n===========================")

else:
    print("Erro Fatal!")