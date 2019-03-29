# -*- coding: utf-8 -*-
# Exception 4


anzahl = "zwanzig"

try:
  for i in range(anzahl):
    print("Durchgang", i)
    f = open("gibtesnicht.txt", "r")
    f.readlines()
except:
  print("Die Angegebene Datei existiert nicht")

# Fehlerkategorien:
# Zeilen 5 und 8: Programmierfehler (zur Programmierzeit behebbar)
# Zeile 10: Laufzeitfehler    (nicht zur Programmierzeit behebbar)