
# Read magic and with from gif file

with open("smiley.gif", "rb") as infile:
    magic = infile.read(4) # 4 Bytes lesen
    print(magic)
    print(type(magic), type("GIF8"))

    # Alternative 1
    if magic == "GIF8".encode("ascii"):
        print("Es ist ein GIF Bild.")
    else:
        print("Es ist kein GIF Bild.")

    # Alternative 2
    # ACHTUNG: schlägt fehl, wenn kein ASCII gelesen wurde
    if magic.decode("ascii") == "GIF8":
        print("Es ist ein GIF Bild.")
    else:
        print("Es ist kein GIF Bild.")

    # Alternative 3
    if magic == b"GIF8":
        print("Es ist ein GIF Bild.")
    else:
        print("Es ist kein GIF Bild.")

    # Breite auslesen
    infile.seek(6) # Lesecursor auf Zeichen Nr. 6
    width_data = infile.read(2) # 2 Bytes lesen
    width = width_data[0] + 256 * width_data[1]
    print("Breite:", width)

    # Höhe auslesen
    height_data = infile.read(2) # 2 Bytes lesen
    height = height_data[0] + 256 * height_data[1]
    print("Höhe:", height)
