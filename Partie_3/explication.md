Le code Python de cette partie a pour but de résoudre numériquement l’équation de Schrödinger à une dimension pour un paquet d’ondes gaussien libre, puis de comparer la solution obtenue avec la solution théorique connue. Il reprend aussi les outils de dérivation numérique demandés au début de l’exercice.

Voici le rôle détaillé des principales fonctions et variables du script :

### Constantes physiques simplifiées
Le programme travaille avec des unités adimensionnées afin d’éviter les difficultés numériques liées aux très petites constantes physiques.

**hbar** : la constante de Planck réduite, fixée ici à `1.0`.<br>
**m** : la masse de la particule, fixée ici à `1.0`.<br>

### Partie 3.1 : dérivées numériques
Cette première partie construit les outils permettant d’approximer les dérivées d’une fonction discrétisée sur une grille.

#### La fonction `derivee_premiere(y, dx)`
Cette fonction calcule une approximation numérique de la dérivée première d’un tableau 1D `y`.

**y** : le tableau contenant les valeurs de la fonction à dériver.<br>
**dx** : le pas spatial entre deux points successifs du tableau.<br>
**dy** : le tableau résultat, contenant l’approximation de la dérivée première.<br>

Au milieu du tableau, le code utilise une différence centrée :
$$
f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2dx}
$$
Ce schéma est plus précis qu’une simple différence vers l’avant. Aux bords, le programme emploie des formules décalées pour éviter de sortir du tableau.

#### Les fonctions tests `carre(x)` et `double(x)`
Ces deux fonctions servent à vérifier que les dérivées numériques fonctionnent correctement.

**carre(x)** : renvoie $x^2$.<br>
**double(x)** : renvoie $2x$.<br>

Comme la dérivée exacte de $x^2$ est $2x$, on peut comparer le calcul numérique à la formule théorique.

#### La fonction `derivee_seconde(y, dx)`
Cette fonction calcule une approximation numérique de la dérivée seconde d’un tableau 1D.

**d2y** : le tableau contenant l’approximation de la dérivée seconde.<br>

À l’intérieur du tableau, le schéma utilisé est la différence centrée classique :
$$
f''(x_i) \approx \frac{f(x_{i-1}) - 2f(x_i) + f(x_{i+1})}{dx^2}
$$
Là encore, des formules décalées sont utilisées aux extrémités pour traiter les bords.

### Reprise du paquet d’ondes gaussien
La fonction `GaussWP(k0, a, x, t)` redéfinit localement le paquet d’ondes gaussien déjà étudié dans la partie précédente.

**k0** : le nombre d’onde moyen du paquet. Il fixe l’impulsion moyenne de la particule.<br>
**a** : un paramètre qui contrôle la largeur initiale du paquet d’ondes.<br>
**x** : la ou les positions où l’on évalue la fonction d’onde.<br>
**t** : l’instant considéré.<br>
**alpha** : une quantité complexe qui décrit l’étalement du paquet avec le temps.<br>
**norm** : le facteur de normalisation, qui maintient la probabilité totale proche de `1`.<br>
**vg** : la vitesse de groupe, c’est-à-dire la vitesse de déplacement du centre du paquet.<br>
**phase** : la partie oscillante complexe de l’onde.<br>
**envelope** : l’enveloppe gaussienne qui localise le paquet dans l’espace.<br>

La fonction renvoie finalement la fonction d’onde complexe $\Psi(x,t)$.

### Résolution du système linéaire : `resoudre_tridiagonal(a, b, c, d)`
Pour faire évoluer la fonction d’onde dans le temps, le code doit résoudre à chaque étape un système linéaire tridiagonal. Cette fonction applique la méthode de Thomas, qui est une version simplifiée de l’élimination de Gauss adaptée à ce cas particulier.

**a** : la sous-diagonale du système.<br>
**b** : la diagonale principale.<br>
**c** : la sur-diagonale.<br>
**d** : le second membre.<br>
**ac, bc, cc, dc** : des copies complexes des tableaux d’entrée pour effectuer les calculs sans modifier les données initiales.<br>
**x** : la solution du système linéaire.<br>

Cette étape est importante car le schéma de Crank-Nicolson ne donne pas directement `psi[j+1]` : il faut résoudre un petit système matriciel à chaque pas de temps.

### Partie 3.2 : évolution temporelle selon l’équation de Schrödinger
La fonction `evolution_schrodinger(nx, nt, xmin, xmax, tmin, tmax, k0, a, V0)` constitue le cœur du programme. Elle calcule la fonction d’onde sur une grille d’espace et de temps.

#### Paramètres de grille
**nx** : nombre de points spatiaux.<br>
**nt** : nombre de points temporels.<br>
**xmin, xmax** : bornes de l’intervalle spatial.<br>
**tmin, tmax** : bornes de l’intervalle temporel.<br>

