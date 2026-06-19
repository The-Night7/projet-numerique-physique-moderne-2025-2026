import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

try:
    from numba import njit
except ImportError as exc:
    raise ImportError(
        "Ce script optimisé nécessite numba. Installe-le avec : pip install numba"
    ) from exc


hbar = 1.0
m = 1.0


# ============================================================
# Réglages rapides
# ============================================================
# Le calcul numérique est optimisé par Numba. Le premier lancement compile les
# fonctions JIT, puis les appels suivants sont nettement plus rapides.
SAVE_MP4 = True
SAVE_GIF = True      
SHOW_PLOT = True
ANIMATION_STEP = 50
OUTPUT_DIR = "Partie_4/"


# ============================================================
# Paquet d'ondes gaussien centré en x0 à t=0
# ============================================================
def GaussWP_centre(k0, a_wp, x, x0, t):
    alpha = a_wp + 1j * hbar * t / (2 * m)
    norm = (2 * a_wp / np.pi) ** 0.25 / np.sqrt(2 * alpha)
    vg = hbar * k0 / m
    phase = np.exp(1j * (k0 * (x - x0) - hbar * k0**2 / (2 * m) * t))
    enveloppe = np.exp(-((x - x0 - vg * t) ** 2) / (4 * alpha))
    return norm * enveloppe * phase


# ============================================================
# Barrière de potentiel rectangulaire
# ============================================================
def potentiel_barriere(x, x_b, a_b, V0):
    V = np.zeros_like(x)
    V[(x >= x_b) & (x <= x_b + a_b)] = V0
    return V


# ============================================================
# Solveur tridiagonal optimisé
# ============================================================
@njit(cache=True)
def factoriser_tridiagonal(a, b, c):
    """
    Pré-factorisation Thomas pour une matrice tridiagonale constante.
    À faire une seule fois par simulation, au lieu de recopier/factoriser b
    à chaque pas de temps.
    """
    n = b.size
    cp = np.empty(n - 1, dtype=np.complex128)
    denom = np.empty(n, dtype=np.complex128)

    denom[0] = b[0]
    cp[0] = c[0] / denom[0]

    for i in range(1, n - 1):
        denom[i] = b[i] - a[i - 1] * cp[i - 1]
        cp[i] = c[i] / denom[i]

    denom[n - 1] = b[n - 1] - a[n - 2] * cp[n - 2]
    return cp, denom


@njit(cache=True)
def resoudre_tridiagonal_factorise(a, cp, denom, d, out, tmp):
    """
    Résout Ax=d avec la factorisation pré-calculée.
    out et tmp sont réutilisés pour éviter les allocations répétées.
    """
    n = d.size

    tmp[0] = d[0] / denom[0]
    for i in range(1, n):
        tmp[i] = (d[i] - a[i - 1] * tmp[i - 1]) / denom[i]

    out[n - 1] = tmp[n - 1]
    for i in range(n - 2, -1, -1):
        out[i] = tmp[i] - cp[i] * out[i + 1]


@njit(cache=True)
def _evolution_full_core(psi0, a_lower, cp, denom, rhs_coef, r, nt, nx):
    """Évolution complète : garde psi(t, x), nécessaire pour l'animation."""
    n_int = nx - 2
    psi = np.zeros((nt, nx), dtype=np.complex128)
    rhs = np.empty(n_int, dtype=np.complex128)
    out = np.empty(n_int, dtype=np.complex128)
    tmp = np.empty(n_int, dtype=np.complex128)

    for i in range(nx):
        psi[0, i] = psi0[i]

    for j in range(nt - 1):
        for i in range(n_int):
            ix = i + 1
            rhs[i] = rhs_coef[i] * psi[j, ix] + r * psi[j, ix - 1] + r * psi[j, ix + 1]

        resoudre_tridiagonal_factorise(a_lower, cp, denom, rhs, out, tmp)

        psi[j + 1, 0] = 0.0 + 0.0j
        for i in range(n_int):
            psi[j + 1, i + 1] = out[i]
        psi[j + 1, nx - 1] = 0.0 + 0.0j

    return psi


