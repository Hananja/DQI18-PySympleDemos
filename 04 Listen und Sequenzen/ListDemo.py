# Demo von Listen


# map ruft hier für jedes Element in der Sequenz
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# str(element) für das Element auf und
# liefert eine Liste der Ergebnisse zurück
# ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
l = list(map(str, range(10)))

# Join erzeugt eine Zeichenkette einer Sequenz, indem das davor angegebene
# Objekt dazwischen gehängt wird.
print("\n".join(l))