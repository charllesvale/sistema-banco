ARQ = "F:\\Logica de programação\\AT - LOGICA\\contas.txt"
FIM = 0
cliente = []

def mostra_linha():
    print("=" * 30)


def lendo_contas():
    with(open(ARQ, "r")) as contas:
        linha = contas.readline()
        while(linha != ""):
            linha = linha.strip("\n")
            linha = linha.split(";")
            cod = int(linha[0])
            nome = linha[1]
            saldo = float(linha[2])
            conta = [cod, nome, saldo]
            cliente.append(conta)
            linha = contas.readline()
    return cliente             


def ler_relatorio_ger():
    print('LISTA DE CONTAS')
    for i in cliente:
        dado = i
        dado[2] = dado[2]
        print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>15}')
    

def grava_arquivo(cliente):
    with open(ARQ, "w+") as contas:
        for clnt in cliente:
            contas.write(str(clnt[0]) + ";" + str(clnt[1]) + ";" + str(clnt[2]) + "\n")
    print("Arquivo Gravado")


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


def validate_account():
    cnt= validate_int()
    while cnt not in cliente:
        for i in cliente:
            while cnt == i[0]:
                print('conta ja existe')
                cnt = validate_int()
        return cnt         


def validate_name():
    name= validate_str()
    v_name = name.split(" ")
    while len(v_name ) <=1 :
        print("insira nome e sobrenome")
        name= validate_str()
        v_name = name.split(" ")
    return name

    
def validate_balance():
    sld= validate_float()
    while sld <= 0:
        print('Saldo tem que ser maior que zero')
        return validate_balance()  
    return sld


def validate_int():
    int_ok = False
    while not int_ok:
        try:
            cnt = int(input("Informe o codigo do cliente: "))
            int_ok = True
            while cnt <= 0:
                print("Digite uma conta maior diferente de 0")
                cnt = validate_int()
        except ValueError:
            print("Caractere invalido" "\nDigite um numero")
    return cnt


def validate_float():
    flt_ok = False
    while not flt_ok:
        try:
            sld = float(input("Informe o saldo inicial: "))
            flt_ok = True
        except ValueError:
            print("Caractere invalido")
    return sld


def validate_str():
    str_ok = False
    try:
        while not str_ok:
            nm = (input("Informe o nome do cliente: "))
            str_ok = True
    except:
        print("Caractere invalido")
        
    return nm


def add_accounts():
    cod = validate_account()
    nome = validate_name()
    saldo = validate_balance()
    cliente.append([cod, nome, saldo])
    print(cliente)


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
    [0] - SAIR
    ''')
        mostra_linha()
        return en_opc_relatorio_gerecial()


def read_balance_negative():
    print('CONTAS COM SALDO NEGATIVO')  
    try:
        for i in cliente:
            if i[2] < 0:
                dado = i
                dado[2] = dado[2]
                print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>15}')
               
    except:
        print("não há contas com saldo negativo")


def read_balance_positive():
    print('CONTAS COM SALDO ACIMA DE 1000') 
    try:
        for i in cliente:
            if i[2] > 1000:
                dado = i
                dado[2] = dado[2]
                print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>15}')
    except:
        print("não há contas acima de 1000")                      
         

def change_account():
    acco = validate_float()
    contador = 0
    for i in cliente:
        if acco == i[0]:
            if i[2] == 0: 
                del(cliente[contador])
                print("Conta removida com sucesso")
            else:
                print("conta com saldo")
        contador += 1
                    

def en_op_balance():
    dado_ok = False
    while not dado_ok:
        try:
            opcao = int(input("Entre com uma opção: "))
            if (opcao < 0) or (opcao > 2):
                print("Erro: opção inválida")
            else:
                opcao_ok = True
                dado_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return opcao


def sub_menu_balance():
    opcao_ok = False
    while not opcao_ok:
        mostra_linha()
        print('''
       
    [1] - Depositar
    [2] - Sacar
    [0] - Sair
    ''')
        mostra_linha()
        return en_op_balance()
        

def deposit():
    consult = validate_int()
    for i in cliente:
        if consult == i[0]:
            dpst = float(input('Digite o valor do deposito'))
            i[2] = dpst + i[2]
            print("Valor adcionado com sucesso.")
            print(i[2])  

 
def withdraw():
    consult = validate_int()
    for i in cliente:
        if consult == i[0]:
            dpst = float(input('Digite o valor do saque'))
            i[2] = i[2] - dpst
            print("Saque feito com sucesso.")
            print(i[2]) 


def remove_account():
    acco = validate_int()
    contador = 0
    for i in cliente:
        if acco == i[0]:
            if i[2] == 0: 
                del(cliente[contador])
                print("Conta removida com sucesso")
            else:
                print("conta com saldo")
        contador += 1


lendo_contas()
opcao = menu()
while opcao != FIM:
    if opcao == 1:
        add_accounts()
    elif opcao == 2:
        op1 = sub_mn_relatorio_gerencial()
        while op1 != FIM:
            if op1 == 1:
                ler_relatorio_ger()          
            elif op1 == 2:
                read_balance_negative()
            elif op1 == 3:
                read_balance_positive()
            else:
                print("ERRO: opção inválida")
            op1 = sub_mn_relatorio_gerencial()    
    elif opcao == 3:
        op2 = sub_menu_balance()
        while op2 != FIM:
            if op2 == 1:
                deposit()       
            elif op2 == 2:
                withdraw()
            else:
                print("ERRO: opção inválida")
            op2 = sub_menu_balance()
    elif opcao == 4:
        remove_account()       
    else:
        print("ERRO: opção inválida")
    opcao = menu()
grava_arquivo(cliente)
mostra_linha()
print("""Você finalizou programa.
Até logo!""")
mostra_linha()
