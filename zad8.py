# Napisz program, który obliczy sumę pierwszych N wyrazów 
# rozwinięcia w szereg Maclaurina funkcji e^x dla x zadanego
# przez użytkownika. Porównaj wynik z wartością obliczoną 
# przez funkcję exp z biblioteki math. Poeksperymentuj z 
# różnymi wartościami N, np. 5, 10, 15.

import math

N = 5
print(f"N = {N}")

x = input("Podaj x: ")

try:
  x = x.replace(",", ".")
  x = float(x)

  n = 0
  sumE = 0

  while(n < N):
    sumE += (x**n)/math.factorial(n)
    n += 1

  print(f"Suma wynosi: {sumE},\ne^{x} (e^x) = {math.exp(x)}")
except(ValueError):
  quit()

# if(not(x.isdigit())):
#   print("Nieprawidłowy x")
#   quit()

# x = float(x)


# 0.2(5) =>  0.255555555
# 0.4(12) => 0.412121212

# x % 6 = 4 => (1) * 6 + 4 = 10
# kolejne czyli y = 11 lub y = 9
# x > y => y = 9
# 3(x + y) = 3(10 + 9) = 3 * 19 = 57

