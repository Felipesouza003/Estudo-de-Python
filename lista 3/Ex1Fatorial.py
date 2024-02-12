n = int(input("Digite o valor de n: 5 "))
fat = n
if n != 0:
    while n != 1:
        n = n -1 
        fat = fat * n
    print(fat)
else:
    print(1)