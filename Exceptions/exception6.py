# -*- coding: utf-8 -*-
# Exception 6


def message(msg):
  print(msg)

try:
  messager("Hello TAI!")
  f = open("gibtesnicht.txt", "r")
  f.readlines()
except:
  print("Die Angegebene Datei existiert nicht")
