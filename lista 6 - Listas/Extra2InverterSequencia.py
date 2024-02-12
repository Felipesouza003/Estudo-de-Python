lista = []
x = int(input("Digite um número: "))
while x != 0:
    if x != 0:
        lista.append(x)
    x = int(input("Digite um número: "))
i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i -= 1