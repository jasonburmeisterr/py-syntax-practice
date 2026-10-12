# Project 2: How often do you roll a 6?
#
# The math says 1 out of 6 rolls is a 6, about 0.1667.
# Roll a die many times and see if the computer agrees.
#
# Same shape as the pi project: a loop, an if, and a counter.
# Fill in the two TODOs, save (Ctrl+S), then say "run it".

import random


def chance_of_six(num_rolls):
    sixes = 0

    for _ in range(num_rolls):
        # TODO 1: roll the die (a random whole number from 1 to 6)
        #         hint: random.randint(1, 6)
        roll = random.randint(1, 6)

        # TODO 2: if the roll is a 6, add 1 to `sixes`
        #         remember: to compare, use == (two equals signs)
        if roll == 6: 
            sixes += 1
            

    return sixes / num_rolls


if __name__ == "__main__":
    print("Math says: 0.1667\n")
    for n in [60, 600, 6_000, 60_000, 600_000]:
        print(f"{n:>7,} rolls -> {chance_of_six(n):.4f}")
