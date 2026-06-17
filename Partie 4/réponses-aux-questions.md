# 4 Projet – Effet tunnel et temps de traversée

## 4.1 Objectif

Le but est de déterminer le temps nécessaire à une particule pour franchir une barrière rectangulaire de potentiel de hauteur $V_0 > 0$ par effet tunnel.

L'état initial est un paquet d'ondes gaussien de vecteur d'onde moyen $k_0$, centré en $x_0 < 0$, se déplaçant vers la barrière placée entre $x_b$ et $x_b + a$.

**Paramètres utilisés :**
- Unités adimensionnées : $\hbar = m = 1$
- $k_0 = 5$, $a_{\rm wp} = 1$ (largeur du paquet), $x_0 = -10$
- Barrière : $x_b = 0$, $a = 1$, $V_0 = 15$
- Énergie : $E = k_0^2 / 2 = 12.5 < V_0$ → **effet tunnel**
- Vitesse de groupe : $v_g = k_0/m = 5$
- $\kappa = \sqrt{2m(V_0-E)}/\hbar = \sqrt{5} \approx 2.236$

---

## Aspects numériques

### 4.1.a – Programme de résolution avec barrière

Le programme `EffetTunnel1d2A.py` adapte le schéma de Crank-Nicolson de la partie 3 à un **potentiel spatialement variable**.

La barrière rectangulaire est définie par :
$$V(x) = V_0 \cdot \mathbf{1}_{[x_b,\, x_b + a]}(x)$$

La seule différence par rapport à la partie 3 est que la diagonale principale $b_i$ du système linéaire dépend maintenant du point $i$ :
$$b_i = 1 + 2r + s_i, \quad s_i = \frac{i\,V(x_i)\,\Delta t}{2\hbar}$$

La simulation produit trois régimes visibles :
1. **Avant la barrière** ($t$ petit) : le paquet se déplace librement vers la droite.
2. **Interaction avec la barrière** : une partie du paquet est réfléchie vers la gauche, une partie (exponentiellement petite) est transmise.
3. **Après la barrière** ($t$ grand) : un paquet réfléchi et un paquet transmis coexistent.

La norme totale est conservée à $10^{-5}$ près (propriété du schéma de Crank-Nicolson).

### 4.1.b – Temps de traversée libre $\tau_{0,\rm num}$

Pour $V_0 = 0$, le paquet se propage librement. On mesure le temps que met le pic de $|\psi(x,t)|^2$ pour aller de $x_b$ à $x_b + a$ :

$$\tau_{0,\rm num} = t_{\rm sortie} - t_{\rm entrée}$$

où $t_{\rm entrée}$ (resp. $t_{\rm sortie}$) est l'instant où $|\psi(x_b, t)|^2$ (resp. $|\psi(x_b+a, t)|^2$) est maximal.

**Résultat analytique attendu :**
$$\tau_{0,\rm th} = \frac{a}{v_g} = \frac{a\,m}{\hbar\,k_0} = \frac{1}{5} = 0.200$$

La simulation confirme $\tau_{0,\rm num} \approx 0.200$.

### 4.1.c – Temps de traversée tunnel $\tau_{t,\rm num}$

Pour $V_0 = 15 > E = 12.5$, on mesure l'instant où le pic de la **partie transmise** de $|\psi|^2$ passe en $x = x_b + a$ :

$$\tau_{t,\rm num} = t_{\rm sortie,\,tunnel} - t_{\rm entrée}$$

**Résultats numériques obtenus :**

```
t_entree      = 1.999  (attendu 2.000)
t_sortie libre= 2.191  (attendu 2.200)
τ_{0,num}     = 0.192      τ_{0,th} = 0.200

t_sortie tunnel = 2.111
τ_{t,num}       = 0.112
τ_{t,th} (Hartman) = 0.168    →  τ_t/τ_0 = 0.841 < 1

Norme initiale   : 1.000000
Norme finale     : 1.000000
Norme transmise  : ~2.5 × 10⁻²  (conforme à |T|² analytique)
```

$\tau_{t,\rm num} = 0.112 < \tau_{0,\rm num} = 0.192$ : la particule semble traverser la barrière **plus vite** que la particule libre ne traverse la même distance. C'est l'**effet Hartman** (voir partie analytique).

