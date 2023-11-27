# Napisz funkcję, która zwraca sumę pierwszych N wyrazów 
# rozwinięcia exp w szereg Maclaurina. Wartości x i N niech
# będą argumentami funkcji. Możesz wykorzystać kod napisany
# w zadaniu 8. Zadaj wartość domyślną N wynoszącą 50. 
# Przetestuj działanie funkcji porównując wyniki z 
# obliczonymi przez exp z biblioteki math.

import math

def firstNofMaclaurins(x, N = 50):
  n = 0
  sumE = 0

  while(n < N):
    sumE += (x**n)/math.factorial(n)
    n += 1

  return sumE

x = input("Podaj x: ")
N = input("Podaj N: ")

try:
  x = x.replace(",", ".")
  x = float(x)

  N = N.replace(",", ".")
  N = float(N)

  sumE = firstNofMaclaurins(x, N)

  print(f"Suma wynosi: {sumE},\ne^{x} (e^x) = {math.exp(x)}")
  
except(ValueError):
  quit()