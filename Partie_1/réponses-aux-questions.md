# Ondes Planes
## Généralités 
### 1. Notions physiques
#### a. Rappeler l’expression d’une onde plane à trois dimensions l’espace ainsi que la signification, la dimension physique et l’unité de $\vec{k}$ et $\omega$.
Réponse : $\Psi(\vec{r},t)=\Psi_0 \exp(i(\vec{k} \cdot \vec{r} - \omega t))$
$\vec{k}$ : direction de la propagation d'onde. Sa dimension physique est $L⁻¹$ et son unité s'exprime en $m⁻¹$.
$\omega$ : Elle caractérise la période temporelle de l'onde. Sa dimension physique est $T⁻¹$ et son unité s'exprime en $s⁻¹$.
#### b. En déduire son expression à une dimension d’espace et déterminer sa partie réelle et sa partie imaginaire. Nous travaillerons désormais à une dimension d’espace uniquement.
Réponse : Sur un seul axe, le produit scalaire $k \cdot r$ devient simplement $kx$. <br>
L'expression se simplifie en : $\Psi(x,t)=\Psi_0 \exp(i(kx - \omega t))$ <br>
En utilisant la formule d'Euler ($e^{i\theta} = cos(\theta) + i\sin(\theta)$), on détermine : <br>
∙ Partie réelle : $\Psi_0\cos(kx - \omega t)$ <br>
∙ Partie imaginaire : $\Psi_0\sin(kx - \omega t)$ <br>
#### c. On suppose que la fonction d’onde d’une particule est une onde plane. Quelle est la dimension et l’unité du terme « d’amplitude » devant l’exponentielle.
Réponse  : Dans un espace à une dimension, l'interprétation probabiliste de Max Born impose que $|\Psi|²$ représente une densité de probabilité par unité de longueur ($|\Psi|²dx$ est une probabilité sans dimension). La fonction d'onde $\Psi$ a donc pour dimension physique $L^{-1/2}$. L'exponentielle étant un terme sans dimension, l'amplitude $\Psi_0$ a exactement la même dimension que la fonction d'onde, soit $L^{-1/2}$. Son unité dans le Système International est donc le $m^{-1/2}$

#### d. Montrer que cette fonction d’onde est solution de l’équation de Schrödinger, si la particule est libre.
Réponse : Pour une particule libre, le potentiel est nul ($V(x)=0$). L'équation de Schrödinger dépendante du temps s'écrit alors : $i\hbar\frac{\partial\Psi}{\partial t}(x,t)=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}(x,t)$. En considérant l'onde plane complexe $\Psi(x,t)=\Psi_0 e^{i(kx-\omega t)}$ : <br>
∙ La dérivée temporelle est : $\frac{\partial\Psi}{\partial t}=-i\omega\Psi$. <br>
∙ La dérivée spatiale seconde est : $\frac{\partial^2\Psi}{\partial x^2}=(ik)^2\Psi=-k^2\Psi$. <br>
En réinjectant ces expressions dans l'équation de Schrödinger, on obtient : $i\hbar(-i\omega\Psi)=-\frac{\hbar^2}{2m}(-k^2\Psi)$, ce qui donne $\hbar\omega\Psi=\frac{\hbar^2 k^2}{2m}\Psi$. Sachant que l'énergie est $E=\hbar\omega$ et que l'impulsion est $p=\hbar k$, cette égalité se simplifie en $E=\frac{p^2}{2m}$, ce qui correspond parfaitement à l'énergie cinétique d'une particule libre. L'onde plane est donc bien une solution mathématique de l'équation.

#### e. Déterminer la relation de dispersion, la vitesse de phase et la vitesse de groupe. 
Réponse : <br>
∙ **Relation de dispersion** : D'après la démonstration ci-dessus, la relation liant la pulsation angulaire $\omega$ au nombre d'onde $k$ est $\omega=\frac{\hbar k^2}{2m}$. <br>
∙ **Vitesse de phase** : La vitesse de propagation de l'onde (ou vitesse de phase) est définie par $v_\phi=\frac{\omega}{k}$. En appliquant la relation de dispersion, on obtient $v_\phi=\frac{\hbar k}{2m}$ (ce qui équivaut à $\frac{p}{2m}$). <br>
∙ **Vitesse de groupe** : La vitesse de groupe correspond à la vitesse de l'enveloppe de l'onde et se calcule par $v_g=\frac{d\omega}{dk}$. En dérivant la relation de dispersion, on obtient $v_g=\frac{\hbar k}{m}$ (ce qui équivaut à $\frac{p}{m}$).

