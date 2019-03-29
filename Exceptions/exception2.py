# -*- coding: utf-8 -*-
# Exception 2

try:
  f = open("gibtesnicht.txt", "r")
  print(f.readlines())
except:
  print("Die Angegebene Datei existiert nicht")
