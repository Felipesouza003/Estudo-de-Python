import math

a = int(input("Por favor informe o coeficiente que acaompanha o x² da equação ou seja o a: "))
b = int(input("Por favor informe o coeficiente que acaompanha o x da equação ou seja o b: "))
c = int(input("Por favor informe o coeficiente constante da equação ou seja o c: "))


delta  = (b**2 - (4*a*c))

if delta == 0:
    print("a raiz dupla desta equação é", ((-b)/ 2*a))
elif delta >  0:
    raiz1 = ((-b + math.sqrt(delta))/ (2*a))
    raiz2 = ((-b - math.sqrt(delta))/ (2*a))
    if raiz1 <= raiz2:
        print("as raízes da equação são", raiz1,  "e", raiz2)
    else:
        print("as raízes da equação são", raiz2,  "e", raiz1)
else:
    print("esta equação não possui raízes reais")