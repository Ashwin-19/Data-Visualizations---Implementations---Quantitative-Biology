# Author @Ashwin_19

import matplotlib.pyplot as plot
import numpy

def Cobweb(sf, lim):

    x_axis = numpy.arange(0,lim,0.01)
    y_axis= [sf*i*(1-i) for i in x_axis]

    line = plot.figure()
    line = line.add_subplot(1,1,1)
    line.plot(x_axis, x_axis)

    xplot = [0 for i in range(41)]
    yplot = [0 for i in range(41)]

    xplot[0] = 0.2

    for j in range(1,40,2):
        xplot[j] = xplot[j-1]
        yplot[j] = sf*xplot[j-1]*(1-xplot[j-1])
        yplot[j+1] = yplot[j]
        xplot[j+1] = yplot[j]

    line.plot(xplot, yplot)

    plot.plot(x_axis, y_axis, label = "N(t+1)", color = "c")
    plot.title("N(t+1) vs N(t)")
    plot.show()


# Cobweb(sf, lim)
