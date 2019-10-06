import sys
import numpy as np
from SumofGaussians import SumofGaussians
from math import e
import random

if len(sys.argv) != 4:
    print()
    print("Usage: %s [seed] [number of dimensions] [number of gausians]" % (sys.argv[0]))
    print()
    sys.exit(1)

max_iteration = 100000
T = 1.0
t_min = 1e-5
cooling_rate = 0.99


def main():
    np.random.seed(int(sys.argv[1]))
    num_dim = int(sys.argv[2])
    num_gaus = int(sys.argv[3])
    search_space = SumofGaussians(num_dim, num_gaus)
    start = np.random.ranf(num_dim)
    (found_max, it) = search(search_space, start, T, cooling_rate)
    print("starting at point: ", start, " = ", search_space.Eval(start))
    print("ending at point: ", found_max, " = ", search_space.Eval(found_max))
    print("ended with ", it, " iterations")



def search(search_space, current_point, T, cooling_rate):

    iterations = 0

    while iterations < max_iteration and T > t_min:

        iterations +=1
        new_point = current_point + np.random.uniform(-0.01, 0.01)
        current_energy = search_space.Eval(current_point)
        new_energy = search_space.Eval(new_point)

        if new_energy > current_energy:
            current_point = new_point  # accept the value
        else:
            print(T)
            p = e ** ((new_energy - current_energy) / T)
            if p > random.uniform(0, 1):
                current_point = new_point  # accept the value

        T *= cooling_rate

    return (current_point, iterations)


if __name__ == '__main__':
    main()