@njit(cache=True)
def _evolution_pic_core(psi0, a_lower, cp, denom, rhs_coef, r, nt, nx, idx_probe, tmin, dt):
    """
    Évolution légère pour les balayages paramétriques : ne stocke pas psi(t,x),
    seulement le temps où le pic est maximal au point idx_probe.
    """
    n_int = nx - 2
    prev = np.empty(nx, dtype=np.complex128)
    curr = np.zeros(nx, dtype=np.complex128)
    rhs = np.empty(n_int, dtype=np.complex128)
    out = np.empty(n_int, dtype=np.complex128)
    tmp = np.empty(n_int, dtype=np.complex128)

    for i in range(nx):
        prev[i] = psi0[i]

    max_j = 0
    max_amp = (prev[idx_probe].real * prev[idx_probe].real +
               prev[idx_probe].imag * prev[idx_probe].imag)

    for j in range(nt - 1):
        for i in range(n_int):
            ix = i + 1
            rhs[i] = rhs_coef[i] * prev[ix] + r * prev[ix - 1] + r * prev[ix + 1]

        resoudre_tridiagonal_factorise(a_lower, cp, denom, rhs, out, tmp)

        curr[0] = 0.0 + 0.0j
        for i in range(n_int):
            curr[i + 1] = out[i]
        curr[nx - 1] = 0.0 + 0.0j

        amp = curr[idx_probe].real * curr[idx_probe].real + curr[idx_probe].imag * curr[idx_probe].imag
        if amp > max_amp:
            max_amp = amp
            max_j = j + 1

        swap = prev
        prev = curr
        curr = swap

    return tmin + max_j * dt


def preparer_systeme(nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_b, V0):
    x = np.linspace(xmin, xmax, nx)
    t = np.linspace(tmin, tmax, nt)
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    V = potentiel_barriere(x, x_b, a_b, V0)
    V_int = V[1:-1]
    n_int = nx - 2

    r = 1j * hbar * dt / (4 * m * dx**2)
    s_int = 1j * V_int * dt / (2 * hbar)

    a_lower = np.full(n_int - 1, -r, dtype=np.complex128)
    b_diag = np.ones(n_int, dtype=np.complex128) * (1 + 2 * r) + s_int
    c_upper = np.full(n_int - 1, -r, dtype=np.complex128)
    rhs_coef = np.asarray(1 - 2 * r - s_int, dtype=np.complex128)
    psi0 = np.asarray(GaussWP_centre(k0, a_wp, x, x0, 0.0), dtype=np.complex128)

    cp, denom = factoriser_tridiagonal(a_lower, b_diag, c_upper)
    return x, t, dx, dt, psi0, a_lower, cp, denom, rhs_coef, r


def evolution_schrodinger(nx, nt, xmin, xmax, tmin, tmax,
                          k0, a_wp, x0, x_b, a_b, V0):
    x, t, dx, dt, psi0, a_lower, cp, denom, rhs_coef, r = preparer_systeme(
        nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_b, V0
    )
    psi = _evolution_full_core(psi0, a_lower, cp, denom, rhs_coef, r, nt, nx)
    return x, t, psi, dx


def temps_pic_sans_stockage(nx, nt, xmin, xmax, tmin, tmax,
                            k0, a_wp, x0, x_b, a_b, V0, x_probe):
    x, t, dx, dt, psi0, a_lower, cp, denom, rhs_coef, r = preparer_systeme(
        nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_b, V0
    )
    idx_probe = int(np.argmin(np.abs(x - x_probe)))
    return _evolution_pic_core(psi0, a_lower, cp, denom, rhs_coef, r, nt, nx, idx_probe, tmin, dt)


def norme(psi_x, dx):
    return np.sum(np.abs(psi_x) ** 2) * dx


def temps_pic_en(psi, t, idx_x):
    # Version vectorisée : évite la liste Python [ ... for j in range(...) ]
    return t[np.argmax(np.abs(psi[:, idx_x]) ** 2)]


# ============================================================
# Fonctions analytiques inchangées
# ============================================================
def coeff_transmission(k0, a_b, V0):
    E = hbar**2 * k0**2 / (2 * m)
    if V0 <= 0.0:
        return 1.0
    if E >= V0:
        k2 = np.sqrt(2 * m * (E - V0)) / hbar
        if k2 == 0.0:
            return 1.0
        denom = 1 + (k0**2 - k2**2) ** 2 * np.sin(k2 * a_b) ** 2 / (4 * k0**2 * k2**2)
        return 1.0 / denom
    kappa = np.sqrt(2 * m * (V0 - E)) / hbar
    denom = 1 + (k0**2 + kappa**2) ** 2 * np.sinh(kappa * a_b) ** 2 / (4 * k0**2 * kappa**2)
    return 1.0 / denom


