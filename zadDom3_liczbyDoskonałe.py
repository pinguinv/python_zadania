# Liczby doskonałe to takie, które są sumą swoich dzielników
# właściwych. Napisz program, który dla podanej liczby 
# naturalnej sprawdza, czy jest ona liczbą doskonałą.

num = input("Podaj liczbę, by sprawdzić czy jest doskonała:\n")

try:
  num = int(num)
  dividedNum = num
  dividers = []
  sumDividers = 0
  isPerfect = ""

  i = 1
  while(i <= round(dividedNum / 2)):
    # print(i)
    if(dividedNum % i == 0):
      dividers.append(i)
    i += 1

  for div in dividers:
    sumDividers += div

  isPerfect = "" if num == sumDividers else " nie"

  print(f"liczba: {num}, dzielniki: {dividers},\n" 
        + f"suma dzielników: {sumDividers},{isPerfect} jest doskonała")
except(ValueError):
  quit()