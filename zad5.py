# Napisz program, który prosi o podanie współczynników 
# równania kwadratowego ax^2 + bx + c = 0 i wypisuje 
# rozwiązania równania (lub informację o braku rozwiązań).

print("Równanie ax^2 + bx + c = 0\n")
a = float(input("Podaj rzeczywiste a:\n"))
b = float(input("Podaj rzeczywiste b:\n"))
c = float(input("Podaj rzeczywiste c:\n"))

delta = b*b - 4 * a * c
if(a != 0):
    if(delta > 0):
        sqrtDelta = delta**(1/2)
        x1 = round(((-b + sqrtDelta) / (2 * a))*100)/100
        x2 = round(((-b - sqrtDelta) / (2 * a))*100)/100
        print(f"miejsca zerowe x1: {x1}, x2: {x2}")
    elif(delta == 0):
        sqrtDelta = delta**(1/2)
        x0 = round(((-b)/(2*a))*100)/100
        print(f"miejsce zerowe x0: {x0}")
    else:
        print("nie da się wyznaczyć miejsc zerowych")
else:
    print("funkcja nie jest kwadratowa")