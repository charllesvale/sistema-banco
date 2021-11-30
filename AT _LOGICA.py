ARQ = "F:\\Logica de programação\\AT - LOGICA\\contas.txt"
FIM = 0

clientes = []


def lendo_contas():
    try:
        a = open(ARQ, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>10}')


def grava_arquivo():
    with open(ARQ, "a") as contas:
        contas.write(str(clientes[0]) + ";" + str(clientes[1]) + ";" + str(clientes[2]) + '\n')

    print("Arquivo gravado")


def mostra_linha():
    print("=" * 30)


# entrar com opção:
def en_opcao():
    dado_ok = False
    while not dado_ok:
        try:
            opcao = int(input("Entre com uma opção: "))
            if (opcao < 0) or (opcao > 4):
                print("Erro: opção inválida")
            else:
                opcao_ok = True
                dado_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return opcao


# exibe o menu
def menu():
    opcao_ok = False
    while not opcao_ok:
        mostra_linha()
        print('''
    SEJA BEM VINDO AO SISTEMA XPTO

    MENU:
    [1] - INCLUIR CONTA
    [2] - RELATORIO GERENCIAL
    [3] - ALTERAR SALDO
    [4] - EXCLUIR CONTA
    [0] - SAIR
    ''')
        mostra_linha()
        return en_opcao()


def inclr_cnts():
    cod = int(input("\nInforme o codigo do cliente: "))
    clientes.append(cod)
    nome = input("Informe o nome do cliente: ")
    clientes.append(nome)
    saldo = float(input("Informe o saldo inicial: "))
    clientes.append(saldo)
    print(clientes)
    grava_arquivo()
    


# ///////////////////
# relatorio gerencial
def en_opc_relatorio_gerecial():
    dado_ok = False
    while not dado_ok:
        try:
            opcao = int(input("Entre com uma opção: "))
            if (opcao < 0) or (opcao > 3):
                print("Erro: opção inválida")
            else:
                opcao_ok = True
                dado_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return opcao

def sub_mn_relatorio_gerencial():
    opcao_ok = False
    while not opcao_ok:
        mostra_linha()
        print('''
    RELATORIO GERENCIAL

    MENU:
    [1] - LISTAR CONTAS
    [2] - CONTAS COM SALDO NEGATIVO
    [3] - CONTAS COM SALDO ACIMA DE 1000
    ''')
        mostra_linha()
        return en_opc_relatorio_gerecial()

def rltr_grncl():
    consultar = input("\nInforme o codigo do cliente: ")
    consultarV = consultar in lendo_contas()

    if consultarV == True:
        pos = clientes.index(consultar)
        print("Codigo \t Nome \t \t \t Saldo")
        print("{0} \t {1} \t {2}".format(clientes[0][pos], clientes[1][pos], clientes[2][pos]))
    else:
        print("Codigo invalido!!!")
    return


# alterar saldo
def altr_sld():
    consultar = input("\nInforme o codigo da conta em que deseja alterar o saldo: ")

    consultarV = consultar in lendo_contas()
    if consultarV == True:
        pos = clientes.index(consultar)
        deposito = input("\nInforme o valor do deposito: ")
        deposito = float(deposito)
        valor = clientes[2][pos]
        valor = valor + deposito
        clientes[2][pos] = valor
    else:
        input("Conta nao existe!!")


# entradas do menu
opcao = menu()
while opcao != FIM:
    if opcao == 1:
        inclr_cnts()
    elif opcao == 2:
        opcao1 = sub_mn_relatorio_gerencial()
        while opcao1 != 0:
            if opcao1 == 1:
                print('LISTAR CONTAS')
            elif opcao1 == 2:
                print('CONTAS COM SALDO NEGATIVO')
            elif opcao1 == 3:
                print('CONTAS COM SALDO ACIMA DE 1000')
            else:
                print("ERRO: opção inválida")    
    elif opcao == 3:
        print("ALTERAR SALDO")
        altr_sld()
    elif opcao == 4:
        print("EXCLUIR CONTA")
        # excluir_cnt()
    else:
        print("ERRO: opção inválida")
    opcao = menu()



mostra_linha()
print("""Você finalizou programa.
Até logo!""")
mostra_linha()
