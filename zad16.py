# Utwórz dwa zbiory i wypełnij je kilkoma losowymi liczbami
# całkowitymi z dowolnego przedziału, np. od 1 do 10 (przedział
# nie powinien być zbyt szeroki, żeby zbiory mogły mieć jakąś
# część wspólną). Następnie wypisz ich: sumę, różnicę i część
# wspólną, a także te elementy, które pojawiają się tylko w
# jednym z nich.

import random

set1, set2 = set(), set()

for i in range(5):
  set1.add(random.randint(1, 10))
  set2.add(random.randint(1, 10))

def sumOfSets(set1: set, set2: set):
  return set1.union(set2)

def setsDiff(set1: set, set2: set): 
  return set1.difference(set2)

def setsIntersection(set1: set, set2: set):
  return set1.intersection(set2)

print(f"Zbiór A: {set1}")
print(f"Zbiór B: {set2}")
print(f"Suma zbiorów: {sumOfSets(set1, set2)}")
print(f"Symetryczna różnica zbiorów: {set1.symmetric_difference(set2)}")
print(f"Różnica zbiorów A\B: {setsDiff(set1, set2)}")
print(f"Różnica zbiorów B\A: {setsDiff(set2, set1)}")
print(f"Część wspólna zbiorów: {setsIntersection(set1, set2)}")
