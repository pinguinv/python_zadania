# Napisz program, który:
# - utworzy pustą listę i wypełni ją pięcioma liczbami
# losowymi z dowolnego zakresu np. [-1, 1]
# - wypisze po kolei wszystkie elementy listy wraz z 
# indeksami w następujący sposób:
# lista[0]: 0.1
# lista[1]: -0.92
# itd.
# - wypisze długość listy, czyli ilość jej elementów
# - znajdzie i wypisze największy element listy oraz 
# jego indeks

import random

lista = []

for i in range(5):
  lista.append(round(random.uniform(-1, 1)*100)/100)

largest = -10
largestId = 0
for i in range(len(lista)):
  print(f"lista[{i}]: {lista[i]}")
  if(lista[i] > largest):
    largestId = i
    largest = lista[i]
    

print(f"Długość listy: {len(lista)}")
print(f"Największa liczba to: {largest}, a jej indeks to: {largestId}")