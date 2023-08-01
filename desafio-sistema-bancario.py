def menu ():
    menu = """\n
    =================MENU==============

[1]\tDepositar     
[2]\tSacar
[3]\tExtrato
[4]\tNova conta
[5]\tlistar contas
[6]\tNovo usuario 
[7]\tSair
=> """
return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f"Deposito: \tR$ {valor:.2f}\n"
        print ("\n=== Depósito realizadocom sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

        return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Falha na operação! Saldo insuficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Falha na operação! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Falha na operação! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

        return saldo, extrato


    def exibir_extrato(saldo, /, *, extrato):
        print("\n============EXTRATO============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f\nSaldo:\t\tR$ {saldo:.2f}")
        print("=================================") 


    def criar_usuario(usuarios):
        cpf = input("Informe o CPF (somente número): ") 
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
        print("\n@@@@ Já existe usuario cadastrado com esse CPF! @@@") 
        return

        nome = input("Infome o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereço = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

        print("=== Usuário criado com sucesso! ===")     


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    reurn usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada comsucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de criação de conta encerrado! @@@")   


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta['agencia']}
            C/C:\t\{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def        