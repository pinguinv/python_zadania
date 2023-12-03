# Napisz i przetestuj klasę reprezentującą kota (lub 
# jakiekolwiek zwierzę). Rozwiązanie zapisz w pliku kot.py. 
# Każdy kot ma: imię, swoje ulubione zabawki, zabawki, 
# których nie znosi,
# a ponadto potrafi:
# przywitać się i przedstawić,
# powiedzieć, jakie są jego ulubione/nielubiane zabawki
# i ile ich jest,
# polubić napotkaną zabawkę,
# obrazić się na jakąś zabawkę, którą dotąd lubił
# Kot może polubić zupełnie nową zabawkę, ale może też nagle
# się na którąś 'odobrazić' i zabawka z nielubianej stanie
# się lubianą. Może też być odwrotnie: nagle przestanie mu się
# podobać jedna z tych, które dotąd lubił. Do nowo napotkanych
# zabawek podchodzi z ufnością, czyli może je polubić, ale
# nie ma tak, że zobaczy i od razu nie znosi.
# Uwaga: Na liście lubianych i nielubianych zabawek żaden 
# element nie pojawia się jednocześnie.

from kot import Kot

kot = Kot("Puszek")

kot.przywitanie()

kot.przestanLubicZabawke("Drapacz")

kot.polubZabawke("Piłka")
kot.przestanLubicZabawke("Piłka")
kot.polubZabawke("Piłka")

kot.polubZabawke("Laser")
kot.przestanLubicZabawke("Laser")


kot.jakieUlubioneZabawki()
kot.jakieNielubianeZabawki()
