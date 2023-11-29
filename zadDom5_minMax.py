# Napisz funkcję, która dla zadanego argumentu (którym może być
# lista, krótka lub inna sekwencja) zwraca indeks i wartość
# najmniejszego elementu oraz indeks i wartość największego
# elementu. Następnie używając składni list comprehension
# utwórz kilkunastoelementową listę wypełnioną losowymi liczbami
# całkowitymi i przetestuj na niej swoją funkcję.
# W funkcji nie używać wbudowanych funkcji min i max.

import random

testList = []

for i in range(15):
  testList.append(random.randint(-10, 10))


def minAndMax(listArg: list):
  listMax = listArg[0]
  listMaxId = 0
  listMin = listArg[0]
  listMinId = 0

  for i in range(len(listArg)):
    if(listArg[i] > listMax):
      listMax = listArg[i]
      listMaxId = i
    if(listArg[i] < listMin):
      listMin = listArg[i]
      listMinId = i
    
  return {
    'listMax': listMax,
    'listMaxId': listMaxId,
    'listMin': listMin,
    'listMinId': listMinId,
  }

print(testList)
print(minAndMax(testList))