#### f. Comment comparer ces vitesses à la vitesseobtenue en prenant : $v = p/m$ 
Réponse : On constate que la vitesse de groupe ($v_g=\frac{p}{m}$) correspond exactement à la vitesse classique d'une particule $v=\frac{p}{m}$. À l'inverse, la vitesse de phase n'est égale qu'à la moitié de la vitesse classique ($v_\phi=\frac{v}{2}$). C'est pour cela que la vitesse de groupe est la grandeur pertinente pour décrire le déplacement macroscopique de la particule matérielle.

#### g. Écrire la condition de normalisation de cette fonction d’onde en précisant les bornes. Quelles seraient les bornes pour une particule dans un puits de profondeur infinie ? 
Réponse : Pour une particule libre évoluant dans tout l'espace, la probabilité totale de la trouver quelque part doit valoir 1. La condition de normalisation s'écrit avec des bornes infinies : $\int_{-\infty}^{+\infty}|\Psi(x,t)|^2\,dx=1$. <br>
Si la particule est confinée dans un puits de potentiel de profondeur infinie de largeur $L$ (de $x=0$ à $x=L$), la particule a une probabilité de présence strictement nulle à l'extérieur. L'intégrale de normalisation se restreint alors aux bornes du puits : $\int_{0}^{L}|\Psi(x,t)|^2\,dx=1$. <br>
*(Pour un puits centré en 0 de largeur $a$, les bornes seraient de $-a/2$ à $a/2$).*

