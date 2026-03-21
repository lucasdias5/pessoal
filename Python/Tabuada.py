while True:
    n = int(input("Digite um número inteiro para ver sua tabuada: "))

    t = "TABUADA"

    print("_" *20)

    print("{:=^20}".format(t))

    print("{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}\n{}x6={}\n{}x7={}\n{}x8={}\n{}x9={}\n{}x10={}".format( n, n*1, n, n*2, n, n*3, n, n*4, n, n*5,  n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
    
    print("_" *20)
    if n == "Sair":break