import math

a = float(input('Introduce el valor de a: '))
b = float(input('introduce el valor de b: '))
c = float(input('introduce el valor de c: '))

x = (b**2)-(4*a*c)

if x < 0:
    print("no se puede resolver este calculo porque no se pueden hacer raices negativas")
else:
    calculoPositivo = (-b + math.sqrt(x)) / (2*a)
    calculoNegativo = (-b - math.sqrt(x)) / (2*a)

    print("el resultado del calculo con suma es: " + str(calculoPositivo))
    print("el resultado del calculo con resta es: " + str(calculoNegativo))