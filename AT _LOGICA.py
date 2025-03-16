ARQ = "contas.txt"
FIM = 0
client = []

def show_lines():
    print("=" * 30)

def line_acc_nm_blnc():
    print("{:<5} {:<10} {:>15}".format('COD','NOME','SALDO'))

def read_accounts():
    with(open(ARQ, "r")) as contas:
        line = contas.readline()
        while(line != ""):
            line = line.strip("\n")
            line = line.split(";")
            cod = int(line[0])
            name = line[1]
            balance = float(line[2])
            conta = [cod, name, balance]
            client.append(conta)
            line = contas.readline()
    return client             

def write_file(client):
    with open(ARQ, "w+") as contas:
        for clnt in client:
            contas.write(str(clnt[0]) + ";" + str(clnt[1]) + ";" + str(clnt[2]) + "\n")
    print("Arquivo Gravado com sucesso")

def enter_option():
    data_ok = False
    while (not data_ok):
        try:
            option = int(input("Entre com uma opção: "))
            if (option < 0) or (option > 4):
                print("Erro: opção inválida")
            else:
                data_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return option

def menu():
    option_ok = False
    while (not option_ok):
        show_lines()
        print('''
    SEJA BEM VINDO AO SISTEMA XPTO

    MENU:
    [1] - INCLUIR CONTA
    [2] - RELATORIO GERENCIAL
    [3] - ALTERAR SALDO
    [4] - EXCLUIR CONTA
    [0] - SAIR
    ''')
        show_lines()
        return enter_option()

def validate_account():
    cnt= validate_int()
    while (cnt not in client):
        for i in client:
            while (cnt == i[0]):
                print('conta ja existe')
                cnt = validate_int()
        return cnt         

def validate_name():
    name= validate_str()
    v_name = name.split(" ")
    while (len(v_name ) <=1):
        print("insira nome e sobrenome:")
        name= validate_str()
        v_name = name.split(" ")
    return name
  
def validate_balance():
    sld= validate_float()
    while (sld <= 0):
        print('saldo tem que ser maior que zero')
        return validate_balance()  
    return sld

def validate_int():
    int_ok = False
    while (not int_ok):
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
    while (not flt_ok):
        try:
            sld = float(input("Informe o saldo inicial: "))
            flt_ok = True
        except ValueError:
            print("Caractere invalido")
    return sld

def validate_str():
    str_ok = False
    try:
        while (not str_ok):
            nm = str(input("Informe o nome do cliente: "))
            str_ok = True
    except:
        print("Caractere invalido")
        
    return nm

def add_accounts():
    cod = validate_account()
    name = validate_name()
    balance = validate_balance()
    client.append([cod, name, balance])
    line_acc_nm_blnc()
    print("{:<5} {:<10} {:>10}".format(cod, name, balance))

def sub_m_m_1():
    op1 = sub_mn_management_report()
    while (op1 != FIM):
        if (op1 == 1):
            read_reports()          
        elif (op1 == 2):
            read_balance_negative()
        elif (op1 == 3):
            read_balance_positive()
        else:
            print("ERRO: opção inválida")
        op1 = sub_mn_management_report()

def enter_management_report_option():
    data_ok = False
    while (not data_ok):
        try:
            option = int(input("Entre com uma opção: "))
            if (option < 0) or (option > 3):
                print("Erro: opção inválida")
            else:
                data_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return option

def sub_mn_management_report():
    option_ok = False
    while (not option_ok):
        show_lines()
        print('''
    RELATORIO GERENCIAL

    MENU:
    [1] - LISTAR CONTAS
    [2] - CONTAS COM SALDO NEGATIVO
    [3] - CONTAS COM SALDO ACIMA DE 1000
    [0] - SAIR
    ''')
        show_lines()
        return enter_management_report_option()

def read_reports():
    print('LISTA DE CONTAS')
    line_acc_nm_blnc()
    for i in client:
        dado = i
        print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>15}')
        
def read_balance_negative():
    print('CONTAS COM SALDO NEGATIVO')
    line_acc_nm_blnc()
    for i in client:
        if (i[2] < 0):
            dado = i
            print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>15}')

def read_balance_positive():
    print('CONTAS COM SALDO ACIMA DE 1000')
    line_acc_nm_blnc() 
    for i in client:
        if (i[2] > 1000):
            dado = i  
            print(f'{dado[0]:<5}{dado[1]:<10}{dado[2]:>15}')
                   
def en_op_balance():
    data_ok = False
    while (not data_ok):
        try:
            option = int(input("Entre com uma opção: "))
            if (option < 0) or (option > 2):
                print("Erro: opção inválida")
            else:
                data_ok = True
        except ValueError:
            print("Erro: entrada inválida")
    return option

def sub_menu_balance():
    option_ok = False
    while (not option_ok):
        show_lines()
        print('''
       
    [1] - DEPOSITAR
    [2] - SACAR
    [0] - SAIR
    ''')
        show_lines()
        return en_op_balance()

def sub_m_b_2():
    op2 = sub_menu_balance()
    while (op2 != FIM):
        if (op2 == 1):
            deposit()       
        elif (op2 == 2):
            withdraw()
        else:
            print("ERRO: opção inválida")
        op2 = sub_menu_balance()

def deposit():
    consult = validate_int()
    for i in client:
        if (consult == i[0]):
            dpst = float(input('Digite o valor do deposito:'))
            i[2] = dpst + i[2]
            print("Valor adcionado com sucesso.")
            print('Saldo:', i[2])
        
def withdraw():
    consult = validate_int()
    for i in client:
        if (consult == i[0]):
            dpst = float(input('Digite o valor do saque:'))
            i[2] = i[2] - dpst
            print("Saque feito com sucesso.")
            print('Saldo:',i[2])

def remove_account():
    acco = validate_int()
    counter = 0
    for i in client:
        if (acco == i[0]):
            if (i[2] == 0): 
                del(client[counter])
                print("Conta removida com sucesso")
            elif(i[2] > 0):
                print("conta com saldo")
            else:
                print("conta com saldo negativo")
        counter += 1        
           
read_accounts()
option = menu()
while (option != FIM):
    if (option == 1):
        add_accounts()
    elif (option == 2):
        sub_m_m_1() 
    elif (option == 3):
        sub_m_b_2()
    elif (option == 4):
        remove_account()       
    else:
        print("ERRO: opção inválida")
    option = menu()
write_file(client)
show_lines()
print("""Você finalizou programa.
Até logo!""")
show_lines()
