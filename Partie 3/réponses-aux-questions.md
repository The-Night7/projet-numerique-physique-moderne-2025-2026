# 3 Résolution numérique de l’équation de Schrödinger

L’objectif de cette dernière étape est d’élaborer un premier algorithme de résolution de l’équation de Schrödinger qui permettra de déterminer l’évolution du paquet d’ondes initial [1]. Pour une particule libre et un paquet d’ondes gaussien, l’algorithme doit produire des résultats concordants avec la théorie [1].

## 3.1 Algorithme de dérivation

### 1. Dérivée première

**a. Rappeler la définition de la dérivée d’une fonction réelle en un point.**

**Réponse :** La dérivée d'une fonction réelle $f$ en un point $x$ est définie par la limite du taux d'accroissement lorsque l'intervalle $h$ tend vers 0 :
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

**b. Si cette fonction est un tableau 1d de `npts` éléments, écrire un algorithme (pseudo-code ou Python) calculant cette dérivée.**

**Réponse :** Pour un tableau NumPy `y` avec un pas constant `dx`, on utilise une approximation par différences finies [2]. Voici une implémentation vectorisée utilisant les "slices" de NumPy pour plus d'efficacité :

```python
import numpy as np

def derivee_premiere(y, dx):
    y = np.asarray(y)
    dy = np.zeros_like(y, dtype=np.result_type(y, float))

    dy[1:-1] = (y[2:] - y[:-2]) / (2 * dx)
    dy[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * dx)
    dy[-1] = (3 * y[-1] - 4 * y[-2] + y[-3]) / (2 * dx)
    return dy

```

**c. Écrire en Python une fonction renvoyant le carré $x²$ d’un nombre $x$ et une autre renvoyant $2x$. <br>**

**Réponse :**
```python
import numpy as np

def carre(x):
    return x**2

def double(x):
    return 2*x

```
**d. À l’aide de votre algorithme, calculer numériquement la dérivée de la fonction x² et comparer les valeurs obtenues avec celles renvoyées par la fonction 2x. Vous pouvez, par exemple, regarder l’erreur relative commise par votre algorithme. <br>**

**Réponse :** En appliquant l'algorithme à un tableau généré par np.linspace, on compare la dérivée numérique à la valeur théorique $2x$. L'erreur relative est d'ordre 1 par rapport au pas $dx$ pour un schéma progressif.Plus $dx$ est petit (nombre de points élevé), plus l'erreur diminue.

### 2. Reprendre les questions précédentes, mais pour la dérivée seconde.

**Réponse :**

Définition : La dérivée seconde $f′′(x)$ représente la dérivée de la dérivée première, mesurant la courbure de la fonction.

Algorithme : On utilise le schéma des différences finies centrées, plus précis:
```python
import numpy as np

def derivee_seconde(y, dx):
    y = np.asarray(y)
    d2y = np.zeros_like(y, dtype=np.result_type(y, float))

    d2y[1:-1] = (y[:-2] - 2 * y[1:-1] + y[2:]) / dx**2
    d2y[0] = (2 * y[0] - 5 * y[1] + 4 * y[2] - y[3]) / dx**2
    d2y[-1] = (2 * y[-1] - 5 * y[-2] + 4 * y[-3] - y[-4]) / dx**2
    return d2y
```
Comparaison : La dérivée seconde de $x²$
  est la constante 2. L'algorithme renverra une valeur quasi identique à 2 pour les points intérieurs, avec une erreur d'ordre $dx²$.

## 3.2 Algorithme pour l’équation de Schrödinger

L’équation de Schrödinger décrit l’évolution de la fonction d’onde dans le temps et l’espace. Dès lors, la fonction d’onde ne peut pas être stockée dans un tableau 1d, mais un tableau 4d. Dans la mesure où nous n’étudions que des problèmes à une dimension d’espace, des tableaux 2d seront suffisants.

### 1. Rappeler l’équation de Schrödinger à une dimension d’espace pour une particule dans un potentiel constant `V0`.

**Réponse :**

   Pour une particule de masse `m` se déplaçant selon l’axe `(Ox)` dans un potentiel constant `V0`, l’équation de Schrödinger s’écrit :

   $$
   i\hbar \frac{\partial \Psi(x,t)}{\partial t}
   =
   -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi(x,t)}{\partial x^2}
   + V_0 \Psi(x,t).
   $$

   Dans le cas particulier d’une particule libre, on a `V0 = 0`, donc :

   $$
   i\hbar \frac{\partial \Psi(x,t)}{\partial t}
   =
   -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi(x,t)}{\partial x^2}.
   $$

### 2. Définir une fonction d’onde (tableau 2d) contenant `nx` lignes et `nt` colonnes. La première ligne doit contenir un paquet d’ondes gaussien à instant donné et le reste du tableau doit contenir des zéros (ou mieux, des nombres aléatoires `empty`).

