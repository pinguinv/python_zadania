import random as r
from projectConfig import GARDEN_SIZE, listOfFiles

for i in range(len(listOfFiles)):
  with open("finalProject/" + listOfFiles[i], "w") as file:
    howMany = 3
    # niech myszy będzie 2 razy więcej niż każdego rodzaju kotów
    if(listOfFiles[i] == "mice.txt"):
      howMany *= 2
    for j in range(howMany):
      file.write(f"{r.randint(0, GARDEN_SIZE[0])} {r.randint(0, GARDEN_SIZE[1])}\n")