# Napisz program, który prosi o podanie liczby naturalnej,
# a następnie wypisuje z ilu cyfr składa się wpisana
# wartość, a także informację o sumie tworzących ją cyfr.
# Dla uproszczenia załóż, że podana liczba jest poprawna
# (czyli rzeczywiście naturalna).

number = input("Podaj liczbę naturalną:\n")

if(not(number.isdigit())):
  print("To nie jest liczba naturalna")
  quit()

countOfDigits = len(number)
digits = [*number]
sumOfDigits = 0
for i in range(countOfDigits):
  sumOfDigits += int(digits[i])

print(f"Podana liczba składa się z {countOfDigits} cyfr," 
      + f" a ich suma wynosi {sumOfDigits}")