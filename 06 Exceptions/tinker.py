# just a test


def f1():
    print("f1")
    return f2()

def f2():
    print("f2")
    return f1()

f1()
