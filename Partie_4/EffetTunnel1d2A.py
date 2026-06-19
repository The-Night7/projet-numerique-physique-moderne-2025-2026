import numpy as np
import matplotlib.pyplot as plt


hbar = 1.0
m = 1.0


# ============================================================
# Paquet d'ondes gaussien centré en x0 à t=0
# ============================================================
def GaussWP_centre(k0, a_wp, x, x0, t):
    """
    Paquet d'ondes gaussien dont le centre est en x0 à t=0.
    La vitesse de groupe vg = hbar*k0/m déplace le centre au cours du temps.
    """
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
    """Barrière rectangulaire de hauteur V0, définie sur [x_b, x_b + a_b]."""
    V = np.zeros_like(x)
    V[(x >= x_b) & (x <= x_b + a_b)] = V0
    return V


# ============================================================
# Résolution de système tridiagonal (méthode de Thomas)
# ============================================================
def resoudre_tridiagonal(a, b, c, d):
    n = len(d)
    bc = b.copy()
    dc = d.copy()
    for i in range(1, n):
        f = a[i - 1] / bc[i - 1]
        bc[i] -= f * c[i - 1]
        dc[i] -= f * dc[i - 1]
    x_sol = np.zeros(n, dtype=complex)
    x_sol[-1] = dc[-1] / bc[-1]
    for i in range(n - 2, -1, -1):
        x_sol[i] = (dc[i] - c[i] * x_sol[i + 1]) / bc[i]
    return x_sol


# ============================================================
# Évolution de Schrödinger avec barrière (Crank-Nicolson)
# ============================================================
def evolution_schrodinger(nx, nt, xmin, xmax, tmin, tmax,
                          k0, a_wp, x0, x_b, a_b, V0):
    """
    Résout l'équation de Schrödinger à 1D avec une barrière rectangulaire
    par le schéma de Crank-Nicolson.

    Chaque point intérieur a son propre coefficient de potentiel :
    s_i = i*V(x_i)*dt/(2*hbar), ce qui rend la diagonale b_mat spatialement
    variable (contrairement au cas V0 constant de la partie 3).
    """
    x = np.linspace(xmin, xmax, nx)
    t = np.linspace(tmin, tmax, nt)
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    V = potentiel_barriere(x, x_b, a_b, V0)
    V_int = V[1:-1]

    psi = np.zeros((nt, nx), dtype=complex)
    psi[0, :] = GaussWP_centre(k0, a_wp, x, x0, 0.0)

    n_int = nx - 2
    r = 1j * hbar * dt / (4 * m * dx**2)
    s_int = 1j * V_int * dt / (2 * hbar)

    a_mat = np.full(n_int - 1, -r, dtype=complex)
    b_mat = np.ones(n_int, dtype=complex) * (1 + 2 * r) + s_int
    c_mat = np.full(n_int - 1, -r, dtype=complex)

    for j in range(nt - 1):
        psi_int = psi[j, 1:-1]
        rhs = (1 - 2 * r - s_int) * psi_int + r * psi[j, :-2] + r * psi[j, 2:]
        psi[j + 1, 1:-1] = resoudre_tridiagonal(a_mat, b_mat, c_mat, rhs)
        psi[j + 1, 0] = 0.0
        psi[j + 1, -1] = 0.0

    return x, t, psi, dx


def norme(psi_x, dx):
    return np.sum(np.abs(psi_x) ** 2) * dx


