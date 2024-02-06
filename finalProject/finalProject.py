# W dużym kwadratowym ogrodzie żyje gromadka kotów i sporo myszy. Od rana
# koty uganiają się za myszami i wydeptują ścieżki. Czasem kot i mysz mogą
# spotkać się w jednym miejscu. Jak kończy się taka sytuacja? To zależy 
# (opis możliwych scenariuszy poniżej). Wieczorem na trawie widać ścieżki 
# wydeptane przez zwierzęta. Na początku symulacji umieszczamy koty i myszy
# w ogródku. Lista położeń początkowych (czyli położeń kocich pudełek/mysich
# norek) wszystkich kotów i myszy wczytywana jest z plików, których opis 
# znajduje się nieco dalej. Na jej podstawie należy stworzyć wszystkie
# obiekty reprezentujące zwierzęta.
# W ciągu dnia zarówno koty, jak i myszy poruszają się po ogrodzie, każdy 
# na swój sposób:
# - Myszy są małe, więc robią małe kroczki. W jednym momencie mogą co 
# najwyżej zmienić swoją pozycję (x, y) o 1 (lub nie zmienić wcale)
# w każdym kierunku. Wyjątek stanowi ucieczka, wtedy mysz nabiera supermocy
# i teleportuje się do swojego schronienia, niezależnie jak to daleko.
# - Koty Przeciętniaki oraz Koty Leniuchy poruszają się w losowym kierunku
# zmieniając położenie o co najwyżej 10, zarówno w kierunku x jak i y.
# - Kociaki poruszają się w losowym kierunku, zmieniają swoją pozycję 
# (każdą współrzędną) o co najwyżej 5, ale nigdy nie oddalają się od swojego
# domu o odległość większą niż 100. Jeśli nowe położenie sprawiłoby, że 
# kociak oddali się od domu o ponad 100, to zamiast tego wraca do 
# poprzedniego położenia.

# Uwaga: Każdy zwierzak pamięta wszystkie swoje położenia. Jeśli mysz 
# znajdzie się w odległości mniejszej niż 4 od kota, to następuje ich 
# spotkanie. Spotkanie kota i myszy może przebiegać różnie:

# - Koty Przeciętniaki, których jest najwięcej, po prostu zawsze trącają 
# mysz łapką, ona teleportuje się do swojego domku, a kot jest zadowolony.

# - Kociaki są bardzo młode i praktycznie zawsze boją się myszy, a gdy ją 
# spotkają, natychmiast teleportują się do swojego pudła. Mysz nadal normalnie
# spaceruje sobie po ogródku. Jednak jeżeli jakimś cudem spotkają mysz w 
# pobliżu swojego pudełka (w promieniu 50), wtedy stają się odważne i potrafią
# przestraszyć gryzonia na tyle, że tym razem to on teleportuje się natychmiast
# do swojej kryjówki.

# - Koty Leniuchy są względnie niegroźne. Gdy spotkają mysz, nawet w swoim
# mieszkaniu, często zupełnie się nią nie przejmują i po spotkaniu każde z 
# nich idzie w swoją stronę jak gdyby nic się nie stało. Czasem jednak kot
# trąca mysz łapką, ta ucieka (teleportuje się) do kryjówki, a kot jest 
# zadowolony, że pogonił gryzonia. To, czy kot jest akurat zainteresowany 
# myszą, jest losowe. Zależy jednak od liczby przegonionych już myszy.
# Im jest ich więcej, tym kotu jednak bardziej się chce. Prawdopodobieństwo
# zainteresowania wynosi 1/(1+e^(-0.1n)), gdzie n to liczba dotychczas
# pogonionych myszy.

# Cały dzień trwa kilkaset iteracji, a cała symulacja to jeden dzień.
# Po zakończeniu symulacji chcemy zobaczyć wszystkie ścieżki wydeptane
# w trawie przez koty i myszy.
# Pliki z danymi. Za pomocą dowolnego programu (lub ręcznie) należy stworzyć 
# plik tekstowy, który w każdej linijce zawiera dwie liczby oddzielone 
# spacją - położenia początkowe x i y jednego zwierzaka. Dane dla każdego
# typu zwierząt powinny znaleźć się w osobnym pliku 
# (3 typy kotów + myszy = 4 pliki). Położenia powinny być liczbami całkowitymi
# nieujemnymi, żaden zwierzak nie powinien też znajdować się poza ogrodem.
# Należy stworzyć po kilka zwierząt każdego typu.
# Po zakończeniu symulacji chcemy zobaczyć ścieżki wydeptane przez wszystkie
# zwierzęta. Jako że każde zwierzę pamięta wszystkie swoje położenia, 
# wystarczy narysować wykres przedstawiający kolejno połączone punkty.
# Można to zrobić używając Matplotlib i polecenia plot.


