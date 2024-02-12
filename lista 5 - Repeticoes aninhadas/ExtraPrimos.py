def ehPrimo(num):
    i = 2
    cont = 0
    while i != num:
        if num % i == 0:
            cont = cont + 1
        i = i + 1
    if cont != 0:
        return False 
    else:
        return True
    
def n_primos(num):
    i = 2
    contPrimos = 0
    while i != num + 1:
        if ehPrimo(i) == True:
            contPrimos = contPrimos + 1
        i = i + 1
    return contPrimos