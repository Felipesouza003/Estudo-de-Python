largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))    
j = 0
while j != altura:
    i = 0
    while i != largura:
        if(i == 0 or j == 0 or i == largura -1 or j == altura -1):
            print("#", end = "")
        else:
            print(" ", end = "")
        i = i + 1
    print()
    j = j + 1