# Napisz program proszący użytkownika o podanie dwóch liczb a i b i wypisujący 
# ich sumę, różnicę, iloczyn, iloraz, pierwiastek z (a + b) oraz a^b i b^a

a = float(input("Podaj a:\n"))
b = float(input("Podaj b:\n"))

print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

if(b != 0):
  print(f"{a} / {b} = {a / b}")

print(f"pierwiastek z ({a} + {b}) = {round((a + b) ** (1/2) * 1000) / 1000}")
print(f"{a} ^ {b} = {a ** b}")
print(f"{b} ^ {a} = {b ** a}")