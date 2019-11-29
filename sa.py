#!/usr/bin/env python3

import sys
import numpy as np
from SumofGaussians import SumofGaussians

np.set_printoptions(formatter={'float': lambda x: "{0:0.8f}".format(x)})

if len(sys.argv) != 4:
    print()
    print("Usage: %s [seed] [number of dimensions] [number of gausians]" % (sys.argv[0]))
    print()
    sys.exit(1)

max_iteration = 100000
T = 10000.0
t_min = 1e-8
cooling_rate = 0.99


def main():
    np.random.seed(int(sys.argv[1]))
    num_dim = int(sys.argv[2])
    num_gaus = int(sys.argv[3])
    search_space = SumofGaussians(num_dim, num_gaus)
    start = 10 * np.random.ranf(num_dim)
    found_max = search(search_space, start, T, cooling_rate, num_dim)
    print(str(found_max).lstrip('[').rstrip(']'), "{:.8f}".format(search_space.Eval(found_max)))


def search(search_space, current_point, T, cooling_rate, num_dim):
    iterations = 0

    while iterations < max_iteration and T > t_min:

        print(str(current_point).lstrip('[').rstrip(']'), "{:.8f}".format(search_space.Eval(current_point)))

        iterations += 1
        new_point = current_point + np.random.uniform(-0.01, 0.01, num_dim)

        for x in range(len(new_point)):
            if new_point[x] > 10:
                new_point[x] -= 10
            elif new_point[x] < 0:
                new_point[x] += 10

        current_energy = search_space.Eval(current_point)
        new_energy = search_space.Eval(new_point)

        if new_energy > current_energy:
            current_point = new_point  # accept the value
        else:
            p = np.exp((new_energy - current_energy) / T)
            if p > np.random.uniform(0, 1):
                current_point = new_point  # accept the value

        T *= cooling_rate

    return current_point


if __name__ == '__main__':
    main()
