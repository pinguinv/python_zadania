# Napisz program, który wykasuje dowolną liczbę całkowitą
# od zera do 10 (do losowania liczb użyj np. funkcji randint
# z biblioteki random), a następnie prosi użytkownika o jej 
# zgadnięcie tak długo, aż ten poda poprawną wartość. 
# Gdy program działa, rozszerz go np. o podawanie 
# informacji za którym razem udało się zgadnąć lub 
# o wskazówki typu "Podana przez ciebie liczba jest 
# większa/mniejsza od wylosowanej"

import random

print("Zgadnij jaki numer został wylosowany!\n")
rand = random.randint(0,10)
ans = str(rand)
userAns = ""
ansCounter = 0
while(ans != userAns):
  ansCounter += 1
  userAns = input("Zgaduj:\n")
  if(userAns.isdigit()):
    if(int(userAns) > int(ans)):
      print("Mniej!\n")
    if(int(userAns) < int(ans)):
      print("Więcej!\n")


print(f"Brawo, poprawna odpowiedź to {ans}!")
print(f"Trafił*ś za {ansCounter} razem!")