total: float = 0.00
done: bool = False
while not done:
    art_no: str = input("Artikelnummer: ")
    count: int = int(input("Anzahl: "))
    price: float = float(input("Preis: "))
    total = total + count * price

    done = not input("weitere Eingabe?") == "J"

tax_rate: float = 0.19
tax: float = total * tax_rate
gross: float = total + tax

if gross < 50:
    shipping: float = 7.50
    print("Versandkosten: " + str(shipping))
    gross = gross + shipping

print("Endpreis: " + str(gross))
