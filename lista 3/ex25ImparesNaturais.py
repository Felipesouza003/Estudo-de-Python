n = int(input("Digite o valor de n: "))

i = 0
j = 1
while i < n:
    if j % 2 != 0:
        print(j)
        j = j + 1
        i = i + 1
    j = j + 1