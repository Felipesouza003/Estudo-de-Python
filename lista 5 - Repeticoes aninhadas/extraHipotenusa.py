def é_hipotenusa(h, n):
    i = 1
    while i != n + 1:
        j = 1
        while j != n+1:
            if h**2 == ((i*i) + (j*j)):
                return True
            j = j + 1
        i = i + 1

def soma_hipotenusas(num):
    soma = 0
    i = 1
    while i != num + 1:
        if é_hipotenusa(i, num) == True:
            soma = soma + i
        i = i + 1
    return soma
print(soma_hipotenusas(121))