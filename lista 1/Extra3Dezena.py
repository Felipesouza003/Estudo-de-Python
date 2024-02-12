numero = int(input("Digite um número inteiro: "))

if(numero >= 10):
    print("O dígito das dezenas é", (numero//10)%10)
else:
    print("O dígito das dezenas é 0")