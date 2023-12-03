# Napisz funkcję, która mierzy czas wykonania innej funkcji
# za pomocą time tak, jak w przykładzie. Argumentami tej
# funkcji jest nazwa funkcji, którą chcemy wykonać oraz 
# wartości jej argumentów. Chodzi o to, by można było
# wykorzystać ją w następujący sposób:
# def czas wykonania...

# def f1(x):
#   ...
# def f2(x1, x2, x3):
#   ...
# t1 = czas_wykonania(f1, 2) mierzy czas wykonania f(2) 
# i przypisuje go do t1
# t2 = czas_wykonania(f2, 3, 4, 5) mierzy czas wykonania 
# f2(3, 4, 5) i przypisuje go do t2

import time

def czas_wykonania(f, *args):
  start = time.time()
  f(*args)
  end = time.time()
  return end - start