**Réponse :**

   En pratique, il est plus cohérent de stocker la fonction d’onde sous la forme `psi[j, i] = psi(t_j, x_i)`, donc dans un tableau de taille `(nt, nx)` :

   - chaque **ligne** correspond à un instant ;
   - chaque **colonne** correspond à une position.

   Ainsi, la première ligne `psi[0, :]` contient naturellement l’état initial à `t = 0`.

   ```python
   import numpy as np

   psi = np.zeros((nt, nx), dtype=complex)
   psi[0, :] = gauss_wp(k0, a, x, 0)
   ```

   Si l’on veut suivre strictement l’idée de l’énoncé, on peut dire que la première ligne contient le paquet d’ondes gaussien initial et que toutes les autres cases sont initialisées à zéro en attendant le calcul de l’évolution temporelle.

### 3. Définir (`numpy.linspace`) des tableaux 1d pour les intervalles d’espace `x` et de temps `t`.

**Réponse :**

   On définit un intervalle spatial `[xmin, xmax]` discrétisé en `nx` points, et un intervalle temporel `[tmin, tmax]` discrétisé en `nt` points :

   ```python
   x = np.linspace(xmin, xmax, nx)
   t = np.linspace(tmin, tmax, nt)
   ```

   Les pas associés sont :

   ```python
   dx = x[1] - x[0]
   dt = t[1] - t[0]
   ```

   Ces deux pas `dx` et `dt` sont essentiels pour écrire les dérivées numériques.

### 4. Écrire un algorithme combinant les dérivées première par rapport au temps et seconde par rapport à l’espace pour décrire l’évolution de la fonction d’ondes initiale (paquet d’ondes dans notre cas) selon l’équation de Schrödinger.

**Réponse :**

Une discrétisation directe de l’équation de Schrödinger peut se faire avec des différences finies, mais un schéma d’Euler explicite devient vite instable. Dans le code, on utilise donc un schéma de **Crank-Nicolson**, plus adapté, car il conserve beaucoup mieux la norme de la fonction d’onde.

On part de

$$
i\hbar \frac{\partial \Psi}{\partial t}
=
-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}
+ V_0 \Psi.
$$

La dérivée seconde spatiale est approchée par une différence centrée, et l’évolution temporelle est écrite à mi-chemin entre les instants `t_j` et `t_{j+1}`. Cela conduit à un système linéaire tridiagonal à résoudre à chaque pas de temps.

Sous forme algorithmique :

```python
psi = np.zeros((nt, nx), dtype=complex)
psi[0, :] = GaussWP(k0, a, x, 0.0)

for j in range(nt - 1):
    # Construction du membre de droite
    second_membre = ...

    # Resolution du systeme tridiagonal
    psi[j + 1, 1:-1] = resoudre_tridiagonal(a_mat, b_mat, c_mat, second_membre)

    # Conditions aux bords
    psi[j + 1, 0] = 0.0
    psi[j + 1, -1] = 0.0
```

L’idée importante est la suivante :

- on connaît `psi[j, :]` à l’instant `t_j` ;
- on calcule `psi[j+1, :]` à l’instant suivant ;
- la dérivée seconde en espace contrôle l’étalement du paquet ;
- le potentiel `V0` ajoute une phase et modifie l’évolution.




### 5. Confronter les résultats de l’algorithme, dans le cas `V0 = 0`, avec le programme `PaquetOndes.py`. La comparaison peut, dans un premier temps, se faire sans représenter les paquets d’ondes.

**Réponse :**

Dans le cas libre `V0 = 0`, la solution numérique doit rester proche du paquet d’ondes gaussien théorique obtenu dans la partie 2.

La comparaison peut se faire sur plusieurs points :

- la norme `\int |\Psi|^2 dx` doit rester proche de `1` ;
- le paquet doit se déplacer dans le bon sens avec une vitesse cohérente avec `v_g = \hbar k_0 / m` ;
- le paquet doit s’étaler progressivement ;
- l’écart entre la solution numérique et la solution théorique doit rester faible.

Dans le script, cette comparaison est faite en calculant :

```python
psi_th_0 = GaussWP(k0, a, x, t[0])
psi_th_f = GaussWP(k0, a, x, t[-1])

erreur_initiale = np.max(np.abs(psi_num[0, :] - psi_th_0))
erreur_finale = np.max(np.abs(psi_num[-1, :] - psi_th_f))
```

**Résultats numériques obtenus** (avec `nx=1200`, `nt=800`, `k0=5.0`, `a=0.5`, `tmax=1.0`) :

```
Verification des derivees sur x^2
erreur max derivee premiere : 4.810e-12
erreur max derivee seconde  : 7.595e-10

Comparaison paquet d’ondes
norme initiale numerique : 1.000000
norme finale numerique   : 1.000000
erreur max a t=0         : 0.000e+00
erreur max a t=t_final   : 2.375e-02
```

**Interprétation :**

- Les erreurs sur les dérivées ($\sim 10^{-12}$ et $\sim 10^{-10}$) sont proches de la précision machine, ce qui valide complètement l’algorithme de dérivation.
- La norme se conserve à $10^{-6}$ près entre $t=0$ et $t=t_{\rm final}$ : le schéma de Crank-Nicolson préserve bien la norme (propriété essentielle pour une équation quantique).
- L’erreur finale de $2.4 \times 10^{-2}$ représente l’écart maximum entre la solution numérique et le paquet gaussien théorique à $t=1.0$. Cet écart est dû à la discrétisation spatiale et temporelle, mais reste petit devant les amplitudes en jeu ($\sim 1$), ce qui valide le comportement général de l’algorithme.
