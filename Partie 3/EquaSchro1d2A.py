import numpy as np
import GaussWP from /Partie 2/PaquetOndeGauss1d2A.py

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

#3.2.2
psi = np.zeros((nt, nx), dtype=complex)
psi[0, :] = GaussWP(k0, a, x, 0)

#3.2.3
x = np.linspace(xmin, xmax, nx)
t = np.linspace(tmin, tmax, nt)
dx = x[1] - x[0]
dt = t[1] - t[0]

#3.2.4
# Pré-calcul de la constante pour optimiser l'itération
coeff = dt / (1j * hbar)

for n in range(0, nt - 1):
    # Calcul de la dérivée seconde spatiale à l'instant n (points intérieurs)
    d2psi_dx2 = (psi[:-2, n] - 2*psi[1:-1, n] + psi[2:, n]) / dx**2
    
    # Action de l'opérateur Hamiltonien sur la fonction d'onde
    H_psi = -(hbar**2 / (2*m)) * d2psi_dx2 + V0 * psi[1:-1, n]
    
    # Mise à jour de la fonction d'onde à l'instant n+1
    psi[1:-1, n+1] = psi[1:-1, n] + coeff * H_psi