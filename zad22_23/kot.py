class Kot:
  ulubioneZabawki = []
  nielubianeZabawki = []

  def __init__(self, imie):
    self.imie = imie

  def polubZabawke(self, zabawka: str):
    try:
      self.nielubianeZabawki.remove(zabawka)
    except(ValueError):
      pass
    self.ulubioneZabawki.append(zabawka)

  def przestanLubicZabawke(self, zabawka: str):
    try:
      self.ulubioneZabawki.remove(zabawka)
      self.nielubianeZabawki.append(zabawka)
    except(ValueError):
      pass

  def przywitanie(self):
    print(f"Cześć! Jestem {self.imie}!")

  def jakieUlubioneZabawki(self):
    print(f"Mam {len(self.ulubioneZabawki)} ulubionych zabawek, oto one:")
    for zabawka in self.ulubioneZabawki:
      print(zabawka)

  def jakieNielubianeZabawki(self):
    print(f"Mam {len(self.nielubianeZabawki)} nielubianych zabawek, oto one:")
    for zabawka in self.nielubianeZabawki:
      print(zabawka)