# ============================================================
# 4.3.a - Coefficient de transmission analytique |T|²
# ============================================================
def coeff_transmission(k0, a_b, V0):
    """
    Probabilité de transmission |T|² pour une barrière rectangulaire.

    Pour E < V0 (effet tunnel, κ réel) :
      |T|² = 1 / [1 + (κ²+k²)²·sinh²(κa) / (4k²κ²)]

    Pour E > V0 (au-dessus de la barrière, k2 réel) :
      |T|² = 1 / [1 + (k²-k2²)²·sin²(k2·a) / (4k²·k2²)]
    """
    E = hbar**2 * k0**2 / (2 * m)
    if V0 <= 0.0:
        return 1.0
    if E >= V0:
        k2 = np.sqrt(2 * m * (E - V0)) / hbar
        if k2 == 0.0:
            return 1.0
        denom = 1 + (k0**2 - k2**2) ** 2 * np.sin(k2 * a_b) ** 2 / (4 * k0**2 * k2**2)
        return 1.0 / denom
    else:
        kappa = np.sqrt(2 * m * (V0 - E)) / hbar
        denom = 1 + (k0**2 + kappa**2) ** 2 * np.sinh(kappa * a_b) ** 2 / (4 * k0**2 * kappa**2)
        return 1.0 / denom


# ============================================================
# 4.3.b-c - Vitesse de groupe et temps de traversée libre
# ============================================================
def vitesse_groupe(k0):
    """v_g = hbar·k0 / m."""
    return hbar * k0 / m


def tau_libre(k0, a_b):
    """τ_{0,th} = a / v_g = m·a / (hbar·k0)."""
    return m * a_b / (hbar * k0)


# ============================================================
# 4.3.f - Phase de T(k) et temps de tunnel (effet Hartman)
# ============================================================
def phase_transmission(k, a_b, V0):
    """
    Phase φ_T(k) = arg(T(k)) pour l'effet tunnel (E < V0).

    En partant de :
      T(k) = e^{-ika} / [cosh(κa) + i·(κ²-k²)/(2kκ)·sinh(κa)]

    on obtient :
      φ_T(k) = -k·a - arctan[(κ²-k²)·tanh(κa) / (2k·κ)]
    """
    E_k = hbar**2 * k**2 / (2 * m)
    if E_k >= V0:
        return None
    kappa = np.sqrt(2 * m * (V0 - E_k)) / hbar
    eta = (kappa**2 - k**2) / (2 * k * kappa)
    return -k * a_b - np.arctan(eta * np.tanh(kappa * a_b))


def decalage_groupe(k0, a_b, V0):
    """
    Décalage de groupe τ_g = (1/v_g)·dφ_T/dk|_{k0}.

    Ce décalage est NÉGATIF dans le régime tunnel : le pic transmis
    « sort » de la barrière en avance sur la particule libre.
    """
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
    """
    Temps de traversée tunnel analytique : τ_{t,th} = τ_0 + τ_g.

    τ_0 = a/v_g  est le temps libre pour parcourir la distance a.
    τ_g = décalage_groupe(k0, a_b, V0)  est le retard de groupe (négatif
    en régime tunnel).

    En régime opaque (κ·a >> 1), τ_g → -τ_0 + constante, donc τ_{t,th}
    sature vers une valeur indépendante de a : c'est l'effet Hartman.
    """
    E = hbar**2 * k0**2 / (2 * m)
    if E >= V0:
        return None
    tau_g = decalage_groupe(k0, a_b, V0)
    if tau_g is None:
        return None
    return tau_libre(k0, a_b) + tau_g


# ============================================================
# Mesure numérique des temps de traversée
# ============================================================
def temps_pic_en(psi, t, idx_x):
    """
    Retourne le temps t* tel que |ψ(x_{idx_x}, t*)|² soit maximal.
    """
    amp = np.array([np.abs(psi[j, idx_x]) ** 2 for j in range(len(t))])
    return t[np.argmax(amp)]


