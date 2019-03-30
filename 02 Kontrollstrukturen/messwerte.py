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

        user_input = input("Weiterer Messwert? ")
        new_value = user_input == "j" or user_input == "J"
    print("Anzahl: " + str(count))
    print("Summe: " + str(sum))
    print("Mittelwert: " + str(sum/count))

    user_input = input("Weiteren Messreihe?")
    new_row = user_input == "j" or user_input == "J"
