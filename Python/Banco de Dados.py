while True:
    T = "Banco de Dados"
    print("\n{:=^20}".format(T))

    c = input("Qual código você deseja ver: ")

    if c == "Sair":break

    elif c == "Calculadora":print("""Código: 
    \nwhile True:
        import math
        c = "CALCULADORA"
        print("{:=^20}".format(c))
        z = int(input("Aperte 1 para começar e qualquer outro número para sair: "))
        if z >= 2:break

        x = float(input("informe o primeiro valor: "))
        operacao = input("escolha a operação: ")
        if operacao == "raiz quadrada":print("resultado:", math.sqrt(x))
        if operacao == "raiz quadrada":continue
        y = float(input("informe o segundo valor: "))

        por1 = (x*y)/100

        if operacao == "-":print("resultado: ", x - y)
        elif operacao == "*":print("resultado: ", x * y)
        elif operacao == "/":print("resultado:", x / y)
        elif operacao == "+":print("resultado: ", x + y)
        elif operacao == "potencia":print("resultado: ", x**y)
        elif operacao == "%":print("resultado: ", (x*y)/100)
        elif operacao == "+%":print("resultado: ", x + por1)
        elif operacao == "-%":print("resultado: ", x - por1)
        else:print("erro, operacao invalida")\n""")

    elif c == "Tabuada":print("""Código: 
    \nn = int(input("Digite um número inteiro para ver sua tabuada: "))

    t = "TABUADA"

    print("_" *20)

    print("{:=^20}".format(t))

    print("{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}\n{}x6={}\n{}x7={}\n{}x8={}\n{}x9={}\n{}x10={}".format( n, n*1, n, n*2, n, n*3, n, n*4, n, n*5,  n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))


    print("_" *20)\n""")
        
    elif c == "Calcular media":print("""Código:
    \nwhile True:
    
    nota1 = float(input("\nDigite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    print("A média do aluno é: {:.2f}".format(media))
    if media >= 6:print("Aprovado!")
    elif media <= 6:print("Reprovado!")

    continuar = input("Deseja continuar?: ")
    if continuar == "nao":break""")