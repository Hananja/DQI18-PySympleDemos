# -*- coding: utf-8 -*-
# Exception 5


anzahl = "zwanzig"

try:
  for i in range(anzahl):
    print("Durchgang", i)
    f = open("gibtesnicht.txt", "r")
    f.readlines()
except IOError:
  print("Die Angegebene Datei existiert nicht")
except TypeError as e:
  print("TypeError:", str(e))
