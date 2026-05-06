# Ondes Planes
## Généralités 
### 1. Notions physiques
#### a. Rappeler l’expression d’une onde plane à trois dimensions l’espace ainsi que la signification, la dimension physique et l’unité de $\vec{k}$ et $\omega$.
Réponse : $\Psi(r,t)=\Psi_0 \exp(\vec{k} \bullet r - \omega t)$
$\vec{k}$ : direction de la propagation d'onde. Sa dimension physique est $L⁻¹$ et son unité s'exprime en $m⁻¹$.
$\omega$ : Elle caractérise la période temporelle de l'onde. Sa dimension physique est $T⁻¹$ et son unité s'exprime en $s⁻¹$.
#### b. En déduire son expression à une dimension d’espace et déterminer sa partie réelle et sa partie imaginaire. Nous travaillerons désormais à une dimension d’espace uniquement.
Réponse : Sur un seul axe, le produit scalaire $k \bullet r$ devient simplement $kx$. <br>
L'expression se simplifie en : $\Psi(x,t)=\Psi_0 \exp(kx - \omega t)$ <br>
En utilisant la formule d'Euler ($e^{i\theta} = cos(\theta) + i\sin(\theta)$), on détermine : <br>
∙ Partie réelle : $\Psi_0cos(\omega t)$ <br>
∙ Partie imaginaire : $\Psi_0sin(\omega t)$ <br>
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