#### h. Montrer que ces fonctions d’onde (pour une particule libre) ne sont pas des solutions physiquement acceptables. 
Réponse : Si l'on cherche à normaliser l'onde plane libre $\Psi(x,t)=\Psi_0 e^{i(kx-\omega t)}$, le calcul donne : $\int_{-\infty}^{+\infty}|\Psi_0 e^{i(kx-\omega t)}|^2\,dx=\int_{-\infty}^{+\infty}|\Psi_0|^2\,dx$. <br>
Comme $|\Psi_0|^2$ est une constante, cette intégrale diverge vers l'infini et ne converge jamais vers 1. Ainsi, bien que l'onde plane soit une solution mathématique valide de l'équation de Schrödinger, elle n'est pas normalisable et ne peut donc pas représenter l'état physique réel et acceptable d'une particule isolée. *(Dans la réalité, on utilise des paquets d'ondes, c'est-à-dire une superposition d'ondes planes, pour obtenir des solutions localisées et normalisables).*

### 2. Un peu de Python
Réponse : Le programme `OndePlane1d2A.py` a été créé pour tracer le graphique décrit ci-dessus. Voir le fichier Python associé.

---

## Superposition d'ondes planes
### 1. Notions physiques

#### a. Justifier qu'une superposition d'ondes planes reste solution de l'équation de Schrödinger.
Réponse : L'équation de Schrödinger est une équation **linéaire** en $\Psi$. Cela signifie que si $\Psi_1$ et $\Psi_2$ sont deux solutions, alors toute combinaison linéaire $\alpha\Psi_1 + \beta\Psi_2$ (avec $\alpha, \beta \in \mathbb{C}$) est également solution : c'est le **principe de superposition**. <br>
En effet, en notant $\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$ l'opérateur hamiltonien (pour une particule libre), l'équation de Schrödinger s'écrit $i\hbar\frac{\partial\Psi}{\partial t} = \hat{H}\Psi$. Par linéarité de la dérivée et de $\hat{H}$ :

$$i\hbar\frac{\partial}{\partial t}(\alpha\Psi_1+\beta\Psi_2) = \alpha\,i\hbar\frac{\partial\Psi_1}{\partial t}+\beta\,i\hbar\frac{\partial\Psi_2}{\partial t} = \alpha\hat{H}\Psi_1+\beta\hat{H}\Psi_2 = \hat{H}(\alpha\Psi_1+\beta\Psi_2)$$

Une superposition (finie ou infinie) d'ondes planes est donc toujours solution de l'équation de Schrödinger.

#### b. On considère à présent trois ondes planes au même instant $t=0$, de nombres d'onde $k_0$, $k_0-\Delta k/2$ et $k_0+\Delta k/2$. La deuxième et la troisième ont une amplitude deux fois plus petite que la première. Déterminer l'expression de l'onde résultant de la somme de ces trois ondes planes.
Réponse : À $t=0$, les trois ondes planes s'écrivent :

$$\Psi_1(x,0) = A\,e^{ik_0 x}, \quad \Psi_2(x,0) = \frac{A}{2}\,e^{i(k_0-\Delta k/2)x}, \quad \Psi_3(x,0) = \frac{A}{2}\,e^{i(k_0+\Delta k/2)x}$$

Leur somme vaut :
$\Psi(x,0) = A\,e^{ik_0 x} + \frac{A}{2}\,e^{i(k_0-\Delta k/2)x} + \frac{A}{2}\,e^{i(k_0+\Delta k/2)x}$

On factorise par $A\,e^{ik_0 x}$ :
$\Psi(x,0) = A\,e^{ik_0 x}\left[1 + \frac{1}{2}e^{-i\Delta k\,x/2} + \frac{1}{2}e^{+i\Delta k\,x/2}\right]$

En utilisant la formule d'Euler ($e^{i\theta}+e^{-i\theta}=2\cos\theta$), le crochet se simplifie :

$$\Psi(x,0) = A\,e^{ik_0 x}\left[1 + \cos\!\left(\frac{\Delta k\,x}{2}\right)\right]$$

#### c. En déduire la densité de probabilité de présence au même instant.
Réponse : La densité de probabilité de présence est $\rho(x) = |\Psi(x,0)|^2$. Comme $|e^{ik_0 x}|^2 = 1$, on obtient directement :

$$\boxed{\rho(x) = |\Psi(x,0)|^2 = A^2\left[1+\cos\!\left(\frac{\Delta k\,x}{2}\right)\right]^2}$$

Cette expression est réelle et positive, comme attendu pour une densité de probabilité. Elle présente des **modulations périodiques** de période spatiale $\frac{4\pi}{\Delta k}$ : la particule est plus probablement trouvée là où les ondes interfèrent de manière constructive.

#### d. Représenter graphiquement les parties réelles de ces trois ondes et la partie réelle de leur somme sur l'intervalle $[-\pi/\Delta k,\, \pi/\Delta k]$. Sur le même graphique, représenter l'enveloppe.
Réponse : Les parties réelles des trois ondes composantes sont :

$$\Re(\Psi_1) = A\cos(k_0 x), \quad \Re(\Psi_2) = \frac{A}{2}\cos\!\left(\!\left(k_0-\frac{\Delta k}{2}\right)x\right), \quad \Re(\Psi_3) = \frac{A}{2}\cos\!\left(\!\left(k_0+\frac{\Delta k}{2}\right)x\right)$$

La partie réelle de la somme est :
$\Re(\Psi) = A\cos(k_0 x)\left[1+\cos\!\left(\frac{\Delta k\,x}{2}\right)\right]$

L'**enveloppe** correspond au facteur modulant (toujours positif sur l'intervalle considéré) :

$$\mathcal{E}(x) = A\left[1+\cos\!\left(\frac{\Delta k\,x}{2}\right)\right]$$

Sur l'intervalle $[-\pi/\Delta k,\, \pi/\Delta k]$, l'enveloppe est maximale en $x=0$ (valeur $2A$) et s'annule aux bords (valeur $0$), ce qui illustre bien la localisation spatiale apportée par la superposition. Le tracé Python ci-dessous (section 2) permet de visualiser ces courbes.

### 2. Un peu de Python
Réponse : Le programme `OndePlane1d2A.py` a été étendu pour tracer les graphiques décrits ci-dessus. Voir le fichier Python associé.