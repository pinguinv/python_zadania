# Liczby Catalana to ciąg, który można wyrazić wzorem 
# rekurencyjnym: C0 = 1, Cn+1 = Cn*(4n+2)/(n+2)
# Napisz program, który wypisuje wszystkie liczby 
# Catalana mniejsze od miliona i podaje, ile jest 
# wśród nich liczb parzystych i nieparzystych. Uwaga 
# na kolejność instrukcji w pętli - może mieć znaczenie!

cCurrent = int(1)
cNext = int(0)
cN = int(0)
even = 0
odd = 0

print(f"n: Cn")
while(cCurrent < 1000000):
  print(f"{cN}: {int(cCurrent)}")
  if(cCurrent % 2 == 0):
    even += 1
  else:
    odd += 1
  cNext = ((4*cN + 2)/(cN + 2)) * cCurrent
  cCurrent = cNext
  cN += 1

print(f"Parzystych: {even}, nieparzystych: {odd}")