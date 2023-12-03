# Napisz program, który wczyta pliki utworzone w poprzednim
# zadaniu i obliczy sumę oraz średnią arytmetyczną liczb
# znajdujących się w każdym z nich.

import os

def getNumbers(file):
  lines = file.readlines()
  for i in range(len(lines)):
    try:
      lines[i] = int(lines[i].replace("\n", ""))
    except(ValueError):
      print("Błąd w pliku")
      quit()
  return lines

num = ""

if(not(os.path.exists(os.getcwd() + "\\numbers"))):
  print("Folder 'numbers' nie istnieje w tej lokalizacji.")

evenSum = 0
oddSum = 0

evenNums = []
oddNums = []

with open('numbers/even.txt', 'r') as even, open('numbers/odd.txt', 'r') as odd:
  evenNums = getNumbers(even)
  oddNums = getNumbers(odd)

for i in evenNums:
  evenSum += i

for i in oddNums:
  oddSum += i

print(f"Parzyste:\nSuma: {evenSum}, Średnia: {evenSum/len(evenNums)}")
print(f"Nieparzyste:\nSuma: {oddSum}, Średnia: {oddSum/len(oddNums)}")