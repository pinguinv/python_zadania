# Napisz dwie funkcje obliczające silnię liczby podanej
# jako argument: w sposób iteracyjny i rekurencyjny.
# Przetestuj ich działanie. Możesz porównać wynik z wynikiem
# obliczonym przez funkcję factorial z biblioteki math.

def factorialIteration(num):
  result = 1
  while(num > 0):
    result *= num
    num -= 1
  return result

def factorialRecursion(num):
  if(num > 0):
    return num * factorialIteration(num - 1)
  else: 
    return 1
  
print(factorialIteration(6))
print(factorialRecursion(6))