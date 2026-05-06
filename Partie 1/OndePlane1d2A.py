from numpy import pi, exp, sqrt, real, imag, zeros, linspace, cos, abs as npabs
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

# ═════════════════════════════════════════════
# PARTIE 2 — Superposition de trois ondes planes
# ═════════════════════════════════════════════

# --- Paramètres de la superposition ---
A  = 1.0        # amplitude de l'onde centrale (m^{-1/2})
k0 = 10.0 * pi  # nombre d'onde central (rad/m)
dk = 2.0 * pi   # écart en nombre d'onde Δk (rad/m)
t2 = 0.0        # instant t = 0

# Pulsations (relation de dispersion ω = ħk²/2m, avec ħ/2m = 1 pour la visualisation)
omega_1 = k0**2
omega_2 = (k0 - dk/2)**2
omega_3 = (k0 + dk/2)**2

# --- Axe spatial : intervalle [-π/Δk, π/Δk] ---
x2 = linspace(-pi/dk, pi/dk, 2000)

# --- Les trois ondes planes à t = 0 ---
psi1 = PlaneWave(A,   k0,        omega_1, x2, t2)   # amplitude A
psi2 = PlaneWave(A/2, k0 - dk/2, omega_2, x2, t2)   # amplitude A/2
psi3 = PlaneWave(A/2, k0 + dk/2, omega_3, x2, t2)   # amplitude A/2

# --- Onde résultante et enveloppe analytique ---
psi_sum  = psi1 + psi2 + psi3
envelope = A * (1 + cos(dk * x2 / 2))   # A·[1 + cos(Δk·x/2)]

# ── Figure 2 : parties réelles des 3 ondes + somme + enveloppe ──
fig2, ax2 = plt.subplots(figsize=(10, 5))

ax2.plot(x2, real(psi1),    label=r"$\Re(\Psi_1)$ — $k_0$",                color="royalblue", linewidth=1.0)
ax2.plot(x2, real(psi2),    label=r"$\Re(\Psi_2)$ — $k_0-\Delta k/2$",     color="tomato",    linewidth=1.0, linestyle="--")
ax2.plot(x2, real(psi3),    label=r"$\Re(\Psi_3)$ — $k_0+\Delta k/2$",     color="seagreen",  linewidth=1.0, linestyle=":")
ax2.plot(x2, real(psi_sum), label=r"$\Re(\Psi_\mathrm{somme})$",            color="black",     linewidth=1.8)
ax2.plot(x2,  envelope,     label=r"Enveloppe $A\!\left[1+\cos\!\left(\frac{\Delta k\,x}{2}\right)\right]$",
         color="darkorange", linewidth=2.0, linestyle="-.")
ax2.plot(x2, -envelope,     color="darkorange", linewidth=2.0, linestyle="-.")  # enveloppe inférieure

ax2.set_xlabel("x (m)")
ax2.set_ylabel(r"$\Re(\Psi)$")
ax2.set_title(
    rf"Superposition de 3 ondes planes — $k_0={k0/pi:.0f}\pi$, "
    rf"$\Delta k={dk/pi:.0f}\pi$ rad/m, $t=0$"
)
ax2.legend(fontsize=8, loc="upper right")
ax2.grid(True, linestyle=":")
plt.tight_layout()

# ── Figure 3 : densité de probabilité ──
rho          = npabs(psi_sum)**2
envelope_rho = A**2 * (1 + cos(dk * x2 / 2))**2   # enveloppe de ρ

fig3, ax3 = plt.subplots(figsize=(10, 4))

ax3.plot(x2, rho,          label=r"$|\Psi|^2$",  color="mediumpurple", linewidth=1.8)
ax3.plot(x2, envelope_rho, label=r"Enveloppe $A^2\!\left[1+\cos\!\left(\frac{\Delta k\,x}{2}\right)\right]^2$",
         color="darkorange", linewidth=2.0, linestyle="-.")

ax3.set_xlabel("x (m)")
ax3.set_ylabel(r"$|\Psi(x,0)|^2$")
ax3.set_title("Densité de probabilité de présence — superposition de 3 ondes planes")
ax3.legend(fontsize=9)
ax3.grid(True, linestyle=":")
plt.tight_layout()

plt.show()