# ============================================================
# Main
# ============================================================
def main():
    # --------------------------------------------------------
    # Paramètres de la simulation
    # --------------------------------------------------------
    nx = 3000
    nt = 6000
    xmin, xmax = -30.0, 30.0
    tmin, tmax = 0.0, 6.0

    k0 = 5.0       # vecteur d'onde moyen → E = k0²/2 = 12.5
    a_wp = 1.0     # largeur initiale du paquet d'ondes (en espace)
    x0 = -10.0     # centre initial du paquet
    x_b = 0.0      # bord gauche de la barrière
    a_b = 1.0      # largeur de la barrière (distance a)
    V0 = 15.0      # hauteur de la barrière (V0 > E : effet tunnel)

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

    # --------------------------------------------------------
    # 4.1.b - Particule libre (V0 = 0) : mesure de τ_{0,num}
    # --------------------------------------------------------
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

    # --------------------------------------------------------
    # 4.1.a-c - Simulation avec barrière (effet tunnel)
    # --------------------------------------------------------
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
    print(f"  |T|² théorique (onde plane k0)      : {coeff_transmission(k0,a_b,V0):.4e}")

    # --------------------------------------------------------
    # 4.1.d - Influence de la largeur a
    # --------------------------------------------------------
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

        _, _, psi_tmp, _ = evolution_schrodinger(
            nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_val, V0
        )
        idx_s = np.argmin(np.abs(x - (x_b + a_val)))
        t_s = temps_pic_en(psi_tmp, t, idx_s)
        tau_t_num_list.append(t_s - t_entree)

        print(
            f"  a={a_val:.1f} : τ_0={tau_0_list[-1]:.3f}  "
            f"τ_t_num={tau_t_num_list[-1]:.3f}  "
            f"τ_t_th={tau_t_th_list[-1]:.3f}  "
            f"|T|²={T2_list[-1]:.2e}"
        )

    # --------------------------------------------------------
    # 4.1.e - Influence de V0
    # --------------------------------------------------------
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

    # ========================================================
    # Figures
    # ========================================================
    V_plot = potentiel_barriere(x, x_b, a_b, V0)

    # --- Figure 1 : évolution temporelle ---
    fig1, axes = plt.subplots(1, 3, figsize=(15, 4))
    instants = [0, nt // 2, -1]
    titres = ["t = 0 (initial)", f"t = {t[nt // 2]:.2f}", f"t = {t[-1]:.2f} (final)"]

    for ax, j, titre in zip(axes, instants, titres):
        y_max = max(
            np.max(np.abs(psi_libre[j, :]) ** 2),
            np.max(np.abs(psi_barr[j, :]) ** 2),
        )
        echelle = 0.4 * y_max if y_max > 0 else 0.01
        barriere_plot = V_plot / V0 * echelle
        ax.fill_between(x, 0, barriere_plot, alpha=0.25, color="gray",
                        label=f"Barrière V0={V0}")
        ax.plot(x, np.abs(psi_libre[j, :]) ** 2, color="royalblue",
                label="|ψ libre|²")
        ax.plot(x, np.abs(psi_barr[j, :]) ** 2, color="tomato",
                label="|ψ tunnel|²")
        ax.set_title(titre)
        ax.set_xlabel("x")
        ax.set_ylabel("|ψ|²")
        ax.legend(fontsize=8)
        ax.grid(True, linestyle=":")

    plt.suptitle(
        f"Évolution : k0={k0}, a={a_b}, V0={V0}, |T|²={coeff_transmission(k0, a_b, V0):.2e}",
        fontsize=10,
    )
    plt.tight_layout()
    plt.savefig("/Partie_4/Figure_1_evolution.png", dpi=100)

    # --- Figure 2 : normes transmise / réfléchie ---
    mask_ref = x < x_b
    norme_tot_t = [norme(psi_barr[j, :], dx) for j in range(nt)]
    norme_tra_t = [np.sum(np.abs(psi_barr[j, mask_trans]) ** 2) * dx for j in range(nt)]
    norme_ref_t = [np.sum(np.abs(psi_barr[j, mask_ref]) ** 2) * dx for j in range(nt)]

    fig2, ax2 = plt.subplots(figsize=(9, 4))
    ax2.plot(t, norme_tot_t, color="black", label="Norme totale", linewidth=1.5)
    ax2.plot(t, norme_tra_t, color="green", label="Transmise (x > x_b+a)")
    ax2.plot(t, norme_ref_t, color="red", label="Réfléchie (x < x_b)")
    ax2.axhline(
        coeff_transmission(k0, a_b, V0),
        color="green",
        linestyle="--",
        alpha=0.7,
        label=f"|T|² analytique = {coeff_transmission(k0, a_b, V0):.2e}",
    )
    ax2.set_xlabel("t")
    ax2.set_ylabel("Probabilité")
    ax2.set_title("Transmission et réflexion en fonction du temps")
    ax2.legend(fontsize=9)
    ax2.grid(True, linestyle=":")
    plt.tight_layout()
    plt.savefig("/Partie_4/Figure_2_normes.png", dpi=100)

   # --- Figure 3 : influence de a ---
    fig3, axes3 = plt.subplots(1, 2, figsize=(12, 4))

    # Filtrer tau_t_num pour les valeurs fiables (a <= 1.0)
    idx_reliable = np.where(np.array(a_valeurs) <= 1.0)[0]
    a_reliable = np.array(a_valeurs)[idx_reliable]
    tau_t_num_reliable = np.array(tau_t_num_list)[idx_reliable]

    axes3[0].plot(a_valeurs, tau_0_list, "o-", color="royalblue",
                  label="τ₀ = a/v_g  (libre, linéaire)")
    axes3[0].plot(a_valeurs, tau_t_num_list, "s-", color="tomato", linestyle=":", alpha=0.5)
    axes3[0].plot(a_reliable, tau_t_num_reliable, "s-", color="tomato",
                  label="τₜ  (tunnel, numérique)")
    axes3[0].plot(a_valeurs, tau_t_th_list, "^--", color="darkorange",
                  label="τₜ  (Hartman, analytique)")
    axes3[0].set_xlabel("Largeur de la barrière a")
    axes3[0].set_ylabel("Temps de traversée")
    axes3[0].set_title(r'Temps de traversée en fonction de la largeur de la barrière $a$')
    axes3[0].legend(fontsize=9)
    axes3[0].grid(True, linestyle=":")

    axes3[1].semilogy(a_valeurs, T2_list, "o-", color="purple")
    axes3[1].set_xlabel("Largeur de la barrière a")
    axes3[1].set_ylabel("|T|²  (échelle log)")
    axes3[1].set_title("Probabilité de transmission vs a")
    axes3[1].grid(True, linestyle=":")

    plt.tight_layout()
    plt.savefig("/Partie_4/Figure_3_influence_a.png", dpi=100)

    # --- Figure 4 : influence de V0 ---
    if V0_valid:
        fig4, axes4 = plt.subplots(1, 2, figsize=(12, 4))
        axes4[0].plot(V0_valid, tau_t_V0_list, "o-", color="tomato",
                      label="τₜ (Hartman)")
        axes4[0].axhline(tau_0_th, color="royalblue", linestyle="--",
                         label=f"τ₀ = {tau_0_th:.3f}")
        axes4[0].set_xlabel("Hauteur de la barrière V0")
        axes4[0].set_ylabel("Temps de traversée τₜ")
        axes4[0].set_title("Influence de V0 sur le temps tunnel")
        axes4[0].legend(fontsize=9)
        axes4[0].grid(True, linestyle=":")

        axes4[1].semilogy(V0_valid, T2_V0_list, "o-", color="purple")
        axes4[1].set_xlabel("Hauteur de la barrière V0")
        axes4[1].set_ylabel("|T|²  (échelle log)")
        axes4[1].set_title("Probabilité de transmission vs V0")
        axes4[1].grid(True, linestyle=":")

        plt.tight_layout()
        plt.savefig("/Partie_4/Figure_4_influence_V0.png", dpi=100)

    if plt.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    main()
