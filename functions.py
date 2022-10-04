dic_hexa_para_deci = {"A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15"}
dic_deci_para_hexa = {"10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"}

def qualquer_para_decimal(base,numero):
    resultado = 0
    numero = numero[::-1]
    for index, digito in enumerate(numero):
        if digito in dic_hexa_para_deci.keys() and base == 16:
            digito = dic_hexa_para_deci[digito]
        resultado += int(digito) * base ** index
    return str(resultado)

def decimal_para_qualquer(base, numero):
    resultado = ""
    if numero == 0:
        return "0"
    while numero >= 1:
        parcial = f"{numero % base}"
        if parcial in dic_deci_para_hexa.keys() and base == 16:
            parcial = dic_deci_para_hexa[parcial]
        resultado += parcial
        numero = numero // base
    resultado = resultado[::-1]
    return resultado

def hexa_octa_para_binario(bits,numero):
    resultado = ""
    for i, digito in enumerate(numero):
        if digito in dic_hexa_para_deci.keys() and bits == 4:
            digito = dic_hexa_para_deci[digito]
        parcial = decimal_para_qualquer(2,int(digito))
        while len(parcial) % bits > 0 and i > 0:
            parcial = "0" + parcial
        resultado += parcial
    return resultado

def binario_para_hexa_octa(bits, numero):
    resultado = ""
    while len(numero) % bits > 0:
        numero = "0" + numero
    for i in range(0,len(numero)-1,bits):
        parcial = qualquer_para_decimal(2, numero[i:i+bits])
        if parcial in dic_deci_para_hexa.keys() and bits == 4:
            parcial = dic_deci_para_hexa[parcial]
        resultado += parcial
    if resultado[0] == "0":
        resultado = resultado[1:]
    return resultado

def octal_para_hexadecimal(numero):
    binario = hexa_octa_para_binario(3,numero)
    hexadecimal = binario_para_hexa_octa(16,4,binario)
    return hexadecimal

def hexadecimal_para_octal(numero):
    binario = hexa_octa_para_binario(4,numero)
    octal = binario_para_hexa_octa(8,3,binario)
    return octal

def validar_escolha_menu(numero):
    while not numero.isdigit() and (int(numero) < 1 or int(numero) > 4):
        print("Opção Inválida!")
        numero = input("Digite a opção que deseja selecionar:\n")
    return int(numero)

def opcoes(numero, base_inicial, base_final):
    if base_inicial == 1 and base_final == 2:
        resultado = binario_para_hexa_octa(8,3,numero)
    elif base_inicial == 1 and base_final == 3:
        resultado = qualquer_para_decimal(2,numero)
    elif base_inicial == 1 and base_final == 4:
        resultado = binario_para_hexa_octa(16,4,numero)
    elif base_inicial == 2 and base_final == 1:
        resultado = hexa_octa_para_binario(3,numero)
    elif base_inicial == 2 and base_final == 3:
        resultado = qualquer_para_decimal(8,numero)
    elif base_inicial == 2 and base_final == 4:
        resultado = octal_para_hexadecimal(numero)
    elif base_inicial == 3 and base_final == 1:
        resultado = decimal_para_qualquer(2,int(numero))
    elif base_inicial == 3 and base_final == 2:
        resultado = decimal_para_qualquer(8,int(numero))
    elif base_inicial == 3 and base_final == 4:
        resultado = decimal_para_qualquer(16,int(numero))
    elif base_inicial == 4 and base_final == 1:
        resultado = hexa_octa_para_binario(4,numero)
    elif base_inicial == 4 and base_final == 2:
        resultado = hexadecimal_para_octal(numero)
    else:
        resultado = qualquer_para_decimal(16,numero)
    print(f"Resposta:", resultado)

def validar_sim_nao(opcao):
    while not (opcao == "s" or opcao == "n"):
        print("Resposa Inválida!")
        opcao = input("Deseja converter outro valor? [S] ou [N]\n").lower()
    return opcao

def validar_entradas(entrada, base_inicial):
    valido = True
    dic_validacao = {1:"01", 2:"01234567", 3:"0123456789", 4:"0123456789ABCDEF"}
    caracteres = dic_validacao[base_inicial]
    for digito in entrada:
        if not digito in caracteres:
            valido = False
            break
    while not valido:
        valido = True
        print("Entrada inválida para a base selecionada!")
        entrada = input("Digite o número que deseja converter: ")
        for digito in entrada:
            if not digito in caracteres:
                valido = False
                break
    return entrada