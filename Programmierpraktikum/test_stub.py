# Beispiel für eine Stubfunktion
#
# Eine Funktion liefert zum Test Dummydaten zurück, die sich von Aufruf zu Aufruf verändern.

def f(p):
    data = [(1,2,3), (4,5,6), (7,8,9)]
    if "index" not in f.__dict__: f.index = -1
    f.index += 1
    return data[f.index]

# Alternative Implementierung
def g(p):
    data = [(1,2,3), (4,5,6), (7,8,9), (10, 11, 12)]
    try:
        g.index += 1            # next element
        g.index %= len(data)    # wrap around
    except AttributeError as e:
        g.index = 0             # first element
    return data[g.index]

print(f(1))
print(f(1))
print(f(1))

print("---".center(10))

print(g(1))
print(g(1))
print(g(1))
print(g(1))
print(g(1))
print(g(1))
