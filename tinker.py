# Nur zum ausprobieren


def myprint(*args, **kwargs):
    if not 'sep' in kwargs:
        kwargs['sep'] = ''
    return print(*args, **kwargs)


myprint("Test", 12, "ab")
myprint("Test", 12, "ab", sep="-")