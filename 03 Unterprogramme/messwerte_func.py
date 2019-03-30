# Demonstration von Unterprogrammen

def get_user_input_bool(question:str) -> bool:
    while True: # beendet durch return
        user_input = input(question + " (J/N): ").upper()
        if user_input != "J" and user_input != "N":
            print("Fehler! Bitte j oder n eingeben.")
        else:
            return user_input == "J" # beendet das Unterprogramm und gibt den angegebene Wert zurück

new_row = True
while new_row:
    count: int = 0
    sum: float = 0.0
    new_value = True
    while new_value:
        value: float = float(input("Messwert: "))
        if value >= 0:
            count = count + 1
            sum = sum + value
        else:
            print("Falscher Wert!")

        new_value = get_user_input_bool("Weiterer Messwert? ")
    print("Anzahl: " + str(count))
    print("Summe: " + str(sum))
    print("Mittelwert: " + str(sum/count))

    new_row = get_user_input_bool("Weiteren Messreihe?")
