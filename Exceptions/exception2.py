# -*- coding: utf-8 -*-
# Exception 2

try:
  f = open("gibtesnicht.txt", "r")
  print(f.readlines())
except:
  print("Die Angegebene Datei existiert nicht")

# Prinzip:
# Tritt im try-Block eine Exception auf, so wird die Ausführung
# unterbrochen und der (passende) except-Block ausgeführt.
# Ein Rücksprung ist ohne Schleife nicht möglich.