n = int(input("Por favor, digite um número inteiro: "))
lista = [n] 
i = 0
while n != 0:
    n = int(input("Por favor, digite um número inteiro: "))
    if n != 0 :
        lista.append(n)
        i = i + 1
while i >= 0:
    print(lista[i], end= " ")
    i = i - 1
print()