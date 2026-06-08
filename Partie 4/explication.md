Le programme `EffetTunnel1d2A.py` étend le solveur de la partie 3 à un potentiel spatialement variable (barrière rectangulaire) pour étudier l'effet tunnel et les temps de traversée.

---

### Constantes physiques

Le programme utilise des unités adimensionnées : `hbar = 1.0` et `m = 1.0`, comme en partie 3.

---

### `GaussWP_centre(k0, a_wp, x, x0, t)`

Paquet d'ondes gaussien dont le centre est en `x0` à `t=0`. La différence avec la partie 3 est que le point de départ n'est pas forcément l'origine : on substitue `x - x0` à `x` dans l'exponentielle de la phase et `x - x0 - vg*t` dans l'enveloppe.

**k0** : vecteur d'onde moyen → fixe l'impulsion et la vitesse de groupe.<br>
**a_wp** : largeur initiale du paquet en espace réel.<br>
**x0** : position du centre à t=0, typiquement à gauche de la barrière.<br>

---

### `potentiel_barriere(x, x_b, a_b, V0)`

Retourne un tableau de même taille que `x` valant `V0` dans l'intervalle `[x_b, x_b + a_b]` et `0` ailleurs. Ce profil de potentiel est directement injecté dans la matrice de Crank-Nicolson.

**x_b** : bord gauche de la barrière.<br>
**a_b** : largeur de la barrière (distance `a` du projet).<br>
**V0** : hauteur de la barrière.<br>

---

### `resoudre_tridiagonal(a, b, c, d)`

Identique à la partie 3. Méthode de Thomas (élimination de Gauss sur un système tridiagonal), utilisée à chaque pas de temps.

---

### `evolution_schrodinger(nx, nt, xmin, xmax, tmin, tmax, k0, a_wp, x0, x_b, a_b, V0)`

Cœur du programme. Résout l'équation de Schrödinger par Crank-Nicolson avec un potentiel variable en espace.

**Différence par rapport à la partie 3 :**
En partie 3, le potentiel `V0` était uniforme, ce qui donnait un coefficient `s` identique pour tous les points intérieurs. Ici, `V(x_i)` varie : le vecteur `s_int = i*V_int*dt/(2*hbar)` est différent à chaque position, donc la diagonale principale :
```
b_mat[i] = 1 + 2*r + s_int[i]
```
est un tableau (non une constante). Le second membre change aussi en conséquence :
```
rhs[i] = (1 - 2*r - s_int[i])*psi_int[i] + r*psi[j, i-1] + r*psi[j, i+2]
```
Tout le reste (méthode de Thomas, conditions aux bords nulles) reste identique.

**Retour :** `x, t, psi, dx` — grilles et tableau 2D de la fonction d'onde.

---

### `norme(psi_x, dx)`

Approximation de $\int |\psi|^2 dx$ par somme discrète. Doit rester proche de 1 (conservation de la norme par Crank-Nicolson).

---

### `coeff_transmission(k0, a_b, V0)`

Calcule la probabilité de transmission analytique $|T|^2$ pour une barrière rectangulaire.

**Pour E < V0 (effet tunnel) :**
$$|T|^2 = \frac{1}{1 + \dfrac{(\kappa^2 + k_0^2)^2}{4k_0^2\kappa^2}\sinh^2(\kappa a)}$$
avec $\kappa = \sqrt{2m(V_0-E)}/\hbar$.

**Pour E > V0 (au-dessus de la barrière) :**
$$|T|^2 = \frac{1}{1 + \dfrac{(k_0^2 - k_2^2)^2}{4k_0^2 k_2^2}\sin^2(k_2 a)}$$
avec $k_2 = \sqrt{2m(E-V_0)}/\hbar$.

---

### `tau_libre(k0, a_b)`

Retourne $\tau_{0,\rm th} = m\,a / (\hbar\,k_0)$, le temps analytique que met le pic du paquet gaussien libre pour parcourir la distance `a_b` à la vitesse de groupe $v_g = \hbar k_0/m$.

---

### `phase_transmission(k, a_b, V0)`

Phase $\varphi_T(k) = \arg(T(k))$ pour le régime tunnel ($E_k < V_0$) :
$$\varphi_T(k) = -k\,a - \arctan\!\left[\frac{\kappa^2-k^2}{2k\kappa}\tanh(\kappa a)\right]$$