def vitesse_groupe(k0):
    return hbar * k0 / m


def tau_libre(k0, a_b):
    return m * a_b / (hbar * k0)


def phase_transmission(k, a_b, V0):
    E_k = hbar**2 * k**2 / (2 * m)
    if E_k >= V0:
        return None
    kappa = np.sqrt(2 * m * (V0 - E_k)) / hbar
    eta = (kappa**2 - k**2) / (2 * k * kappa)
    return -k * a_b - np.arctan(eta * np.tanh(kappa * a_b))


def decalage_groupe(k0, a_b, V0):
    E = hbar**2 * k0**2 / (2 * m)
    if E >= V0:
        return None
    dk = 1e-6
    phi_p = phase_transmission(k0 + dk, a_b, V0)
    phi_m = phase_transmission(k0 - dk, a_b, V0)
    if phi_p is None or phi_m is None:
        return None
    dphi_dk = (phi_p - phi_m) / (2 * dk)
    vg = hbar * k0 / m
    return dphi_dk / vg


def tau_tunnel(k0, a_b, V0):
    E = hbar**2 * k0**2 / (2 * m)
    if E >= V0:
        return None
    tau_g = decalage_groupe(k0, a_b, V0)
    if tau_g is None:
        return None
    return tau_libre(k0, a_b) + tau_g


