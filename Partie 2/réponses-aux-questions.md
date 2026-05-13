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

$$\Psi(\vec{r}, t) = [2\pi]^{-3/2} \int g(\vec{k}) \exp \left[ \mathrm{i}\vec{r} \cdot \vec{k} - \mathrm{i}\omega t \right] \mathrm{d}^3k$$

ou encore si on note $\mathbf{k} = \vec{k}$ :

$$\Psi(\mathbf{r}, t) = [2\pi]^{-3/2} \int g(\mathbf{k}) \exp \left[ \mathrm{i}\mathbf{r} \cdot \mathbf{k} - \mathrm{i}\omega t \right] \mathrm{d}\mathbf{k}.$$

### 2.2 Paquets d'ondes gaussien

Un cas particulier de paquet d'ondes est celui pour lequel la fonction $g$ est une gaussienne (loi normale). Ce cas particulier est assez important notamment parce que les calculs sont plus simples et parce que ce type de paquet d'ondes est réalisable en laboratoire.
En dimension une

$$g(k) = \sqrt{a}[2\pi]^{-1/4} \exp \left[ -a^2(k - k_0)^2/4 \right]$$

où $a$ est une grandeur qui sera interprétée par la suite.

**1. Notions physiques**
a. Donner l'expression générale d'un paquet d'ondes pour une particule libre se déplaçant selon l'axe $(Ox)$ de manière à ce que $\omega$ n'intervienne pas. <br>

L'expression générale d'un paquet d'ondes à une dimension s'écrit comme une superposition d'ondes planes : $\Psi(x,t) = \frac{1}{\sqrt{2\pi}} \int g(k) e^{i(kx - \omega t)} dk$. 
Pour une particule libre, l'énergie est purement cinétique : $E = \frac{p^2}{2m}$. En utilisant les relations de de Broglie et Planck-Einstein ($p = \hbar k$ et $E = \hbar\omega$), on obtient la relation de dispersion $\omega = \frac{\hbar k^2}{2m}$. 
En remplaçant $\omega$, l'expression générale devient :
**$\Psi(x,t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} g(k) e^{i\left(kx - \frac{\hbar k^2}{2m}t\right)} dk$**

b. Donner l'expression générale d'un paquet d'ondes gaussien. <br>

Un paquet d'ondes est gaussien si la fonction de distribution des nombres d'onde $g(k)$ est une fonction gaussienne. Son expression mathématique standard, centrée autour d'un nombre d'onde moyen $k_0$ avec une largeur liée à un paramètre $a$, est :
**$g(k) = \left(\frac{2a}{\pi}\right)^{1/4} e^{-a(k-k_0)^2}$**

c. En calculant l'intégrale, déterminer l'expression du paquet d'ondes gaussien à l'instant $t$. <br>

L'insertion de $g(k)$ dans l'expression de $\Psi(x,t)$ donne une intégrale gaussienne complexe. En effectuant l'intégration (généralement via une complétion du carré dans l'exponentielle), on obtient l'expression analytique du paquet d'ondes au cours du temps :
**$\Psi(x,t) = \left(\frac{2a}{\pi}\right)^{1/4} \frac{1}{\sqrt{2\alpha(t)}} \exp\left[ -\frac{(x - v_g t)^2}{4\alpha(t)} \right] \exp\left[ i\left(k_0 x - \frac{\hbar k_0^2}{2m}t\right) \right]$**
Où :
*   $v_g = \frac{\hbar k_0}{m}$ est la vitesse de groupe (vitesse classique de la particule).
*   $\alpha(t) = a + i\frac{\hbar t}{2m}$ est un paramètre complexe traduisant l'étalement temporel du paquet d'ondes.

d. Vérifier que ce paquet d'ondes est normalisé. <br>

Pour qu'un paquet d'ondes soit normalisé, il faut que $\int_{-\infty}^{+\infty} |\Psi(x,t)|^2 dx = 1$. 
En calculant le module au carré de l'expression précédente, la phase complexe s'annule, et le terme en amplitude donne :
$|\Psi(x,t)|^2 = \sqrt{\frac{2a}{\pi |\alpha(t)|^2}} \exp\left[-\frac{2a}{4|\alpha(t)|^2} (x - v_g t)^2\right]$
L'intégration de cette densité de probabilité (qui est elle-même une gaussienne réelle dont l'écart-type augmente avec le temps) sur tout l'espace donnera bien **1**, confirmant que la probabilité totale de trouver la particule reste égale à 100 % au cours du temps, indépendamment de son étalement spatial. L'état est donc physiquement acceptable.


e. En utilisant les « Outils mathématiques » relatifs à la transformation de FOURIER ou avec les notions vus en Ondes, exprimer $g(k)$ en fonction de $\Psi(x, t = 0)$. <br>

À l'instant $t=0$, la relation $\Psi(x,0) = \frac{1}{\sqrt{2\pi}} \int g(k) e^{ikx} dk$ n'est rien d'autre que la **transformée de Fourier inverse** de $g(k)$. 
D'après les propriétés mathématiques de la transformation de Fourier, on peut inverser la relation pour trouver $g(k)$ :
**$g(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} \Psi(x, 0) e^{-ikx} dx$**


**2. Un peu de python**
Nommez ce programme : `PaquetOndeGauss1dXY.py` avec `X` votre groupe de TD et `Y` la lettre de votre groupe de projet. <br>

a. Définir des constantes `hbar` et `m` (pour la masse de l'électron par exemple). <br>

b. Définir une fonction `GaussWP` (pour « *Gaussian Wave Packet* ») prenant en argument les quatre paramètres `k0`, `a`, `x`, `t` et renvoyant le paquet d'ondes gaussien $\Psi(x,t)$. <br>

c. Tester cette fonction puis représenter les parties réelle et imaginaire du paquet d'ondes gaussien $\Psi(x,t)$ en fonction de $x$, à l'instant $t = 0$. <br>

d. Quelle difficulté rencontrez-vous ? <br>

Si nous utilisons les constantes en USI ($\hbar \approx 10^{-34}$ J.s, $m \approx 10^{-31}$ kg, $x \approx 10^{-9}$ m), **nous nous heurtons aux limites de la précision en virgule flottante (`float64`) de Python**. La machine manipule des ordres de grandeur extrêmes, ce qui entraîne des risques d'**underflow** (valeurs assimilées à 0 par l'ordinateur) ou d'erreurs d'arrondi colossales lors de la division ou de l'exponentiation (parlant d'expérience), générant un paquet d'ondes faussé ou numériquement instable.

e. Proposer une solution/astuce. <br>

Pour contourner ce problème, il faut **changer de système d'unités (adimensionner le problème)**. 
*   L'astuce principale consiste à travailler en **unités atomiques** (où on pose arbitrairement $\hbar = 1$ et $m = 1$). 
*   Alternativement, vous pouvez utiliser des unités adaptées à l'échelle quantique, comme l'électron-volt (eV) pour l'énergie, le nanomètre (nm) pour les longueurs et la femtoseconde (fs) pour le temps. Cela ramène toutes les grandeurs numériques (y compris `hbar` et `m`) autour de l'unité ($\approx 1$), garantissant un calcul Python rapide et extrêmement précis.