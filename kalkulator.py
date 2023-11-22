# Kalkulator

options = {
  '1': "dodawanie",
  '2': "odejmowanie",
  '3': "mnożenie",
  '4': "dzielenie",
  '5': "potęgowanie",
  '6': "pierwiastkowanie"
}

def checkIfNumber(arg):
  try:
    arg = arg.replace(",", ".")
    arg = float(arg)
  except(ValueError):
    print("Błędne dane wejściowe")
    quit()
  return float(arg)

def checkBInRoot(arg, bInRoot):
  bInRoot = checkIfNumber(bInRoot)
  if(arg < 0 and bInRoot % 2 == 0):
    print("Nie można wyciągnąć parzystego pierwiastka z ujemnej liczby")
    quit()
  return bInRoot

def checkBInPow(arg, bInPow):
  bInPow = checkIfNumber(bInPow)
  print((1/bInPow))
  if(arg < 0 and (1/bInPow) % 2 == 0):
    print("Nie można wyciągnąć parzystego pierwiastka z ujemnej liczby")
    quit()
  return bInPow

print("Wybierz działanie:\n")
for key in options:
  print(f"{key}. {options[key]}")

opt = input("\n")
if(not(options.get(opt))):
  quit()

print(options.get(opt))

a = b = 0

match(opt):
  case '1'|'2'|'3'|'4':
    a = input("Podaj a: ")
    a = checkIfNumber(a)

    b = input("Podaj b: ")
    b = checkIfNumber(b)

    match(opt):
      case '1':
        print(f"{a} + {b} = {a + (b)}")
      case '2':
        print(f"{a} - {b} = {a - (b)}")
      case '3':
        print(f"{a} * {b} = {(round(a * (b) * 100))/100}")
      case '4':
        if(b == 0):
          print("Nie można dzielić przez 0")
          quit()
        print(f"{a} / {b} = {(round(a / (b) * 100))/100}")
  case '5':    
    a = input("Podaj podstawę potęgi: ")
    a = checkIfNumber(a)

    b = input("Podaj wykładnik potęgi: ")
    b = checkBInPow(a, b)

    printNegative = False

    if(a < 0):
      a = -a
      printNegative = True

    printMinus = "-" if printNegative else ""

    print(f"{printMinus}{a} ^ {b} = {printMinus}{(round(a ** (b) * 100))/100}")
  case '6':
    a = input("Podaj liczbę z której chcesz wyciągnąć pierwiastek: ")
    a = checkIfNumber(a)

    b = input("Podaj stopień pierwiastka: ")
    b = checkBInRoot(a, b)

    printNegative = False

    if(a < 0):
      a = -a
      printNegative = True

    printMinus = "-" if printNegative else ""

    print(f"Pierwiastek {b} stopnia z {printMinus}{a} = " +
          f"{printMinus}{(round(a ** (1/(b)) * 100))/100}")