# ============================================================
# Main
# ============================================================
def main():
    nx = 3000
    nt = 6000
    xmin, xmax = -30.0, 30.0
    tmin, tmax = 0.0, 6.0

    k0 = 5.0
    a_wp = 1.0
    x0 = -10.0
    x_b = 0.0
    a_b = 1.0
    V0 = 15.0

    E = hbar**2 * k0**2 / (2 * m)
    vg = vitesse_groupe(k0)
    kappa = np.sqrt(2 * m * (V0 - E)) / hbar

    print("=" * 58)
    print("Paramètres physiques")
    print("=" * 58)
    print(f"  E = {E:.3f},  V0 = {V0:.3f}  →  effet tunnel")
    print(f"  v_g = hbar·k0/m = {vg:.3f}")
    print(f"  κ = sqrt(2m(V0-E))/hbar = {kappa:.4f}")
    print(f"  κ·a = {kappa * a_b:.3f}  (> 1 : régime opaque)")
    print(f"  |T|² analytique = {coeff_transmission(k0, a_b, V0):.4e}")

    print("\n--- 4.1.b : particule libre (V0 = 0) ---")
    x, t, psi_libre, dx = evolution_schrodinger(
        nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_b, 0.0
    )

    idx_entree = np.argmin(np.abs(x - x_b))
    idx_sortie = np.argmin(np.abs(x - (x_b + a_b)))

    t_entree = temps_pic_en(psi_libre, t, idx_entree)
    t_sortie_libre = temps_pic_en(psi_libre, t, idx_sortie)
    tau_0_num = t_sortie_libre - t_entree
    tau_0_th = tau_libre(k0, a_b)

    print(f"  t_entree      = {t_entree:.4f}  (attendu {(x_b - x0) / vg:.4f})")
    print(f"  t_sortie      = {t_sortie_libre:.4f}  (attendu {(x_b + a_b - x0) / vg:.4f})")
    print(f"  τ_{{0,num}}    = {tau_0_num:.4f}")
    print(f"  τ_{{0,th}}     = a/v_g = {tau_0_th:.4f}")

    print("\n--- 4.1.a-c : barrière de potentiel (V0 > 0) ---")
    x, t, psi_barr, dx = evolution_schrodinger(
        nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_b, V0
    )

    t_sortie_tunnel = temps_pic_en(psi_barr, t, idx_sortie)
    tau_t_num = t_sortie_tunnel - t_entree
    tau_t_th = tau_tunnel(k0, a_b, V0)

    print(f"  t_sortie tunnel   = {t_sortie_tunnel:.4f}")
    print(f"  τ_{{t,num}}        = {tau_t_num:.4f}")
    if tau_t_th is not None:
        print(f"  τ_{{t,th}} (Hartman) = {tau_t_th:.4f}")
        print(f"  τ_{{t,th}} / τ_{{0,th}} = {tau_t_th / tau_0_th:.3f}  (< 1 : effet Hartman)")

    norme_init = norme(psi_barr[0, :], dx)
    norme_fin = norme(psi_barr[-1, :], dx)
    mask_trans = x > x_b + a_b
    norme_trans = norme(psi_barr[-1, mask_trans], dx)
    print(f"\n  Norme initiale    : {norme_init:.6f}")
    print(f"  Norme finale      : {norme_fin:.6f}")
    print(f"  Norme transmise (paquet numérique) : {norme_trans:.4e}")
    print(f"  |T|² théorique (onde plane k0)      : {coeff_transmission(k0, a_b, V0):.4e}")

    print("\n--- 4.1.d : influence de la largeur a ---")
    a_valeurs = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    tau_0_list = []
    tau_t_num_list = []
    tau_t_th_list = []
    T2_list = []

    for a_val in a_valeurs:
        tau_0_list.append(tau_libre(k0, a_val))
        tau_t_th_list.append(tau_tunnel(k0, a_val, V0))
        T2_list.append(coeff_transmission(k0, a_val, V0))

        t_s = temps_pic_sans_stockage(
            nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_val, V0, x_b + a_val
        )
        tau_t_num_list.append(t_s - t_entree)

        print(
            f"  a={a_val:.1f} : τ_0={tau_0_list[-1]:.3f}  "
            f"τ_t_num={tau_t_num_list[-1]:.3f}  "
            f"τ_t_th={tau_t_th_list[-1]:.3f}  "
            f"|T|²={T2_list[-1]:.2e}"
        )

    print("\n--- 4.1.e : influence de V0 ---")
    V0_valeurs = [13.5, 14.0, 15.0, 17.0, 20.0, 25.0]
    V0_valid = []
    tau_t_V0_list = []
    T2_V0_list = []

    for V0_val in V0_valeurs:
        if V0_val <= E:
            print(f"  V0={V0_val:.1f} : E >= V0, au-dessus de la barrière")
            continue
        kap = np.sqrt(2 * m * (V0_val - E)) / hbar
        tt = tau_tunnel(k0, a_b, V0_val)
        T2 = coeff_transmission(k0, a_b, V0_val)
        V0_valid.append(V0_val)
        tau_t_V0_list.append(tt)
        T2_V0_list.append(T2)
        print(
            f"  V0={V0_val:.1f} : κ·a={kap * a_b:.3f}  "
            f"τ_t_th={tt:.4f}  |T|²={T2:.2e}"
        )

    V_plot = potentiel_barriere(x, x_b, a_b, V0)

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.set_xlim(xmin, xmax)
    y_max = max(np.max(np.abs(psi_libre) ** 2), np.max(np.abs(psi_barr) ** 2))
    ax1.set_ylim(0, y_max * 1.1)

    echelle = 0.4 * y_max if y_max > 0 else 0.01
    barriere_plot = V_plot / V0 * echelle
    ax1.fill_between(x, 0, barriere_plot, alpha=0.25, color="gray", label=f"Barrière V0={V0}")

    line_libre, = ax1.plot([], [], color="royalblue", label="|ψ libre|² (V0=0)")
    line_barr, = ax1.plot([], [], color="tomato", label=f"|ψ tunnel|² (V0={V0})")

    ax1.set_xlabel("x")
    ax1.set_ylabel("|ψ|²")
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(True, linestyle=":")
    titre_texte = ax1.set_title("")

    def init():
        line_libre.set_data([], [])
        line_barr.set_data([], [])
        titre_texte.set_text("")
        return line_libre, line_barr, titre_texte

    def animate(j):
        line_libre.set_data(x, np.abs(psi_libre[j, :]) ** 2)
        line_barr.set_data(x, np.abs(psi_barr[j, :]) ** 2)
        titre_texte.set_text(f"Évolution quantique : temps t = {t[j]:.2f}")
        return line_libre, line_barr, titre_texte

    frames = range(0, nt, ANIMATION_STEP)
    ani = animation.FuncAnimation(
        fig1, animate, frames=frames, init_func=init,
        blit=True, interval=30, repeat=False
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if SAVE_MP4:
        ani.save(os.path.join(OUTPUT_DIR, "Figure_1_animee.mp4"), writer="ffmpeg", fps=30)
    if SAVE_GIF:
        ani.save(os.path.join(OUTPUT_DIR, "Figure_1_animee.gif"), writer="pillow", fps=30)

    if SHOW_PLOT and plt.get_backend().lower() != "agg":
        plt.show()
    else:
        plt.close(fig1)


if __name__ == "__main__":
    main()
