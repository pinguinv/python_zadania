# Napisz program, który oblicza pole i obwód koła o promieniu
# podanym przez użytkownika. Wartość stałej pi weź 
# z biblioteki math. Promień nie może być ujemny. 
# W przypadku podania liczby ujemnej, program powinien 
# wypisywać komunikat informujący o błędnej wartości i 
# nic nie liczyć.

import math
r = input("Podaj promień:\n")

r = r.replace(",", ".")

if(not(r.isdigit()) 
    and (r[0] == '-'
    or r.find(".") == -1)):
  print("Nieprawidłowy promień")
  quit()

r = float(r)

pole = round(math.pi * r * r * 100) / 100
obw = round(2 * math.pi * r * 100) / 100

print(f"Pole: {pole}, obwód: {obw}")