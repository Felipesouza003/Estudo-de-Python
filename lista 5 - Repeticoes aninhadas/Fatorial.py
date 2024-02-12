n = 1
while n >= 0:
    n = int(input("Informe um número que deseja saber o fatorial: "))
    fatorial = 1
    while n > 1:
        fatorial = fatorial* n
        n = n - 1
    if n >= 0:
        print("O fatorial desse número é:", fatorial)