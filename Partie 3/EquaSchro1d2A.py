import numpy as np
import matplotlib.pyplot as plt


# On travaille en unites adimensionnees pour eviter les problemes
# numeriques deja rencontres en partie 2 avec les constantes SI.
hbar = 1.0
m = 1.0


# ============================================================
# 3.1.1.b - Derivee premiere numerique
# ============================================================
def derivee_premiere(y, dx):
    """Approximation numerique de la derivee premiere d'un tableau 1D."""
    y = np.asarray(y)
    dy = np.zeros_like(y, dtype=np.result_type(y, float))

    # Schema centre sur les points interieurs, plus precis que
    # la difference simple vers l'avant.
    dy[1:-1] = (y[2:] - y[:-2]) / (2 * dx)

    # Aux bords, on ne peut pas centrer le schema : on utilise donc
    # une formule decalee d'ordre 2.
    dy[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * dx)
    dy[-1] = (3 * y[-1] - 4 * y[-2] + y[-3]) / (2 * dx)
    return dy


# ============================================================
# 3.1.1.c - Fonctions tests
# ============================================================
def carre(x):
    return x**2


def double(x):
    return 2 * x


# ============================================================
# 3.1.2 - Derivee seconde numerique
# ============================================================
def derivee_seconde(y, dx):
    """Approximation numerique de la derivee seconde d'un tableau 1D."""
    y = np.asarray(y)
    d2y = np.zeros_like(y, dtype=np.result_type(y, float))

    # Difference centree classique sur les points interieurs.
    d2y[1:-1] = (y[:-2] - 2 * y[1:-1] + y[2:]) / dx**2

    # Formules decalees aux bords pour eviter de sortir du tableau.
    d2y[0] = (2 * y[0] - 5 * y[1] + 4 * y[2] - y[3]) / dx**2
    d2y[-1] = (2 * y[-1] - 5 * y[-2] + 4 * y[-3] - y[-4]) / dx**2
    return d2y


# ============================================================
# Partie 2 - Reprise du paquet d'ondes gaussien
# ============================================================
def GaussWP(k0, a, x, t):
    """
    Paquet d'ondes gaussien libre.

    On reprend ici la formule utilisee en partie 2. La fonction est
    redefinie localement au lieu d'etre importee directement, car le
    fichier de la partie 2 contient aussi du code d'affichage execute
    des l'import.
    """
    alpha = a + 1j * (hbar * t) / (2 * m)
    norm = (2 * a / np.pi) ** 0.25 / np.sqrt(2 * alpha)
    vg = (hbar * k0) / m

    phase = np.exp(1j * (k0 * x - (hbar * k0**2 / (2 * m)) * t))
    envelope = np.exp(-((x - vg * t) ** 2) / (4 * alpha))
    return norm * envelope * phase


# ============================================================
# Outil numerique - Resolution d'un systeme tridiagonal
# ============================================================
def resoudre_tridiagonal(a, b, c, d):
    """
    Methode de Thomas.

    Elle sert a resoudre rapidement le systeme lineaire tridiagonal
    produit par le schema de Crank-Nicolson.
    """
    n = len(d)
    ac = np.array(a, dtype=complex, copy=True)
    bc = np.array(b, dtype=complex, copy=True)
    cc = np.array(c, dtype=complex, copy=True)
    dc = np.array(d, dtype=complex, copy=True)

    for i in range(1, n):
        facteur = ac[i - 1] / bc[i - 1]
        bc[i] = bc[i] - facteur * cc[i - 1]
        dc[i] = dc[i] - facteur * dc[i - 1]

    x = np.zeros(n, dtype=complex)
    x[-1] = dc[-1] / bc[-1]

    for i in range(n - 2, -1, -1):
        x[i] = (dc[i] - cc[i] * x[i + 1]) / bc[i]

    return x


