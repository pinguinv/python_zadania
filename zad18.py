# Napisz program, który dla zadanej listy par wypisze tą listę
# posortowaną według drugiego elementu, czyli np. dla listy
# zawierającej imiona i nazwiska kilku osób:
# ludzie = [("Jan", "Kowalski"), 
#           ("Grzegorz", "Brzęczyszczykiewicz"), 
#           ("Jacek", "Placek")]

people = [("Jan", "Kowalski"), 
          ("Grzegorz", "Brzęczyszczykiewicz"), 
          ("Jacek", "Placek")]

print(sorted(people, key = lambda x: x[1]))