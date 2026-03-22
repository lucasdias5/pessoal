while True:
    import math
    c = "CALCULADORA"
    print("\n{:=^20}".format(c))
    
    x = float(input("\ninforme o primeiro valor: "))
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
    else:print("erro, operacao invalida")

    c = input("Deseja repetir?: ")
    if c == "não":break
