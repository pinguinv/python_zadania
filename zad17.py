# Czy następujące programy są poprawne? Jeśli tak, to co wypiszą
# instrukcje print i dlaczego? Jeśli nie, to gdzie są błędy?
# 1. 
# t = (1, 2, 3, 4)
# t[0] = 8
# print(t)
# Błąd: 'tuple' object does not support item assignment 

# 2.
# t = (1, 2, 3, 4)
# t.append(5)
# print(t)
# Błąd: 'tuple' object has no attribute 'append'

# 3.
# t = "hehe"
# w = t*5
# print(w)
# Wypisze hehehehehehehehehehe (5 razy hehe)

# 4.
# t = {}
# print(type(t))
# Wypisze <class 'dict'>

# 5.
# t = {}
# t[i] = 10
# t[199] = 'c'
# print(t)
# Nie działa, i jest niezdefiniowane

# 6.
# a = [1, 2, 3]
# b = a
# b[2] = 10
# print(a)
# print(b)
# Wypisze 2 razy [1, 2, 10]

# 7.
# L = [1, 2, 3]
# for element in L:
#   element = 5
# print(L)
# Wypisze [1, 2, 3]

# 8.
# L = [1, 2, 3]
# for i in range(len(L)):
#   L[i] = 5
# print(L)
# Wypisze [5, 5, 5]

# 9. 
# if True:
#   x = 10
# print(x)
# Wypisze 10

# 10.
# for i in range(5):
#   pass
# print(i)
# Wypisze 4

# 11.
# def f():
#   print(a)
# a = 8
# f()
# Wypisze 8

# 12.
# def f():
#   a = 15
# a = 8
# f()
# print(a)
# Wypisze 8

# 13.
# def f():
#   global a
#   a = 15
# a = 8
# f()
# print(a)
# Wypisze 15

# 14.
# def f():
#   global a
#   a = 15
# a = 8
# print(a)
# Wypisze 8

# 15.
# def f(L1):
#   L1[0] = 15
# L = [1, 2, 3]
# f([4, 5, 6])
# print(L)
# Wypisze [1, 2, 3]

# 16.
# def f(L1):
#   L = L1
# L = [1, 2, 3]
# f([4, 5, 6])
# print(L)
# Wypisze [1, 2, 3]

# 17.
# def f(L1):
#   global L
#   L = L1
# L = [1, 2, 3]
# f([4, 5, 6])
# print(L)
# Wypisze [4, 5, 6]


# 18.
# def f(L1):
#   L = L1[:]
#   L[0] = 15
# L = [1, 2, 3]
# f([4, 5, 6])
# print(L)
# Wypisze [1, 2, 3]

# 19.
# def f(L1):
#   L = L1[:]
#   L[0] = 15
# L = (1, 2, 3)
# f((4, 5, 6))
# print(L)
# Błąd: 'tuple' object does not support item assignment 