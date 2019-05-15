# Author - @ashwin17222

import numpy as np
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings("ignore")

def equilibrium(arr):

    a = arr[0][0]
    b = arr[0][1]
    c = arr[1][0]
    d = arr[1][1]

    x = np.array([[1-a, -b], [c, d-1]])
    y = np.array([0,0])
    soln = np.linalg.solve(x,y)
    print(soln)


def eigenfunc(arr):

    eigval, eigvectors = np.linalg.eig(arr)

    plt.plot(eigvectors)
    plt.show()

    return eigval, eigvectors

def directionfields(arr):

    a = arr[0][0]
    b = arr[0][1]
    c = arr[1][0]
    d = arr[1][1]

    fig = plt.figure(num=1)
    ax = fig.add_subplot(111)
    xaxis_l = np.linspace(-5, 5, 20)
    xaxis_r = np.linspace(-10, 10, 20)
    x, y = np.meshgrid(xaxis_l, xaxis_r)

    u = (a-1)*x + b*y
    v = c*x + (d-1)*y

    N = np.sqrt(u ** 2 + v ** 2)
    u2, v2 = u / N, v / N

    ax.quiver(x, y, u2, v2)
    plt.xlim([-5, 5])
    plt.ylim([-10, 10])
    plt.show()

def report(l1, l2):

    l1 = abs(l1)
    l2 = abs(l2)

    if l1 > 1 and l2 > 1:

        print("The equilibrium grows and is unstable.")

    elif l1 <= 1 and l2 <= 1:

        print("The equilibrium shrinks and is stable.")

    else:

        print("Different perturbations behave qualitatively differently.")
        print("The eigenvector corresponding to the bigger (>1) eigenvalue will grow.")
        print("The eigenvector corresponding to the smaller (<1) eigenvalue will shrink.")
        print("The equilibrium is saddle in nature.")