La probabilité de transmission est $|T|^2 \approx 2.5 \times 10^{-2}$, donc environ 97.5 % du paquet est réfléchi. La norme est conservée à mieux que $10^{-5}$ près par le schéma de Crank-Nicolson.

**Remarque :** Pour les grandes valeurs de $a$ ($|T|^2 \lesssim 10^{-4}$), la détection numérique du pic transmis est limitée par la faiblesse du signal ; les valeurs analytiques (effet Hartman) restent les plus fiables.

### 4.1.d – Influence de la largeur $a$

| $a$ | $\kappa\cdot a$ | $\tau_0 = a/v_g$ | $\tau_{t,\rm th}$ | $\tau_{t,\rm th}/\tau_0$ | $\|T\|^2$ |
|-----|----------|-----------|------------|-------------|----------|
| 0.5 | 1.12     | 0.100     | 0.125      | 1.25        | 2.3×10⁻¹ |
| 1.0 | 2.24     | 0.200     | 0.168      | 0.84        | 2.5×10⁻² |
| 1.5 | 3.35     | 0.300     | 0.177      | 0.59        | 2.7×10⁻³ |
| 2.0 | 4.47     | 0.400     | 0.179      | 0.45        | 2.9×10⁻⁴ |
| 2.5 | 5.59     | 0.500     | 0.179      | 0.36        | 3.1×10⁻⁵ |
| 3.0 | 6.71     | 0.600     | 0.179      | 0.30        | 3.3×10⁻⁶ |

**Observations :**
- $\tau_0 = a/v_g$ croît linéairement avec $a$.
- $\tau_{t,\rm th}$ croît d'abord pour les petites barrières ($\kappa a \lesssim 2$), puis **sature** autour de $\approx 0.179$ pour $\kappa a \gtrsim 3$.
- Dans le régime opaque ($\kappa a \gg 1$), $\tau_{t,\rm th}$ devient **indépendant de $a$** : c'est l'**effet Hartman**. Cela signifie que la barrière est traversée en un temps qui ne dépend pas de son épaisseur, si celle-ci est suffisamment grande.
- Simultanément, $|T|^2$ décroît exponentiellement avec $a$ : $|T|^2 \approx 16(E/V_0)(1-E/V_0)\,e^{-2\kappa a}$ pour $\kappa a \gg 1$.

### 4.1.e – Influence de $V_0$

| $V_0$ | $\kappa\cdot a$ | $\tau_{t,\rm th}$ | $\|T\|^2$ |
|--------|---------|------------|----------|
| 13.5   | 1.41    | 0.218      | 6.8×10⁻² |
| 14.0   | 1.73    | 0.198      | 4.9×10⁻² |
| 15.0   | 2.24    | 0.168      | 2.5×10⁻² |
| 17.0   | 3.00    | 0.132      | 7.7×10⁻³ |
| 20.0   | 3.87    | 0.103      | 1.6×10⁻³ |
| 25.0   | 5.00    | 0.080      | 1.8×10⁻⁴ |

**Observations :**
- Quand $V_0$ augmente (à $a$ fixé), $\kappa$ augmente, et $\tau_{t,\rm th}$ **diminue**.
- Une barrière plus haute est franchie en moins de temps (apparent) ! Ce résultat contre-intuitif est une autre manifestation de l'effet Hartman.
- La probabilité de transmission $|T|^2$ décroît exponentiellement avec $V_0$.

---

## 4.2 – Comparaison avec le cas classique

**Cas classique $E > V_0$ :**
La particule passe au-dessus de la barrière avec une vitesse réduite :
$$v_{\rm classique} = \sqrt{\frac{2(E - V_0)}{m}}$$
Le temps classique pour traverser la barrière de largeur $a$ est :
$$\tau_{\rm class,\,sup} = \frac{a}{v_{\rm classique}} = \frac{a}{\sqrt{2(E-V_0)}} > \tau_0$$
car $v_{\rm classique} < v_g$.

**Cas classique $0 < E < V_0$ :**
La particule est intégralement **réfléchie** à la barrière : elle ne la traverse pas. Classiquement, $\tau_{\rm traversée} = +\infty$ (ou non défini).

