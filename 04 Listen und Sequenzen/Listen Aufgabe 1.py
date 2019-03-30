#
# Aufgabe 1 aus dem Listen Tutorium
#
from typing import Any, List

# Aufgabe 1 a
def demo_prime_numbers():
    # Initialisierung
    primfaktoren = [2, 2, 3, 7]
    # Verarbeitung
    produkt = 1
    for element in primfaktoren:
        print(produkt * element, "=", produkt, "*", element)
        produkt = produkt * element
    # Ausgabe
    print("Primfaktoren:", primfaktoren)
    print('Zahl:', produkt)


def get_product(data: List[int]) -> int:
    """vereinfachte Lösung als Funktion"""
    product = 1
    for element in data:
        product = product * element
    return product


def run_demo_prime_numbers():
    demo_prime_numbers()


# Aufgabe 1 b
def count(search:Any, sequence: List[Any]):
    """
    Counts an item in a sequence and returns number of occasions.
    """
    counter = 0
    for element in sequence:
        if element == search:
            counter = counter + 1

    return counter

def run_demo_count():

    print(count("X", ["X", "Y", "X", "Z", "Z"]))
    print(count(2,[2,2,5,7]))
    print(count("o", "Hello World!"))

    mylist = ["X", "Y", "X", "Z", "Z"]
    mycount = mylist.count("X")
    print(mycount)


# Aufgabe 1 c

def get_product_exp(data: List[List[int]]) -> int:
    product = 1
    for element in data: # element ist List[int]
        product *= element[0] ** element[1]
    return product

def run_demo_get_product_ext():
    mylist = [[2, 2], [3, 1], [5, 0], [7, 1]]
    print(get_product_exp(mylist))


# Hauptprogramm
#run_demo_prime_numbers()
#run_demo_count()
run_demo_get_product_ext()