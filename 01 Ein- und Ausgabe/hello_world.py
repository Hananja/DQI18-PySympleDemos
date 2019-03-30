# -*- coding: cp1252 -*-

# Eingabe
# -------
# Die Variable name wird angelegt
# mit dem Datentyp str (Zeichenkette)
# und der Wert zugewiesen, der von input(...)
# zurückgegeben wird.
# Die Funktion input(...) ließt eine Zeichenkette
# von der Konsole vom Nutzer ein und gibt diese zurück.
name : str = input("Bitte Name eingeben: ")

# Verarbeitung
# ------------
# Die Variable greeting wird angelegt mit dem Datentyp str
# und eine zusammengesetze Begrüßungsformel wird der
# Variable zugewiesen
greeting : str = "Hello " + name + "!" # + hängt Zeichenketten aneinander

# Ausgabe
# -------
# Die Funktion print(...) gibt den Inhalt
# der Variable greeting auf der Konsole aus
print(greeting)
