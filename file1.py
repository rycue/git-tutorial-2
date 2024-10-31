import random

def foo() -> Optional[int]:
    """This function returns a random integer between 0 and 10, or None if a randomly chosen boolean is False."""
    x = random.randint(0, 10)
    # randomly choose a boolean
    y = random.choice([True, False])
    if y:
        # return the integer
        return x
    else:
        # return None
        return None
