while True:

    #TÍTULO

    print("\n{:=^20}".format("BANCO"))

    #ENTRADA

    saldo = float(input("\nInforme o saldo em conta: "))

    print("\nSaldo: ",saldo)
    print("\nAperte 1 para sacar")
    print("Aperte 2 para depositar")

    operacao = int(input("\nVoce deseja sacar ou depositar?: "))
    valor = float(input("Qual valor você deseja sacar/depositar?: "))

    #se der erro

    if operacao == 1 and valor > saldo:
        print("\nErro: saldo insuficiente")
        print("\nAperte 1 para repetir")
        print("Aperte 2 para sair")

        loop_erro = int(input("Voce deseja repetir?: \n"))
        
        if loop_erro == 1:
            continue
        elif loop_erro == 2:
            break
    
    #processamento e saída

    if operacao == 1:
        print("\nVoce sacou: ",valor, "\nSeu saldo em conta agora é: ", saldo - valor)
    elif operacao == 2:
        print("\nVoce depositou: ",valor, "\nSeu saldo em conta agora é: ", saldo + valor)
    else:
        print("\nOperacao invalida")

    #loop
    
    print("\nAperte 1 para repetir")
    print("Aperte 2 para sair")

    loop = int(input("Voce deseja repetir?: \n"))

    if loop == 1:
        continue
    elif loop == 2:
        break

        
