while True:
    import math

    #titulo

    print("\n{:=^20}".format("CALCULADORA"))
    
    #entrada

    primeiro_valor = float(input("\ninforme o primeiro valor: "))
    operacao = input("escolha a operação: ")
    
    #caso a operacao seja raiz quadrada

    if operacao == "raiz quadrada":
        print("resultado:", math.sqrt(primeiro_valor))
        loop_raiz = str(input("Deseja continuar?: "))
        if loop_raiz == "sim":
            continue
        elif loop_raiz == "nao":
            break    

    segundo_valor = float(input("informe o segundo valor: "))

    #variaveis das operacoes

    soma = primeiro_valor + segundo_valor
    subtracao = primeiro_valor - segundo_valor
    multiplicacao = primeiro_valor * segundo_valor
    divisao = primeiro_valor / segundo_valor
    potencia = primeiro_valor ** segundo_valor
    porcentagem = (primeiro_valor * segundo_valor) / 100
    soma_porcentagem = primeiro_valor + ((primeiro_valor * segundo_valor) / 100)
    subtracao_porcentagem = primeiro_valor - ((primeiro_valor * segundo_valor) / 100)

    #processamento e saida

    if operacao == "+":
        print("resultado: ", soma)
    elif operacao == "-":
        print("resultado: ", subtracao)
    elif operacao == "*":
        print("resultado:", multiplicacao)
    elif operacao == "/":
        print("resultado: ", divisao)
    elif operacao == "potencia":
        print("resultado: ", potencia)
    elif operacao == "%":
        print("resultado: ", porcentagem)
    elif operacao == "+%":
        print("resultado: ", soma_porcentagem)
    elif operacao == "-%":
        print("resultado: ", subtracao_porcentagem)
    else:
        print("Erro: operacao invalida")

    #loop

    loop = input("Deseja repetir?: ")

    if loop == "nao":
        break
    elif loop == "sim":
        continue