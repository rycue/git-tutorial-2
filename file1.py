import random

def foo():
    """This function does something"""
    x = random.randint(0, 10)
    y = random.choice([True, False])
    if y:
        return x
    else:
        return None