**Cas quantique $0 < E < V_0$ :**
La particule peut traverser la barrière par **effet tunnel** avec une probabilité $|T|^2 > 0$. Le temps de traversée apparent $\tau_{t,\rm th} \approx 0.17$ est même **inférieur** à $\tau_0 = 0.2$ pour les paramètres choisis.

**Résumé comparatif :**

| Cas | $E$ vs $V_0$ | Transmission | Temps de traversée |
|-----|-------------|-------------|-------------------|
| Classique (au-dessus) | $E > V_0$ | totale (|T|=1) | $> \tau_0$ (ralentissement) |
| Classique (sous barrière) | $E < V_0$ | nulle | non défini |
| Quantique (effet tunnel) | $E < V_0$ | partielle ($0 < \|T\|^2 \ll 1$) | $\tau_{t,\rm th} < \tau_0$ (apparent) |

---

## Aspects analytiques

### 4.3.a – États stationnaires et coefficients de transmission/réflexion

On cherche les solutions stationnaires $\psi(x) e^{-iEt/\hbar}$ pour une barrière rectangulaire :

**Région I** ($x < 0$) : $\psi_I = e^{ikx} + R\,e^{-ikx}$, onde incidente + réfléchie, avec $k = \sqrt{2mE}/\hbar$.

**Région II** ($0 < x < a$, sous la barrière) : $\psi_{II} = A\,e^{\kappa x} + B\,e^{-\kappa x}$, onde évanescente, avec $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.

**Région III** ($x > a$) : $\psi_{III} = T\,e^{ikx}$, onde transmise uniquement.

