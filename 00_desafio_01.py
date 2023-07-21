class Cliente:
    def __init__(self, nome, id, senha, saldo, limite, extrato='', numero_saques=0):
        self.nome = nome
        self.id = id
        self.senha = senha
        self.saldo = saldo
        self.limite = limite
        self.extrato = extrato
        self.numero_saques = numero_saques

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += (f"Depósito: R$ {valor:.2f} \n")
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido!")

    def sacar(self, valor):
        if valor <= self.saldo and valor <= self.limite and self.numero_saques < LIMITE_SAQUES and valor > 0:
            self.saldo -= valor
            self.extrato += (f"Saque: R$ {valor:.2f} \n")
            self.numero_saques += 1
            print("Saque realizado com sucesso! Total de operações de saque no dia: ", self.numero_saques)            
        elif valor > self.saldo:
            print("Operação falhou. Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("Operação falhou. O valor do saque excede o limite.")
        elif self.numero_saques >= LIMITE_SAQUES:
            print("Operação falou. Número máximo de saques excedidos.")
        elif valor < 0:
            print("Operação falhou! O valor informado é inválido!")
        else:
            print("Algo deu errado!")
    
    def exibir_extrato(self):
        print("\n==========EXTRATO==========")        
        print(" Não foram realizadas movimentações. " if not self.extrato else self.extrato)        


# class Conta(Cliente):
#     def __init__(self, nome, id, senha, saldo, limite, extrato='', numero_saques=0, cheque_especial=0):
#         super().__init__(nome, id, senha, saldo, limite, extrato, numero_saques)        
#         self.cheque_especial = cheque_especial

def identificar_cliente():
    return int(input("Informe sua id de usuário: "))
    
def senha_cliente():
    return int(input("Informe sua senha: "))


menu = """
==============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[z] Encerrar
==============
=>\r
"""

LIMITE_SAQUES = 3
cliente = [
    Cliente('Cliente Um', 0, 1111, 0, 500), 
    Cliente('Cliente Dois', 1, 2222, 0, 1000), 
    Cliente('Cliente Três', 2, 3333, 0, 100)]

operacao = 'q'

# conta = [
#     ('universitaria', Conta('Cliente Um', 0, 1111, 0, 500, 500)),
#     ('especial', Conta('Cliente Dois', 1, 2222, 0, 1000, 1000)),
#     ('universitaria', Conta('Cliente Três', 2, 3333, 0, 100, 500)),
# ]

# print(conta[0][1].cheque_especial)

while True:
  
    if operacao == "q":
        
        id = identificar_cliente()
        if id > len(cliente):
            print("Usuário não cadastrado!")
            continue

        senha = senha_cliente()
        if senha != cliente[id].senha:
            print("Senha inválida!")
            continue
        else:
            print("Cliente identificado!")
            print(f"Bem-vindo, {cliente[id].nome}!")                       
    
    elif operacao == "d":
        
        valor = float(input("Informe o valor do depósito: "))
        cliente[id].depositar(valor)
               
    elif operacao == "s":

        valor = float(input("Informe o valor do saque: "))
        cliente[id].sacar(valor)       
            
    elif operacao == "e":
        
        cliente[id].exibir_extrato()

    elif operacao == "z":
        print("Agradecemos a preferência")
        break

    else:
        print("Opção Inválida!")
        operacao = 'z'
        continue  

    print("===========SALDO===========")    
    print(f"\nSaldo atualizado: R$ {cliente[id].saldo:.2f}")
    print("\n===========================")

    operacao = input(menu)

else:
    print("Erro Fatal!")