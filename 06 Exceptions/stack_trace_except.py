# Exceptions im Stack Trace
import sys


def get_filename():
    filename = input("Bitte Dateinamen eingeben: ")
    return filename

def open_file(filename):
    return open(filename, "r") # hier tritt FileNotFoundError auf

def read_lines():
    done = False
    while not done:
        try:
            with open_file(get_filename()) as infile:
                result = infile.readlines()
                done = True
                return result
        except FileNotFoundError as e: # und wird erst höher im Stack behandelt
            print("Fehler:", str(e))
            print("Noch einmal, bitte.")

try:
    print(read_lines())
except KeyboardInterrupt:
    print("Sie haben abgebrochen.")