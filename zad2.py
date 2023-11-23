# Napisz program proszący użytkownika o imię i tok urodzenia, 
# a następnie obliczający i wypisujący jego wiek.

from datetime import *

name = input("Podaj imię:\n")
yearOfBirth = input("Podaj rok urodzenia:\n")

if(yearOfBirth.isdigit() == False):  
  quit()

if(datetime.today().year < int(yearOfBirth)):
  quit()

age = datetime.today().year - int(yearOfBirth)

print(f"{name}, masz {age} lat.")