Le code construit ensuite :

**x** : le tableau des positions, obtenu avec `numpy.linspace`.<br>
**t** : le tableau des instants.<br>
**dx** : le pas spatial.<br>
**dt** : le pas temporel.<br>

#### Tableau de la fonction d’onde
**psi** : un tableau 2D complexe de taille `(nt, nx)`.<br>

La convention choisie est :
$$
\psi[j, i] = \psi(t_j, x_i)
$$
Autrement dit, chaque ligne correspond à un instant, et chaque colonne à une position.

Au départ :

**psi[0, :]** : contient le paquet d’ondes gaussien initial.<br>

Toutes les autres lignes seront remplies progressivement par l’algorithme.

#### Paramètres du schéma de Crank-Nicolson
Le programme n’utilise pas un schéma d’Euler explicite, car celui-ci diverge rapidement pour l’équation de Schrödinger. Il choisit à la place le schéma de Crank-Nicolson, plus stable et bien mieux adapté à la conservation de la norme.

**n_interieur** : nombre de points spatiaux intérieurs, en excluant les deux bords.<br>
**r** : coefficient complexe lié au terme de dérivée seconde spatiale.<br>
**s** : coefficient complexe lié au potentiel constant `V0`.<br>

Les tableaux :

**a_mat** : sous-diagonale de la matrice du système.<br>
**b_mat** : diagonale principale.<br>
**c_mat** : sur-diagonale.<br>

représentent le membre de gauche du schéma de Crank-Nicolson.

#### Boucle temporelle
Pour chaque instant `j`, le programme :

1. extrait les valeurs intérieures de la fonction d’onde avec `psi_interieur` ;<br>
2. construit `second_membre`, c’est-à-dire le membre de droite du système linéaire ;<br>
3. résout le système tridiagonal pour obtenir `psi[j + 1, 1:-1]` ;<br>
4. impose les conditions aux bords `psi = 0` aux extrémités de la boîte numérique.<br>

Cette procédure fait avancer numériquement la solution dans le temps.

La fonction renvoie finalement :

**x** : la grille spatiale.<br>
**t** : la grille temporelle.<br>
**psi** : la fonction d’onde calculée à tous les instants.<br>
**dx** : le pas spatial, utile pour le calcul de la norme.<br>

### La fonction `norme(psi_x, dx)`
Cette fonction approxime l’intégrale :
$$
\int |\psi(x)|^2 dx
$$
par une somme discrète. En mécanique quantique, cette quantité représente la probabilité totale de présence de la particule. Si le calcul numérique est cohérent, cette norme doit rester proche de `1`.

**psi_x** : la fonction d’onde à un instant donné.<br>
**dx** : le pas spatial.<br>

### La fonction `main()`
Cette dernière partie fixe les paramètres du problème et lance effectivement les calculs.

#### Paramètres numériques
**nx = 1200** : nombre de points d’espace.<br>
**nt = 800** : nombre de points de temps.<br>
**xmin, xmax = -20.0, 20.0** : domaine spatial.<br>
**tmin, tmax = 0.0, 1.0** : intervalle de temps étudié.<br>

#### Paramètres physiques
**k0 = 5.0** : nombre d’onde moyen du paquet initial.<br>
**a = 0.5** : largeur initiale du paquet.<br>
**V0 = 0.0** : potentiel constant. Ici on traite donc le cas d’une particule libre.<br>

Le programme appelle ensuite `evolution_schrodinger(...)` pour produire la solution numérique.

#### Comparaison avec la théorie
Le script calcule aussi :

**psi_th_0** : la solution théorique au temps initial.<br>
**psi_th_f** : la solution théorique au temps final.<br>
**erreur_initiale** : l’écart maximal entre solution numérique et théorique à `t = 0`.<br>
**erreur_finale** : l’écart maximal au temps final.<br>

Ces quantités permettent de vérifier que l’algorithme reproduit correctement la propagation du paquet d’ondes libre.

#### Vérifications affichées dans le terminal
Le programme affiche ensuite :

- l’erreur sur la dérivée première de $x^2$ ;<br>
- l’erreur sur la dérivée seconde de $x^2$ ;<br>
- la norme initiale et finale du paquet d’ondes ;<br>
- les écarts entre solution numérique et solution théorique.<br>

Ces résultats servent à valider à la fois l’algorithme de dérivation et l’algorithme d’évolution temporelle.

### Les graphiques produits
Le script termine en traçant deux graphes :

**Premier graphe** : la partie réelle de la fonction d’onde numérique à `t=0`, comparée à la solution théorique initiale.<br>
**Second graphe** : la densité de probabilité $|\psi|^2$ au temps final, comparée à la densité théorique attendue.<br>

Si les deux courbes se superposent bien, cela montre que la méthode numérique reproduit correctement le comportement attendu du paquet d’ondes.
