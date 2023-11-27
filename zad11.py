# Napisz funkcję, która przyjmuje wartość temperatury w 
# Kelvinach i zwraca wartość wyrażoną w stopniach Celsjusza:
# Tc: Tk - 273.15. W przypadku podania wartości ujemnej
# funkcja zwraca None. Przetestuj jej działanie.

def kelvinsToCelsiusDegrees(kelviny):
  try:
    kelviny = kelviny.replace(",", ".")

    kelviny = float(kelviny)

    if(kelviny < 0):
      print("Temperatura w kelvinach nie może być ujemna!")
      return None

    celc = round((kelviny - 273.15) * 100) / 100

    return celc

  except(ValueError):
    quit()

kelviny = input("Podaj temperaturę w kelwinach:\n")

print(f"Temperatura w stopniach Celsjusza wynosi: " 
      + f"{kelvinsToCelsiusDegrees(kelviny)}")