import matplotlib.pyplot as plt
import random as r
import math
from projectConfig import GARDEN_SIZE, listOfFiles

class Animal:

  def __init__(self, name, startX, startY):
    self.myListOfXs = []
    self.myListOfYs = []
    self.myCurrentPosition = (0, 0)

    self.myName = name
    self.myStartPoint = (startX, startY)
    self.addToListOfPositions(self.myStartPoint)
    self.myCurrentPosition = self.myStartPoint

  def go(self):
    pass

    # Sprawdzenie czy byłboby poza ogrodem
  def canGoLikeThis(self, myNextPosition):
    if(myNextPosition[0] > GARDEN_SIZE[0] 
       or myNextPosition[0] < 0 
       or myNextPosition[1] > GARDEN_SIZE[1] 
       or myNextPosition[1] < 0):
      # Jeśli chce wyjść poza ogród
      return False
    return True

  def run(self):
    self.myCurrentPosition = self.myStartPoint
    self.addToListOfPositions(self.myCurrentPosition)
    print(f"{self.myName} ran away")

  def addToListOfPositions(self, myNextPosition):
    self.myCurrentPosition = myNextPosition
    self.myListOfXs.append(self.myCurrentPosition[0])
    self.myListOfYs.append(self.myCurrentPosition[1])

class MidCat(Animal):
  def go(self):
    super()
    myNextPosition = (self.myCurrentPosition[0] + r.randint(-10, 10),
                      self.myCurrentPosition[1] + r.randint(-10, 10))
    if(self.canGoLikeThis(myNextPosition)):
      self.addToListOfPositions(myNextPosition)

class LazyCat(Animal):
  def __init__(self, name, startX, startY):
    super().__init__(name, startX, startY)
    self.scaredMiceCount = 0

  def go(self):
    super()
    myNextPosition = (self.myCurrentPosition[0] + r.randint(-10, 10),
                      self.myCurrentPosition[1] + r.randint(-10, 10))
    if(self.canGoLikeThis(myNextPosition)):
      self.addToListOfPositions(myNextPosition)

  def scaredMice(self):
    self.scaredMiceCount += 1

class Kitty(Animal):
  def go(self):
    super()
    myNextPosition = (self.myCurrentPosition[0] + r.randint(-5, 5),
                      self.myCurrentPosition[1] + r.randint(-5, 5))
    # czy oddali się na więcej niż 100 od domu
    nextDistanceFromHome = ((myNextPosition[0] - self.myListOfXs[0])**2 
    + (myNextPosition[1] - self.myListOfYs[0])**2)**(1/2)
    if(self.canGoLikeThis(myNextPosition) and nextDistanceFromHome <= 100):
      self.addToListOfPositions(myNextPosition)

class Mouse(Animal):
  def go(self):
    super()
    myNextPosition = (self.myCurrentPosition[0] + r.randint(-1, 1),
                      self.myCurrentPosition[1] + r.randint(-1, 1))
    if(self.canGoLikeThis(myNextPosition)):
      self.addToListOfPositions(myNextPosition)

def checkIfAnimalsHaveMet(animal1, animal2):
  pos1 = animal1.myCurrentPosition
  pos2 = animal2.myCurrentPosition
  x1, y1 = pos1[0], pos1[1]
  x2, y2 = pos2[0], pos2[1]
  distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
  # spotkanie dwóch zwierząt
  if(distance < 4):
    # nie zostawiać tylko sprawdzić jeszcze drugą opcję
    twoAnimals = [animal1, animal2]
    checkMouse(twoAnimals[0], twoAnimals[1])
    checkMouse(twoAnimals[1], twoAnimals[0])