Cette phase encode le déphasage acquis par chaque composante spectrale en traversant la barrière.

---

### `decalage_groupe(k0, a_b, V0)`

Calcule le décalage de groupe $\tau_g = (1/v_g)\,d\varphi_T/dk|_{k_0}$ par différentiation numérique à deux points (pas `dk = 1e-6`).

**Interprétation :** Si $\tau_g < 0$, le pic transmis est en avance sur une particule libre de même largeur spectrale : c'est le cœur de l'effet Hartman.

---

### `tau_tunnel(k0, a_b, V0)`

Temps de traversée physique de la barrière :
$$\tau_{t,\rm th} = \tau_{0,\rm th} + \tau_g = \frac{a}{v_g} + \frac{1}{v_g}\frac{d\varphi_T}{dk}$$

Dans le régime opaque ($\kappa a \gg 1$), $\tau_{t,\rm th}$ converge vers une constante indépendante de `a_b` : **effet Hartman**.

---

### `temps_pic_en(psi, t, idx_x)`

Retourne l'instant $t^*$ où $|\psi(x_{\rm idx},\, t)|^2$ est maximal. Utilisé pour :
- mesurer $t_{\rm entrée}$ (pic libre au bord gauche de la barrière) ;
- mesurer $t_{\rm sortie}$ (pic libre ou tunnel au bord droit).

La différence $t_{\rm sortie} - t_{\rm entrée}$ donne $\tau_{0,\rm num}$ ou $\tau_{t,\rm num}$ selon la simulation.

---

### Fonction `main()`

#### Paramètres physiques et de grille

**nx = 1500, nt = 3000** : grille spatio-temporelle.<br>
**xmin, xmax = −30, 30** : domaine spatial large pour éviter les réflexions aux bords.<br>
**tmin, tmax = 0, 6** : intervalle temporel suffisant pour que le paquet traverse entièrement la barrière.<br>
**k0 = 5** : énergie $E = 12.5$.<br>
**V0 = 15** : $V_0 > E$, régime tunnel, $|T|^2 \approx 2.5\%$.<br>
**x0 = −10** : le paquet démarre loin à gauche, évitant toute interaction initiale avec la barrière.<br>

#### Mesure des temps (4.1.b-c)

Deux simulations sont lancées :
1. `V0 = 0` → mesure de $\tau_{0,\rm num}$ (validation avec $\tau_{0,\rm th} = a/v_g$).
2. `V0 = 15` → mesure de $\tau_{t,\rm num}$.

Le fait que $\tau_{t,\rm num} < \tau_{0,\rm num}$ confirme l'effet Hartman numériquement.

#### Étude de l'influence de $a$ (4.1.d)

Six simulations supplémentaires pour `a` allant de 0.5 à 3.0. Les résultats analytiques montrent :
- $\tau_0$ croît linéairement avec $a$.
- $\tau_{t,\rm th}$ sature autour de 0.179 pour $\kappa a \gtrsim 3$.
- $|T|^2$ décroît exponentiellement.

#### Étude de l'influence de $V_0$ (4.1.e)

Résultats analytiques pour $V_0$ croissant : plus la barrière est haute, plus le temps apparent diminue (et plus $|T|^2$ chute).

#### Figures produites

**Figure 1** (`Figure_1_evolution.png`) : trois instantanés de $|\psi|^2$ à $t=0$, mi-simulation, et $t_{\rm final}$, comparant le cas libre et le cas tunnel. On voit la séparation du paquet en une partie réfléchie et une partie transmise (petite).

**Figure 2** (`Figure_2_normes.png`) : évolution temporelle des probabilités totale, transmise ($x > x_b + a$) et réfléchie ($x < x_b$). La norme totale reste constante ; la norme transmise converge vers $|T|^2$ analytique.

**Figure 3** (`Figure_3_influence_a.png`) : à gauche, $\tau_0$, $\tau_{t,\rm num}$ et $\tau_{t,\rm th}$ en fonction de $a$ — illustration de la saturation (effet Hartman). À droite, $|T|^2$ en échelle logarithmique vs $a$ — décroissance exponentielle.

**Figure 4** (`Figure_4_influence_V0.png`) : temps tunnel et $|T|^2$ en fonction de $V_0$.
