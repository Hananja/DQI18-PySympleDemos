# -*- coding: utf-8 -*-
# Exception 7


def message(msg):
  print(msg)

try:
  messager("Hello DQI!")
  f = open("gibtesnicht.txt", "r")
  f.readlines()
except OSError as e: # Variable e enthält das Exception Objekt
  print("Datei nicht lesbar:", str(e))
  print("Fehlernummer", e.errno)
  print("Dateiname:", e.filename)
