largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))    
j = 0
while j != altura:
    i = 0
    while i != largura:
        print("#", end = "")
        i = i + 1
    print()
    j = j + 1