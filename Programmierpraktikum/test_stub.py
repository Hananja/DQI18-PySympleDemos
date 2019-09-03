# Beispiel für eine Stubfunktion

def f(p):
    data = [(1,2,3), (4,5,6), (7,8,9)]
    if "index" not in f.__dict__: f.index = -1
    f.index += 1
    return data[f.index]

print(f(1))
print(f(1))
print(f(1))