En appliquant les conditions de raccordement en $x = 0$ et $x = a$ ($\psi$ et $\psi'$ continues) :

$$T(k) = \frac{e^{-ika}}{\cosh(\kappa a) + i\dfrac{\kappa^2 - k^2}{2k\kappa}\sinh(\kappa a)}$$

La **probabilité de transmission** est :
$$|T|^2 = \frac{1}{1 + \dfrac{(\kappa^2 + k^2)^2}{4k^2\kappa^2}\sinh^2(\kappa a)}$$

La **probabilité de réflexion** est :
$$|R|^2 = 1 - |T|^2$$

Dans la limite $\kappa a \gg 1$ (régime opaque) :
$$|T|^2 \approx \frac{16k^2\kappa^2}{(k^2 + \kappa^2)^2}\,e^{-2\kappa a}$$

La transmission décroît **exponentiellement** avec la largeur $a$ et avec $\sqrt{V_0 - E}$.

### 4.3.b – Vitesse de phase et de groupe du paquet gaussien

Pour une particule libre de relation de dispersion $\omega(k) = \hbar k^2 / (2m)$ :

$$v_\varphi = \frac{\omega}{k} = \frac{\hbar k}{2m}$$
$$v_g = \frac{d\omega}{dk} = \frac{\hbar k}{m} = 2\,v_\varphi$$

Pour le paquet gaussien centré en $k_0$ :
$$v_g = \frac{\hbar k_0}{m}$$

C'est la vitesse de déplacement du centre du paquet. Avec nos paramètres ($k_0 = 5$, $\hbar = m = 1$) : $v_g = 5$.

### 4.3.c – Temps de traversée libre $\tau_{0,\rm th}$

Pour une particule libre (état gaussien) qui parcourt une distance $a$ :
$$\tau_{0,\rm th} = \frac{a}{v_g} = \frac{m\,a}{\hbar\,k_0}$$

Avec nos paramètres : $\tau_{0,\rm th} = 1/5 = 0.200$.

### 4.3.d – Influence de $a$ sur $\tau_{0,\rm th}$

$$\tau_{0,\rm th} \propto a$$

Le temps de traversée libre est **linéaire** en $a$. Doubler la largeur de la barrière double le temps de traversée libre.

### 4.3.e – Expression du paquet d'ondes transmis

Le paquet transmis est obtenu en pondérant chaque composante de Fourier $g(k)$ par le coefficient $T(k)$ :

$$\psi_{\rm transmis}(x, t) = \frac{1}{\sqrt{2\pi}} \int g(k)\,T(k)\,e^{i(kx - \omega(k)t)}\,dk$$

Pour un paquet étroit en $k$ (large en espace), on peut développer $T(k)$ autour de $k_0$ :
$$T(k) \approx |T(k_0)|\,e^{i\varphi_T(k_0)}\,e^{i\varphi'_T(k_0)(k - k_0)}$$

où $\varphi'_T = d\varphi_T/dk$.

On obtient alors :
$$\psi_{\rm transmis}(x, t) \approx |T(k_0)|\,e^{i\varphi_T(k_0)}\;\psi_{\rm libre}\!\left(x - \varphi'_T(k_0),\; t\right)$$

Le paquet transmis ressemble au paquet libre **décalé spatialement** de $\varphi'_T(k_0)$, qui est positif (avance) dans le régime tunnel profond. Ce décalage correspond à un avancement temporel $\Delta t = \varphi'_T(k_0)/v_g$.

### 4.3.f – Temps de traversée tunnel $\tau_{t,\rm th}$

La phase de $T(k)$ vaut :
$$\varphi_T(k) = -ka - \arctan\!\left[\frac{\kappa^2 - k^2}{2k\kappa}\tanh(\kappa a)\right]$$

Le **décalage de groupe** (group delay) est :
$$\tau_g = \frac{1}{v_g}\frac{d\varphi_T}{dk}\bigg|_{k_0}$$

Le **temps de traversée physique** (temps de groupe de Hartman) est :
$$\tau_{t,\rm th} = \tau_0 + \tau_g = \frac{a}{v_g} + \frac{1}{v_g}\frac{d\varphi_T}{dk}\bigg|_{k_0}$$

Ce temps est calculé numériquement (différentiation de $\varphi_T$).

**Résultats pour $k_0=5$, $V_0=15$, $a=1$ :**
- $\tau_g = -0.032$ (décalage négatif : avance)
- $\tau_{t,\rm th} = \tau_0 + \tau_g = 0.200 - 0.032 = 0.168$

Dans la limite $\kappa a \to \infty$ (tanh$(\kappa a) \to 1$) :
$$\varphi_T(k)\Big|_{\rm opaque} = -ka - \arctan\!\left[\frac{\kappa^2 - k^2}{2k\kappa}\right] + O(e^{-2\kappa a})$$

La dépendance en $a$ se retrouve dans le seul terme $-ka$. Donc :
$$\frac{d\varphi_T}{dk}\Big|_{\rm opaque} = -a - \frac{d}{dk}\arctan\!\left[\frac{\kappa^2 - k^2}{2k\kappa}\right] + O(e^{-2\kappa a})$$

Et le temps de traversée :
$$\tau_{t,\rm th} = \frac{1}{v_g}\left(-a - \frac{d}{dk}\arctan\!\left[\frac{\kappa^2-k^2}{2k\kappa}\right]\right) + \frac{a}{v_g} = -\frac{1}{v_g}\frac{d}{dk}\arctan\!\left[\frac{\kappa^2 - k^2}{2k\kappa}\right]$$

Ce résultat est **indépendant de $a$** ! C'est l'**effet Hartman** : pour une barrière suffisamment opaque, le temps de traversée tunnel ne dépend plus de l'épaisseur de la barrière.

**Valeur numérique de saturation :** $\tau_{t,\rm th}(a \to \infty) \approx 0.179$ pour $k_0 = 5$, $V_0 = 15$.

### 4.3.g – Influence de $a$ sur $\tau_{t,\rm th}$

| $a$ | $\tau_0 = a/v_g$ | $\tau_{t,\rm th}$ |
|-----|-----------|------------|
| 0.5 | 0.100     | 0.125      |
| 1.0 | 0.200     | 0.168      |
| 1.5 | 0.300     | 0.177      |
| 2.0 | 0.400     | 0.179      |
| 2.5 | 0.500     | 0.179      |
| 3.0 | 0.600     | 0.179      |

$\tau_{t,\rm th}$ converge rapidement vers sa valeur asymptotique dès $\kappa a \approx 3$. Pendant ce temps, $\tau_0$ continue de croître linéairement. La vitesse de traversée apparente $v_{\rm app} = a/\tau_{t,\rm th}$ augmente sans limite avec $a$.

**Remarque :** Ce résultat ne viole pas la causalité. Le signal (l'information) ne se propage pas plus vite que la lumière. L'avancement du pic de la partie transmise correspond à un filtrage du paquet d'ondes, non à un transport supraluminique d'énergie ou d'information. La partie transmise est exponentiellement petite et résulte de la queue du paquet incident qui précède le pic principal.
