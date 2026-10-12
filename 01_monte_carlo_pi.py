# Project 1: Estimate pi with random darts (Monte Carlo)
#
# Throw random darts at a 1x1 square. A dart at (x, y) lands inside the
# quarter circle when x*x + y*y <= 1. The fraction that lands inside is
# about pi/4, so pi is about 4 * (inside / total).
#  DOUBLING THE DARTS DOESN'T DOUBLE THE ACCURACY.EACH IMPROVEMENT IN ACCURACY COSTS MUCH MORE EFFORT THAN THE LAST. 

# Fill in the three TODOs, then run it with:   py 01_monte_carlo_pi.py

import random
import math


def estimate_pi(num_darts):
    inside = 0

    for _ in range(num_darts):
        # TODO 1: make x and y random numbers between 0 and 1
        #         hint: random.random() gives you one
        x = random.random()
        y = random.random()

        # TODO 2: if the dart is inside the quarter circle, add 1 to `inside`
        if x ** 2 + y ** 2 <= 1:
            inside +=1

    # TODO 3: turn the count into an estimate of pi
    return 4 * (inside / num_darts )



if __name__ == "__main__":
    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        est = estimate_pi(n)
        error = abs(est - math.pi)
        print(f"{n:>9,} darts -> pi ~ {est:.5f}   (off by {error:.5f})")