def checkMouse(animal1, animal2):
    # jeśli z jakiegoś powodu nie będzie działać tak jak jest teraz, 
    # to trzeba będzie w ten sposób spróbować
    # if(type(animal1) == MidCat and type(animal2) == Mouse):
    #   animal2.run()
    # if(type(animal1) == Kitty and type(animal1 == Mouse)): ...
  if(type(animal1) == Mouse):
    if(type(animal2) == MidCat):
      animal1.run()
    if(type(animal2) == Kitty):
      kittysDistanceFromHome = ((animal2.myCurrentPosition[0] - animal2.myListOfXs[0])**2 
      + (animal2.myCurrentPosition[1] - animal2.myListOfYs[0])**2)**(1/2)
      # jeśli dystans od domu jest większy niż 50 i kociak spotka mysz - ucieka kociak
      if(kittysDistanceFromHome >= 50):
        animal2.run()
      # jeśli dystans od domu jest mniejszy niż 50 i kociak spotka mysz - ucieka mysz
      else:
        animal1.run()
    if(type(animal2) == LazyCat):
      # Prawdopodobieństwo zainteresowania wynosi 1/(1+e^(-0.1n)), 
      # gdzie n to liczba dotychczas pogonionych myszy.
      # pomysł: lista m-elementowa, gdzie m to 1/probability,
      # wypełniona wartościami "False"/zerami,
      # na losowym indeksie wstawić "True"/jedynkę,
      # losować indeks tablicy i sprawdzić czy pod tym indeksem jest
      # "True"/jedynka

      # prostszy i szybszy sposób (chyba)
      probability = 1/(1+math.exp(-0.1 * animal2.scaredMiceCount))
      chance = r.random()
      if(chance < probability):
        animal1.run()
        animal2.scaredMice()

animalsLinesDict = {}

# Odczytanie z plików współrzędnych początkowych wszystkich zwierząt 
# i przypisanie do odpowiednich kluczy w słowniku
for fileName in listOfFiles:
  with open(fileName, "r") as file:
    animalsLinesDict[f"{fileName[:-4]}Lines"] = file.readlines()
# print(animalsLinesDict)

# Zamiana w słowniku z tekstu na współrzędne 
for animal in animalsLinesDict:
  for i in range(len(animalsLinesDict[animal])):
    line = animalsLinesDict[animal][i].split()
    for j in range(len(line)):
      line[j] = int(line[j])
    animalsLinesDict[animal][i] = line
  # print(animalsLinesDict[animal])
# print(animalsLinesDict)

allAnimalsList = []

for key in animalsLinesDict:
  # print(key[:-5])
  for i in range(len(animalsLinesDict[key])):
    name = f"{key[:-5]} {i}"
    match(key[:-5]):
      case "kittens":
        allAnimalsList.append(Kitty(name, animalsLinesDict[key][i][0], animalsLinesDict[key][i][1]))
      case "lazyCats":
        allAnimalsList.append(LazyCat(name, animalsLinesDict[key][i][0], animalsLinesDict[key][i][1]))
      case "mice":
        allAnimalsList.append(Mouse(name, animalsLinesDict[key][i][0], animalsLinesDict[key][i][1]))
      case "midCats":
        allAnimalsList.append(MidCat(name, animalsLinesDict[key][i][0], animalsLinesDict[key][i][1]))
    # print(animalsLinesDict[key][i])

for i in range(100):
  for j in allAnimalsList:
    j.go()
    # sprawdzić czy mysz spotkała kota itd
  for j in range(len(allAnimalsList)):
    for k in range(len(allAnimalsList) - (j+1)):
      # porównanie każdego z każdym, bez powtórzeń
      # print(j, j + k + 1)
      checkIfAnimalsHaveMet(allAnimalsList[j], allAnimalsList[j + k + 1])

axes = plt.gca()
axes.set_xlim([0, GARDEN_SIZE[0]])
axes.set_ylim([0, GARDEN_SIZE[1]])

# for animal in allAnimalsList:
#   plt.plot(animal.myListOfXs, animal.myListOfYs, label = animal.myName)

for i in range(len(allAnimalsList)):
  animal = allAnimalsList[i]
  # print(animal.myListOfXs)
  # print(len(animal.myListOfXs))
  plt.plot(animal.myListOfXs, animal.myListOfYs, 'o', 
           ls='-', label = animal.myName, markevery=[0])

# Shrink current axis by 20%
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.grid()
plt.show()