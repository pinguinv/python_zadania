# Napisz program, który w pętli prosi o podanie liczby naturalnej
# i zapisuje każdą podaną liczbę do odpowiedniego pliku: parzyste 
# do even.txt, a nieparzyste do odd.txt.
# Program kończy się, gdy wpisane zostanie 0.
# Pliki powinny być zapisywane w nowym folderze, który zostanie 
# utworzony przy uruchomieniu programu (o ile jeszcze nie istnieje).
# Aby to zrobić, trzeba użyć modułu os. Przydatne funkcje:
# os.path.exists(nypath) - sprawdza, czy folder istnieje
# os.mkdir(nypath) - tworzy folder w zadanej ścieżce nypath
# os.getcwd() - aktualny katalog
# Uruchomienie programu po raz kolejny powinno powodować,
# że nowe liczby zostaną dopisane do istniejących plików
# lub zostaną utworzone nowe pliki.

import os

num = ""

if(not(os.path.exists(os.getcwd() + "\\numbers"))):
  os.mkdir(os.getcwd() + "\\numbers")

with open('numbers/even.txt', 'a') as even, open('numbers/odd.txt', 'a') as odd:

  while(num != 0):
    try:
      numIn = input("Podaj liczbę: ")
      num = int(numIn)
      
      if(num == 0):
        break

      if(num % 2):
        odd.write(str(num) + "\n")
      else:
        even.write(str(num) + "\n")

    except(ValueError):
      break
    except(TypeError):
      break