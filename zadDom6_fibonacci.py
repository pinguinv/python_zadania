# Wykorzystaj funkcję napisaną w zadaniu 19 w kodzie z 
# zadania 14 (ciąg Fibonacciego).

import time
import matplotlib.pyplot as plt

def czas_wykonania(f, *args):
  start = time.time()
  f(*args)
  end = time.time()
  return end - start

def fibonacciRecursion(n):
  if n <= 1:
      return n
  else:
      return(fibonacciRecursion(n-1) + fibonacciRecursion(n-2))

def fibonacciIteration(n):
  a = 0
  b = 1
  c = b
  while(n - 1 > 0):
    c = a + b
    a, b = b, c
    n -= 1
  return c

n = []
nIterTime = []
nRecuTime = []

for i in range(35):
  # print(i)
  n.append(i)

  timeIter = czas_wykonania(fibonacciIteration, i)
  nIterTime.append(timeIter)

  timeRecu = czas_wykonania(fibonacciRecursion, i)
  nRecuTime.append(timeRecu)

# print(n)
# print(nIterTime)
# print(nRecuTime)
plt.plot(n, nIterTime, label = "Iteration")
plt.plot(n, nRecuTime, label = "Recursion")
plt.xlabel("n")
plt.ylabel("Time [s]")
plt.legend()
plt.show()