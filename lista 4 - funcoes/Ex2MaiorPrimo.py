def ehPrimo(num):
    i = 2
    cont = 0
    while i < num:
        if(num % i == 0):
            cont = cont + 1
        i = i + 1
    if cont == 0:
        return True
    else:
        return False

def maior_primo(num): 
    i = num
    while i >= 2:
        if ehPrimo(i) == True:
            return i
        i = i - 1