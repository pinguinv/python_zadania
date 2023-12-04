# Napisz program, który uruchomiony z terminala poleceniem 
# python3 program.py plik1.txt plik2.txt plik3.txt wypisze 
# zawartość plików plik1.txt, plik2.txt, plik3.txt, a jeśli 
# któregoś z nich nie da się otworzyć, wypisze odpowiednią 
# informację.

for i in range(3):
  try:
    plik = open(f".\zad26\plik{i+1}.txt", "r")
    linie = plik.readlines()
    print(f"plik{i+1}:")
    print(linie)
  except(FileNotFoundError):
    print(f"Nie da się otworzyć pliku: plik{i+1}.txt")
    pass