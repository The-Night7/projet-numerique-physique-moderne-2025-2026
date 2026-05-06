from numpy import pi, exp, sqrt, real, imag, zeros, linspace
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# a. Définition de la fonction PlaneWave
# ─────────────────────────────────────────────
def PlaneWave(amp, k, omega, x, t):
    """
    Retourne une onde plane à 1D :
        Ψ(x, t) = amp * exp(i*(k*x - omega*t))

    Paramètres
    ----------
    amp   : amplitude (Ψ₀), peut être réelle ou complexe
    k     : nombre d'onde (m⁻¹)
    omega : pulsation angulaire (rad/s)
    x     : position (m), scalaire ou tableau numpy
    t     : instant (s), scalaire
    """
    return amp * exp(1j * (k * x - omega * t))


# ─────────────────────────────────────────────
# b. Test et représentation graphique
# ─────────────────────────────────────────────

# --- Paramètres physiques ---
amp   = 1.0          # amplitude (m^{-1/2} en 1D)
k     = 2.0 * pi     # nombre d'onde (rad/m)  → longueur d'onde λ = 1 m
omega = 2.0 * pi     # pulsation (rad/s)       → période T = 1 s
t     = 0.0          # instant choisi (s)

# --- Axe spatial ---
x = linspace(-2, 2, 1000)   # 1000 points entre -2 m et +2 m

# --- Calcul de l'onde plane ---
psi = PlaneWave(amp, k, omega, x, t)

# --- Test rapide en un point ---
psi_test = PlaneWave(1.0, pi, pi, 0.5, 0.0)
print(f"Test PlaneWave(amp=1, k=π, ω=π, x=0.5, t=0) :")
print(f"  Partie réelle    = {real(psi_test):.4f}")
print(f"  Partie imaginaire= {imag(psi_test):.4f}")

# --- Tracé ---
fig, ax = plt.subplots()

ax.plot(x, real(psi), label=r"Partie réelle  $\Re(\Psi)$",      color="royalblue")
ax.plot(x, imag(psi), label=r"Partie imaginaire $\Im(\Psi)$",   color="tomato", linestyle="--")

ax.set_xlabel("x (m)")
ax.set_ylabel(r"$\Psi(x,\,t_0)$")
ax.set_title(
    rf"Onde plane 1D — $k={k/pi:.1f}\pi$ rad/m, "
    rf"$\omega={omega/pi:.1f}\pi$ rad/s, $t={t}$ s"
)
ax.legend()
ax.grid(True, linestyle=":")

plt.tight_layout()
plt.show()