# Napisz program, który poprosi użytkownika o podanie 
# współrzędnych kartezjańskich x, y, z punktu w 
# przestrzeni, a następnie przeliczy je na współrzędne
# w układzie sferycznym i cylindrycznym i wypisze wyniki.
# Zadbaj nie tylko o poprawność wyniktów, ale także o 
# czytelność kodu i komunikację z użytkownikiem. Użyj 
# funkcji matematycznych z biblioteki math.

import math

print("Podaj współrzędne kartezjańskie:")
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

print("\nUkład sferyczny:")
r = (x*x + y*y + z*z) ** (1/2)
heLong = (180 / math.pi) * math.atan2(y, x) # w stopniach
heLat = (180 / math.pi) * math.asin(z/r) # w stopniach
print(f"r: {round(r*100)/100}," 
      + f" długość sferyczna: {round(heLong*100)/100}°," 
      + f" szerokość sferyczna: {round(heLat*100)/100}°")

print("\nUkład walcowy:")
rWalec = (x*x + y*y) ** (1/2)
heLongWalec = (180 / math.pi) * math.atan(y/x)
print(f"r: {round(rWalec*100)/100}," 
      + f" θ: {round(heLongWalec*100)/100}°" 
      + f" z: {round(z*100)/100}")
