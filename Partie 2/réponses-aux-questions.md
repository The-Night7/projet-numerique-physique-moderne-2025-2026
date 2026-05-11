# Paquets d’ondes
## Généralités
L’équation de Schrödinger étant linéaire, si deux fonctions d’ondes sont solutions (pour un même potentiel), leur somme reste solution et constitue un état possible (superposition d’état qui amène à l’expérience du chat de Schrödinger). À trois dimensions d’espace, l’expression la plus générale d’une telle superposition est un paquet d’ondes d’expression :

$$\Psi(\vec{r}, t) = [2\pi]^{-\frac{3}{2}} \iiint g(vec{k})e^{i\vec{r}\bullet\vec{k}-i\omega t}d³\vec{k}$$

où $\vec{k}$ est le vecteur d'onde et \vec{r} le vecteur position (ou rayon vecteur). <br>

Analysons cette expression : <br>
* le pré-facteur $[2\pi]^{-\frac{3}{2}}$ est ajouté de manière à ce que $\psi$ soit normalisable
* la fonction $vec{g}$ est une fonction de trois variables, à savoir les trois composantes $vec{k}$
* le terme en exponentiel correspond à l'onde plane
* l'expression générale fait intervenir une intégrale triple sur les trois coordonnées du vecteur $vec{k}$

Dans une base cartésienne $(\vec{e}_x, \vec{e}_y, \vec{e}_z)$, où $\vec{r} = x\vec{e}_x + y\vec{e}_y + z\vec{e}_z$ et $\vec{k} = k_x\vec{e}_x + k_y\vec{e}_y + k_z\vec{e}_z$ ce paquet d'ondes peut s'écrire

$$\Psi(x, y, z, t) = [2\pi]^{-3/2} \iiint g(k_x, k_y, k_z) \exp \left[ \mathrm{i}\vec{r} \cdot \vec{k} - \mathrm{i}\omega t \right] \mathrm{d}k_x \mathrm{d}k_y \mathrm{d}k_z$$

avec $\vec{r} \cdot \vec{k} = xk_x + yk_y + zk_z$.
**Remarque sur les notations**
Bien souvent, en physique vous verrez l'expression condensée

$$\Psi(\vec{r}, t) = [2\pi]^{-3/2} \int g(\vec{k}) \exp \left[ \mathrm{i}\vec{r} \cdot \vec{k} - \mathrm{i}\omega t \right] \mathrm{d}^3k \tag{2}$$

ou encore si on note $\mathbf{k} = \vec{k}$ :

$$\Psi(\mathbf{r}, t) = [2\pi]^{-3/2} \int g(\mathbf{k}) \exp \left[ \mathrm{i}\mathbf{r} \cdot \mathbf{k} - \mathrm{i}\omega t \right] \mathrm{d}\mathbf{k}. \tag{3}$$

### 2.2 Paquets d'ondes gaussien

Un cas particulier de paquet d'ondes est celui pour lequel la fonction $g$ est une gaussienne (loi normale). Ce cas particulier est assez important notamment parce que les calculs sont plus simples et parce que ce type de paquet d'ondes est réalisable en laboratoire.
En dimension une

$$g(k) = \sqrt{a}[2\pi]^{-1/4} \exp \left[ -a^2(k - k_0)^2/4 \right] , \tag{4}$$

où $a$ est une grandeur qui sera interprétée par la suite.

**1. Notions physiques**
a. Donner l'expression générale d'un paquet d'ondes pour une particule libre se déplaçant selon l'axe $(Ox)$ de manière à ce que $\omega$ n'intervienne pas. <br>



b. Donner l'expression générale d'un paquet d'ondes gaussien. <br>
c. En calculant l'intégrale, déterminer l'expression du paquet d'ondes gaussien à l'instant $t$. <br>
d. Vérifier que ce paquet d'ondes est normalisé. <br>
e. En utilisant les « Outils mathématiques » relatifs à la transformation de FOURIER ou avec les notions vus en Ondes, exprimer $g(k)$ en fonction de $\Psi(x, t = 0)$. <br>

**2. Un peu de python**
Nommez ce programme : `PaquetOndeGauss1dXY.py` avec `X` votre groupe de TD et `Y` la lettre de votre groupe de projet. <br>
a. Définir des constantes `hbar` et `m` (pour la masse de l'électron par exemple). <br>
b. Définir une fonction `GaussWP` (pour « *Gaussian Wave Packet* ») prenant en argument les quatre paramètres `k0`, `a`, `x`, `t` et renvoyant le paquet d'ondes gaussien $\Psi(x,t)$. <br>
c. Tester cette fonction puis représenter les parties réelle et imaginaire du paquet d'ondes gaussien $\Psi(x,t)$ en fonction de $x$, à l'instant $t = 0$. <br>
d. Quelle difficulté rencontrez-vous ? <br>
e. Proposer une solution/astuce. <br>