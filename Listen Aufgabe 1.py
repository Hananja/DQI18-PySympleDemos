#
# Aufgabe 1 aus dem Listen Tutorium
#
from typing import Any, List


def count(search:Any, sequence: List[Any]):
    """
    Counts an item in a sequence and returns number of occasions.
    """
    counter = 0
    for element in sequence:
        if element == search:
            counter = counter + 1

    return counter


print(count("X", ["X", "Y", "X", "Z", "Z"]))
print(count(2,[2,2,5,7]))
print(count("o", "Hello World!"))
