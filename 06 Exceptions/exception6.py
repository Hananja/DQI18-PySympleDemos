# -*- coding: utf-8 -*-
# Exception 6


def message(msg):
  print(msg)

try:
  messager("Hello DQI!")
  f = open("gibtesnicht.txt", "r")
  f.readlines()
except: # besser NICHT ohne Fehlerangabe!
  print("Die Angegebene Datei existiert nicht")
