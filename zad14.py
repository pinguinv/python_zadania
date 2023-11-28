# Napisz dwie funkcje zwracające n-ty wyraz ciągu 
# Fibonacciego. Pierwsza powinna obliczać go iteracyjnie,
# a druga rekurencyjnie. Następnie korzystając z modułu
# time porównaj czas działania obu funkcji w zależności
# od wartości n (n od zera do ok. 30 - 40) i przedstaw je
# na wykresie.

import time
import matplotlib.pyplot as plt

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

  startTimeIter = time.time()
  fibonacciIteration(i)
  endTimeIter = time.time()
  timeIter = endTimeIter-startTimeIter
  nIterTime.append(timeIter)

  startTimeRecu = time.time()
  fibonacciRecursion(i)
  endTimeRecu = time.time()
  timeRecu = endTimeRecu-startTimeRecu
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