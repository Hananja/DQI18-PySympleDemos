# hier wird die Nutzerinteraktion für die Verwendung von
# Alternativen bei der Datenbankansteuerung realisiert.
#
from enum import Enum


class InsertAlternatives(Enum):
    MULTI_INSERT = 1
    FOR_LOOP = 2
    EXECUTEMANY = 3

class FetchAlternatives(Enum):
    WHILE_LOOP = 1
    FOR_LOOP = 2

def input_alternative(AlternativesEnum):
    default_choice = 1
    while True: # Ausstieg durch return bei Erfolg
        # Ausgabe der Informationen
        print("Bitte auswählen:")
        for item in AlternativesEnum:
            print("(%d) %s" %(item.value, item.name))

        user_input = input("Auswahl [%d]: " % default_choice)
        try:
            # Auswertung der Eingabe
            if len(user_input) > 0:
                user_choice = int(user_input)
            else:
                user_choice = default_choice

            # richtiges Element heraussuchen
            for item in AlternativesEnum:
                if user_choice == item.value:
                    return item # Ausstieg
        except ValueError as e:
            pass # auch keine gültige Auswahl
        print("Keine gültige Auswahl!\n")


# Demo / Test Code
if __name__ == "__main__":
    print(input_alternative(InsertAlternatives))