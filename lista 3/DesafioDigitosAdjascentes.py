num = int(input("Digite um número inteiro: "))
anterior = num % 10
num = num // 10

adjascenteIgual = False

while num != 0 and not adjascenteIgual:
    atual = num % 10
    if atual == anterior:
        adjascenteIgual = True
    else:
        anterior = atual
        num = num // 10
if adjascenteIgual:
    print("Este número inteiro posssui dois dígitos",anterior, "adjascentes iguais!")
else:
    print("Este número inteiro não posssui dois dígitos adjascentes iguais!")
