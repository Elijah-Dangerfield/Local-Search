import sys
from SumofGaussians import SumofGaussians
import numpy as np

np.set_printoptions(formatter={'float': lambda x: "{0:0.8f}".format(x)})

if len(sys.argv) != 4:
    print()
    print("Usage: %s [seed] [number of dimensions] [number of gausians]" % (sys.argv[0]))
    print()
    sys.exit(1)
step_size = 0.01
tolerance = 1e-8
max_iteration = 1000000


def main():
    np.random.seed(int(sys.argv[1]))
    num_dim = int(sys.argv[2])
    num_gaus = int(sys.argv[3])
    search_space = SumofGaussians(num_dim, num_gaus)
    start = 10 * np.random.ranf(num_dim)
    local_max = search(search_space, start, 1, 0)
    print(str(local_max).lstrip('[').rstrip(']'), "{:.8f}".format(search_space.Eval(local_max)))


def search(search_space,
           old_point, change,
           itterations):

    while change > tolerance and itterations < max_iteration:
        print(str(old_point).lstrip('[').rstrip(']'), "{:.8f}".format(search_space.Eval(old_point)))
        itterations += 1
        new_point = old_point + (step_size * search_space.Deriv(old_point))
        change = abs(search_space.Eval(new_point) - search_space.Eval(old_point))
        old_point = new_point

    return old_point


if __name__ == '__main__':
    main()