# ============================================================
# 3.2 - Evolution temporelle selon l'equation de Schrodinger
# ============================================================
def evolution_schrodinger(nx, nt, xmin, xmax, tmin, tmax, k0, a, V0):
    """
    Calcule psi(x,t) sur une grille 1D.

    Convention de stockage :
    - axe 0 : le temps
    - axe 1 : l'espace

    Donc psi[j, i] = psi(t_j, x_i).

    Remarque :
    le premier essai naturel est souvent Euler explicite, mais ce schema
    diverge vite pour l'equation de Schrodinger. On utilise donc ici
    Crank-Nicolson, qui conserve beaucoup mieux la norme.
    """
    x = np.linspace(xmin, xmax, nx)
    t = np.linspace(tmin, tmax, nt)
    dx = x[1] - x[0]
    dt = t[1] - t[0]

    # Tableau 2D de la fonction d'onde :
    # chaque ligne correspond a un instant donne.
    psi = np.zeros((nt, nx), dtype=complex)
    psi[0, :] = GaussWP(k0, a, x, 0.0)

    # Nombre de points spatiaux interieurs : on impose psi = 0 aux bords.
    n_interieur = nx - 2
    r = 1j * hbar * dt / (4 * m * dx**2)
    s = 1j * V0 * dt / (2 * hbar)

    # Matrice du membre de gauche du schema de Crank-Nicolson.
    a_mat = np.full(n_interieur - 1, -r, dtype=complex)
    b_mat = np.full(n_interieur, 1 + 2 * r + s, dtype=complex)
    c_mat = np.full(n_interieur - 1, -r, dtype=complex)

    for j in range(nt - 1):
        # On construit le membre de droite a partir de l'etat a l'instant t_j.
        psi_interieur = psi[j, 1:-1]
        second_membre = (
            (1 - 2 * r - s) * psi_interieur
            + r * psi[j, :-2]
            + r * psi[j, 2:]
        )

        # Resolution du systeme tridiagonal pour obtenir psi au temps suivant.
        psi[j + 1, 1:-1] = resoudre_tridiagonal(a_mat, b_mat, c_mat, second_membre)

        # Conditions aux bords : la fonction d'onde est forcee a zero
        # aux deux extremites de la boite numerique.
        psi[j + 1, 0] = 0.0
        psi[j + 1, -1] = 0.0

    return x, t, psi, dx


def norme(psi_x, dx):
    """Approximation discrete de la norme int |psi|^2 dx."""
    return np.sum(np.abs(psi_x) ** 2) * dx


def main():
    # ========================================================
    # Parametres numeriques de la grille
    # ========================================================
    nx = 1200
    nt = 800
    xmin, xmax = -20.0, 20.0
    tmin, tmax = 0.0, 1.0

    # ========================================================
    # Parametres physiques du paquet initial
    # ========================================================
    k0 = 5.0
    a = 0.5
    V0 = 0.0

    # Calcul de l'evolution numerique de la fonction d'onde.
    x, t, psi_num, dx = evolution_schrodinger(
        nx=nx,
        nt=nt,
        xmin=xmin,
        xmax=xmax,
        tmin=tmin,
        tmax=tmax,
        k0=k0,
        a=a,
        V0=V0,
    )

    # Solutions theoriques de reference pour comparer avec le calcul numerique.
    psi_th_0 = GaussWP(k0, a, x, t[0])
    psi_th_f = GaussWP(k0, a, x, t[-1])

    erreur_initiale = np.max(np.abs(psi_num[0, :] - psi_th_0))
    erreur_finale = np.max(np.abs(psi_num[-1, :] - psi_th_f))

    # --------------------------------------------------------
    # Verification de la partie 3.1 sur la fonction test x^2
    # --------------------------------------------------------
    print("Verification des derivees sur x^2")
    y = carre(x)
    print(f"erreur max derivee premiere : {np.max(np.abs(derivee_premiere(y, x[1] - x[0]) - double(x))):.3e}")
    print(f"erreur max derivee seconde  : {np.max(np.abs(derivee_seconde(y, x[1] - x[0]) - 2.0)):.3e}")

    # --------------------------------------------------------
    # Comparaison numerique / theorique pour la partie 3.2
    # --------------------------------------------------------
    print("\nComparaison paquet d'ondes")
    print(f"norme initiale numerique : {norme(psi_num[0, :], dx):.6f}")
    print(f"norme finale numerique   : {norme(psi_num[-1, :], dx):.6f}")
    print(f"erreur max a t=0         : {erreur_initiale:.3e}")
    print(f"erreur max a t=t_final   : {erreur_finale:.3e}")

    # Les deux graphes servent a voir :
    # 1. que l'etat initial numerique coincide avec le paquet theorique ;
    # 2. qu'a temps final la densite de probabilite reste proche du resultat attendu.
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(x, np.real(psi_num[0, :]), label="Re(psi numerique), t=0", color="royalblue")
    axes[0].plot(x, np.real(psi_th_0), label="Re(psi theorique), t=0", color="tomato", linestyle="--")
    axes[0].set_ylabel("Partie reelle")
    axes[0].legend()
    axes[0].grid(True, linestyle=":")

    axes[1].plot(x, np.abs(psi_num[-1, :]) ** 2, label="|psi numerique|^2, t final", color="purple")
    axes[1].plot(x, np.abs(psi_th_f) ** 2, label="|psi theorique|^2, t final", color="darkorange", linestyle="--")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("Densite de probabilite")
    axes[1].legend()
    axes[1].grid(True, linestyle=":")

    plt.tight_layout()
    if plt.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    main()
