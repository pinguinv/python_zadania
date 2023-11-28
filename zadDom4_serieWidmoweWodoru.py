# Serie widmowe wodoru dane są poniższym wzorem
# 1/PhotonsLength = R(1/n1**2 - 1/n2**2)
# gdzie:
# n1, n2 - numery orbitali, między którymi następuje
# przejście, n1 < n2
# R = 0.0109737nm^-1 - stała Rydberga
# Napisz program, który wypisze długości fali kilku serii 
# widmowych wodoru np. w taki sposób:
# Linie widmowe dla n1 = 1:
# n2 = 2 : lambda = 122 nm
# n2 = 3 : lambda = 103 nm
# n2 = 4 : lambda = 97 nm
# itd.
# W swoim programie zawrzyj funkcję, która oblicza długość
# fotonu dla zadanego n1 i n2. 

import math

def calcPhotonsLength(n1, n2):
  R = 0.0109737
  if(n1 < n2):
    photonsLength = 1/(R * (1/(n1**2) - 1/(n2**2)))
    return round(photonsLength)
  else:
    print("Nieprawidłowe dane")
    return 0
  
def printPhotonsLengths(n1Max, howManyLengthsForEach):
  n1 = 1
  while(n1 <= n1Max):
    print(f"Linie widmowe dla n1 = {n1}:")
    for i in range(howManyLengthsForEach):
      n2 = n1 + i + 1
      pLen = calcPhotonsLength(n1, n2)
      print(f"  n2 = {n2}: lambda = {pLen} nm")
    n1 += 1
  
nMax = input("Podaj maksymalne n1 (numery orbitali): ")
howMany = input("Podaj ile długości wypisać dla każdej serii: ")

try:
  nMax = nMax.replace(",", ".")
  nMax = int(nMax)

  howMany = howMany.replace(",", ".")
  howMany = int(howMany)
  printPhotonsLengths(nMax, howMany)
except(ValueError):
  quit()
