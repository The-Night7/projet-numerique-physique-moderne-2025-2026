import numpy as np

#3.1.1.b
def derivee_premiere(y, dx):
    dy = np.zeros(len(y))
    dy[:-1] = (y[1:] - y[:-1]) / dx 
    dy[-1] = (y[-1] - y[-2]) / dx   
    return dy

#3.1.1.c
def carre(x):
    return x**2

def double(x):
    return 2*x

#3.1.2
def calculer_derivee_seconde(y, dx):
    d2y = np.zeros(len(y))
    d2y[1:-1] = (y[:-2] - 2*y[1:-1] + y[2:])
    dx**2
    return d2y
