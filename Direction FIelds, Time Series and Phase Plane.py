# Author - @ashwin17222
# For non-linear population model

import numpy as np
from matplotlib import pyplot as plt

def directionfields(r,K,s,u,v):

    fig = plt.figure(num=1)
    ax = fig.add_subplot(111)
    xaxis_l = np.linspace(-5, 5, 20)
    xaxis_r = np.linspace(-10, 10, 20)
    x, y = np.meshgrid(xaxis_l, xaxis_r)

    # delta P and delta Q
    y1 = r*x - r*(x**2) - s*x*y
    y2 = -u*y + v*x*y

    # Nullclines
    y3 = np.full((2000,1),u/v)
    y4 = np.linspace(-5,5,2000)
    y5 = y4*0
    y6 = (r/s)*(1-(y4))

    N = np.sqrt(y1 ** 2 + y2 ** 2)
    f1, f2 = y1 / N, y2 / N

    plt.plot(y3, y4, label = "P = u/v")
    plt.plot(y5, y4, label = "delta Q = 0")
    plt.plot(y6, y4, label = "Q = (r/s)*(1-P)")
    plt.plot(y4, y5, label = "delta P = 0")

    ax.quiver(x, y, f1, f2)
    plt.xlim([-5, 5])
    plt.ylim([-10, 10])

    # equilibrium point
    plt.scatter(0.4375, 1.4625, label = "Equilibrium point")

    plt.title("Direction Fields")
    plt.legend()
    plt.show()

def timeseries(r,K,s,u,v,string):

    # initial population - p0 = q0 = 0.5
    P = [0.5]
    Q = [0.5]

    x_axis = [i for i in range(500)]

    for i in range(1,500):
        P.append(P[i-1]*(1+r*(1-(P[i-1]/K))) - s*P[i-1]*Q[i-1])
        Q.append((1-u)*Q[i-1] + v*P[i-1]*Q[i-1])

    fig = plt.figure(num=1)
    ax = fig.add_subplot(111)
    if string == "P":
        ax.plot(x_axis, P, label=string, color="c")
        plt.title("Steady State of P - stable, converging to a value")
    elif string == "Q":
        ax.plot(x_axis, Q, label=string, color="c")
        plt.title("Steady State of Q - stable, converging to a value")
    else:
        ax.plot(x_axis, P, Q, label=string, color="c")
        plt.title("Steady State of P & Q - stable, converging to a value")
    plt.show()


def phaseplane(r,K,s,u,v):

    # initial population - p0 = q0 = 0.5
    P = [0.5]
    Q = [0.5]

    for i in range(1, 500):
        P.append(P[i - 1] * (1 + r * (1 - (P[i - 1] / K))) - s * P[i - 1] * Q[i - 1])
        Q.append((1 - u) * Q[i - 1] + v * P[i - 1] * Q[i - 1])

    fig = plt.figure(num=1)
    ax = fig.add_subplot(111)
    ax.plot(P, Q, color="c")
    plt.title("Phase Plane - Convergent and Stable")
    plt.show()


# given - comparing with equation of the standard form
# P[i] = P[i-1]*(1+r*(1-(P[i-1]/K))) - s*P[i-1]*Q[i-1]
# Q[i] = (1-u)*Q[i-1] + v*P[i-1]*Q[i-1]

# Direction field
# directionfields(r,K,s,u,v)

# Phase plane
# phaseplane(r,K,s,u,v)

# Time series plot
# timeseries(r,K,s,u,v,"P")
# timeseries(r,K,s,u,v,"Q")
# timeseries(r,K,s,u,v,"P & Q")
