import numpy as np
import matplotlib.pyplot as plt

# a. Définir des constantes hbar et m (valeurs en USI)
hbar = 1.054e-34
m = 9.109e-31

# b. Définir la fonction GaussWP
def GaussWP(k0, a, x, t):
    # Calcul de alpha(t) défini dans la question 1.c
    alpha = a + 1j * (hbar * t) / (2 * m)
    
    # Facteur de normalisation
    norm = (2 * a / np.pi)**0.25 / np.sqrt(2 * alpha)
    
    # Vitesse de groupe
    vg = (hbar * k0) / m
    
    # Terme exponentiel (spatial et phase)
    exp_term = np.exp(- (x - vg * t)**2 / (4 * alpha)) * \
               np.exp(1j * (k0 * x - (hbar * k0**2 / (2 * m)) * t))
               
    return norm * exp_term

# c. Tester la fonction et représenter à t = 0
x = np.linspace(-5e-9, 5e-9, 1000) # Échelle nanométrique
k0 = 5e9
a = 1e-18

# Calcul de la fonction d'onde à t = 0
psi_0 = GaussWP(k0, a, x, 0)

# Représentation
plt.figure(figsize=(10, 5))
plt.plot(x, np.real(psi_0), label='Partie réelle')
plt.plot(x, np.imag(psi_0), label='Partie imaginaire', linestyle='--')
plt.title("Paquet d'ondes gaussien à t=0")
plt.xlabel("Position x (m)")
plt.ylabel(r"$\Psi(x, 0)$")
plt.legend()
plt.grid()
plt.show()