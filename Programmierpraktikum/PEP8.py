# Demo für PEP8


import random


def my_random(max_value: int)->int:
    return random.randint(0, max_value)


print(my_random(10))
