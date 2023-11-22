# Obliczanie przybliżonej wartości PI metodą Monte Carlo

import random
import time

r = input("Podaj promień koła: ")
pointsNum = input("Podaj liczbę punktów do wylosowania: ")

try: 
  r = float(r)
  pointsNum = int(pointsNum)
  points = []
  countOfPointsIn = 0
  countOfPointsOut = 0

  for i in range(pointsNum):
    x = random.random() * 2 * r
    y = random.random() * 2 * r
    points.append({'x': x, 'y': y})
  
  start = time.time()
  for i in range(pointsNum):
    if((points[i]['x'] - r) ** 2 + (points[i]['y'] - r) ** 2 <= r ** 2):
      # points[i]['inCircle'] = True
      countOfPointsIn += 1
    else:
      countOfPointsOut += 1
  pi = countOfPointsIn/countOfPointsOut
  end = time.time()
  print(f"Punkty wewnątrz koła: {countOfPointsIn}\n" 
        + f"Punkty na zewnątrz koła: {countOfPointsOut}\n" 
        + f"Przybliżenie PI: {pi}\n"
        + f"Trwało to {round((end - start) * 100)/100} s")

except(ValueError):
  quit()
