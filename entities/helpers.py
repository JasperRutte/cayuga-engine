import random

def quality_generator() -> int:
    roll = random.randint(1, 100)

    if roll <= 40:
        return 1
    elif roll <= 65:
        return 2
    elif roll <= 80:
        return 3
    elif roll <= 90:
        return 4
    else:
        return 5