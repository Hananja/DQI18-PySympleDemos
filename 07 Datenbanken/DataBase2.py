# -*- coding: utf-8 -*-
# fme,wol,elo 2019-06-10

# Fallstudie: Ein Programm schreibt und liest Lager-Datensaetze
#   Daten in einer relationale Datenbank (abgebildet in lokaler Datei),
#   Kommunikation ueber eingebettete SQL-Strings
#   Datensaetze sind int, Dezimal und Zeichenkettenwerte

import time
import sqlite3 as sqlite

from alternative_management import input_alternative, InsertAlternatives, FetchAlternatives

VERSION = 'DataBase2 Version 2.1.20190610'

DBFILE = 'sqlite.db'
DROP = "DROP TABLE lager"
CREATE = """CREATE TABLE lager (
                                item_id        INTEGER PRIMARY KEY AUTOINCREMENT,
                                bezeichnung    VARCHAR(20),
                                anzahl         INTEGER,
                                preis          DECIMAL(6,2)
                               )"""
INSERT1 = "INSERT INTO lager VALUES (NULL,'Hemd','16', '34.20')"
INSERT2 = "INSERT INTO lager VALUES (NULL,'Hose','29', '52.60')"
INSERT3 = "INSERT INTO lager VALUES (NULL,'Mantel','36', '144.90')"
INSERT4 = "INSERT INTO lager VALUES (NULL,'Jacke','12', '39.10')"
SELECT  = "SELECT bezeichnung, anzahl, preis FROM lager"
UPDATE  = "UPDATE lager SET preis = preis * 1.10"

VALUES  = [
    ('Hemd'  , 13,  34.20  ), 
    ('Hose'  , 29,  52.60  ), 
    ('Mantel', 36,  144.90 ), 
    ('Jacke' , 12,  39.19  ),
]

# Steuerungsmöglichkeiten durch den Nutzer
print("Alternativen für die Eingabe:")
insertAlternative = input_alternative(InsertAlternatives)
print("\nAlternativen für die Ausgabe:")
fetchAlternative = input_alternative(FetchAlternatives)
print()

# das Hauptprogramm
print(VERSION, ', start um ', time.strftime('%Y-%m-%d %H:%M:%S'))

# Verbindung aufbauen (mit /with/ wie bei Dateien, damit sie automatisch geschlossen wird)
with sqlite.connect(DBFILE, isolation_level=None) as myconn:
    # Cursor für die Kommunikation erzeugen
    cursor = myconn.cursor()

    # Aufräumen
    try:
        cursor.execute(DROP)  # versuche Tabelle zu loeschen
    except sqlite.DatabaseError:
        pass # ignore

    cursor.execute(CREATE)  # Tabelle erzeugen

    if insertAlternative == InsertAlternatives.MULTI_INSERT:  # Alternative
        # Möglichkeit 1 sind 4 verschiedene Statements
        cursor.execute(INSERT1)  # 4 Eintraege vornehmen
        cursor.execute(INSERT2)
        cursor.execute(INSERT3)
        cursor.execute(INSERT4)

    if insertAlternative == InsertAlternatives.FOR_LOOP:  # Alternative
        # Möglichkeit 2 durch Tuple VALUES iterieren
        for value in VALUES:
            cursor.execute("INSERT INTO lager VALUES (NULL, ?, ?, ?)", value)

    if insertAlternative == InsertAlternatives.EXECUTEMANY: # Alternative
        # Möglichkeit 3 excecutemany
        cursor.executemany("INSERT INTO lager VALUES (NULL, ?, ?, ?)", VALUES)

    cursor.execute(SELECT)  # Datensaetze abfragen

    # Durch die Ergebnismenge iterieren ##################################
    if fetchAlternative == FetchAlternatives.WHILE_LOOP:  # Alternative
        # Möglichkeit 1 mit while Schleife
        while True: # siehe break
            satz = cursor.fetchone()  # eine Zeile aus der Ergebnismenge
            if satz is None: break # Schleife abbrechen
            for kette in satz:  # in Komponenten zerlegen
                print(kette, '\t  ', end=' ')  # KEIN Zeilenvorschub
            print()  # naechste Zeile, d.h. NUR Zeilenvorschub

    if fetchAlternative == FetchAlternatives.FOR_LOOP: # Alternative
        # Möglichkeit 2 mit Iterator
        for satz in cursor:  # Datensatzweise aus der Ergebnismenge
            for kette in satz:  # in Komponenten zerlegen
                print(kette, '\t  ', end=' ')  # KEIN Zeilenvorschub
            print()  # naechste Zeile, d.h. NUR Zeilenvorschub

    cursor.execute(UPDATE)  # Preise um 10 % anheben
    print()

    cursor.execute(SELECT)  # Datensaetze anzeigen
    while True:
        satz = cursor.fetchone()  # eine Zeile aus der Ergebnismenge
        if not satz: break
        for kette in satz:  # in Komponenten zerlegen
            print(kette, '\t  ', end=' ')  # KEIN Zeilenvorschub
        print()  # naechste Zeile, d.h. NUR Zeilenvorschub

    cursor.close()  # housekeeping (auch mit /with/ möglich)
    print(VERSION, ', beendet um ', time.strftime('%Y-%m-%d %H:%M:%S'))
