# Napisz program który wypisze pierwse N liczb naturalnych
# kolejności rosnącej i malejącej w osobnych kolumnach:
# 0 5
# 1 4
# 2 3
# 3 2
# 4 1
# 5 0

N = 6

for i in range(N):
  print(f"{i} {5 - i}")