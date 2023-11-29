# Napisz funkcję, która dla dowolnej sekwencji podanej jako 
# argument, obliczy ile razy wystąpił w niej każdy z elementów
# i zwróci te dane jako wynik. Następnie wypisz liczbę wystąpień 
# każdego elementu na ekran zaczynając od elementu najmniejszego.
# Niezbędne sortowanie powinno się odbyć już poza funkcją.
# przykład: "abicddciecffghi"
# a : 1
# b : 1
# c : 3
# d : 2
# e : 1
# f : 2
# g : 1
# h : 1
# i : 3

def countElements(sequence: iter):
  elements = {}
  for i in range(len(sequence)):
    if(not(sequence[i] in elements)):
      elements[sequence[i]] = 1
    else:
      elements[sequence[i]] += 1

  return elements

testStr = "bbacccdddd1233214223"
testList = ['a', 'a', 'b', 'c', 'f']

countElementsRes = dict(sorted(countElements(testStr).items()))
print(dict(sorted(countElements(testList).items())))
print(countElementsRes)
for key in countElementsRes:
  print(key, ":", countElementsRes[key])