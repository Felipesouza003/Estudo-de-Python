num = int(input("Digite um número inteiro: "))
ehPrimo = True
if num != 1:
    i = num - 1
    while i != 1 and ehPrimo:
        if num % i == 0:
            ehPrimo = False
        i = i - 1
    if ehPrimo:
        print("primo")
    else:
        print("não primo")
else:
    print("primo")

