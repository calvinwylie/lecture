import sys

import numpy as np
import matplotlib.pyplot as plt

def amdahl_speedup(alpha, p):
    return 1.0 / (alpha + (1 - alpha) / p)

def amdahl_efficiency(alpha, p):
    return amdahl_speedup(alpha, p) / p

if __name__ == '__main__':
    alpha = float(sys.argv[1])
    core_limit = int(sys.argv[2])

    f = np.vectorize(lambda x: amdahl_speedup(alpha, x))
    p = np.arange(2, core_limit + 1)
    speedup = f(p)
    plt.plot(p, speedup)
    plt.xlabel("Number of Cores")
    plt.ylabel("Speedup")
    plt.xlim(2, core_limit)
    plt.savefig("q1_speedup.png")
    plt.clf()

    efficiency = speedup / p
    plt.plot(p, efficiency)
    plt.xlabel("Number of Cores")
    plt.ylabel("Efficiency")
    plt.xlim(2, core_limit)
    plt.ylim(0, 1)
    plt.savefig("q1_efficiency.png")
    plt.clf()