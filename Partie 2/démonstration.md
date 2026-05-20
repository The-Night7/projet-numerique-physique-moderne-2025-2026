# Démonstration de l’expression intégrale d’un paquet d’ondes

On veut justifier l’écriture

$$
\Psi(\vec{r}, t) = (2\pi)^{-\frac{3}{2}} \iiint g(\vec{k})\, e^{i\vec{r}\cdot\vec{k}-i\omega t}\, d^3\vec{k}.
$$

Cette formule exprime qu’une fonction d’onde peut être vue comme une **superposition continue d’ondes planes**. La démonstration repose sur deux idées :

1. à un instant donné, toute fonction d’onde suffisamment régulière peut se décomposer en composantes sinusoïdales par transformation de Fourier ;
2. chaque composante sinusoïdale évolue ensuite dans le temps comme une onde plane, ce qui ajoute le facteur $e^{-i\omega t}$.

---

## 1. Point de départ : la décomposition de Fourier en une dimension

En une dimension, une fonction assez régulière $f(x)$ peut s’écrire sous la forme

$$
f(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{+\infty} \tilde f(k)\, e^{ikx}\, dk.
$$

Ici :

- $k$ est le nombre d’onde ;
- $e^{ikx}$ est une onde plane ;
- $\tilde f(k)$ donne le poids de chaque onde plane dans la superposition.

La fonction $\tilde f(k)$ est la transformée de Fourier de $f(x)$ :

$$
\tilde f(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{+\infty} f(x)\, e^{-ikx}\, dx.
$$

Autrement dit, **une fonction localisée dans l’espace n’est pas décrite par une seule onde plane**, mais par une infinité d’ondes planes de nombres d’onde différents.

---

## 2. Généralisation à trois dimensions

En trois dimensions, la fonction d’onde dépend de la position

$$
\vec{r}=(x,y,z),
$$

et le nombre d’onde devient un vecteur

$$
\vec{k}=(k_x,k_y,k_z).
$$

Le produit scalaire vaut

$$
\vec{r}\cdot\vec{k}=xk_x+yk_y+zk_z.
$$

La généralisation naturelle de la transformation de Fourier à 3D est alors

$$
\Psi(\vec{r},0)=(2\pi)^{-\frac{3}{2}}\iiint g(\vec{k})\, e^{i\vec{r}\cdot\vec{k}}\, d^3\vec{k},
$$

avec

$$
d^3\vec{k}=dk_x\,dk_y\,dk_z.
$$

Ici, $g(\vec{k})$ joue exactement le même rôle que $\tilde f(k)$ en une dimension : c’est la **répartition des amplitudes** sur les différentes ondes planes de vecteur d’onde $\vec{k}$.

Le facteur $(2\pi)^{-3/2}$ vient du choix de convention pour la transformation de Fourier symétrique en 3D.

---

## 3. Pourquoi obtient-on une intégrale triple ?

Parce qu’en trois dimensions, il faut sommer sur toutes les valeurs possibles de :

- $k_x$ ;
- $k_y$ ;
- $k_z$.

La somme continue sur ces trois variables devient donc une intégrale triple :

$$
\iiint (\cdots)\, dk_x\,dk_y\,dk_z.
$$

On peut aussi écrire cela de manière condensée :

$$
\iiint (\cdots)\, d^3\vec{k}.
$$

Cette notation signifie simplement qu’on intègre sur tout l’espace des vecteurs d’onde.

---

## 4. Interprétation physique de l’onde plane élémentaire

Une onde plane monochromatique en mécanique quantique s’écrit

$$
\psi_{\vec{k}}(\vec{r},t)=e^{i(\vec{r}\cdot\vec{k}-\omega t)}.
$$

Cette expression contient :

- un terme spatial $e^{i\vec{r}\cdot\vec{k}}$ ;
- un terme temporel $e^{-i\omega t}$.

Chaque valeur de $\vec{k}$ correspond donc à une onde plane particulière, et l’état quantique général est obtenu en les additionnant toutes avec leurs poids respectifs $g(\vec{k})$.

---

## 5. Passage de l’instant initial à l’instant $t$

À l’instant initial $t=0$, on a

$$
\Psi(\vec{r},0)=(2\pi)^{-\frac{3}{2}}\iiint g(\vec{k})\, e^{i\vec{r}\cdot\vec{k}}\, d^3\vec{k}.
$$

Maintenant, chaque composante d’onde plane évolue dans le temps en acquérant le facteur de phase

$$
e^{-i\omega t}.
$$

On remplace donc chaque terme $e^{i\vec{r}\cdot\vec{k}}$ par

$$
e^{i\vec{r}\cdot\vec{k}-i\omega t}.
$$

On obtient alors

$$
\Psi(\vec{r}, t) = (2\pi)^{-\frac{3}{2}} \iiint g(\vec{k})\, e^{i\vec{r}\cdot\vec{k}-i\omega t}\, d^3\vec{k}.
$$

C’est exactement la formule demandée.

---

## 6. Sens physique de $g(\vec{k})$

La fonction $g(\vec{k})$ est l’amplitude de chaque composante de vecteur d’onde $\vec{k}$.

- Si $g(\vec{k})$ est très concentrée autour d’une valeur $\vec{k}_0$, le paquet d’ondes ressemble à une onde presque monochromatique.
- Si $g(\vec{k})$ est étalée, la superposition contient beaucoup de composantes différentes, ce qui permet de localiser davantage la particule dans l’espace.

Il y a donc un lien direct entre :

- l’étalement de $\Psi(\vec{r},t)$ dans l’espace ;
- l’étalement de $g(\vec{k})$ dans l’espace des vecteurs d’onde.

---

## 7. Formule réciproque

La décomposition précédente admet la relation inverse :

$$
g(\vec{k})=(2\pi)^{-\frac{3}{2}}\iiint \Psi(\vec{r},0)\, e^{-i\vec{r}\cdot\vec{k}}\, d^3\vec{r}.
$$

Elle permet de retrouver la composition du paquet d’ondes à partir de la fonction d’onde initiale.

---

## 8. Conclusion

La formule

$$
\Psi(\vec{r}, t) = (2\pi)^{-\frac{3}{2}} \iiint g(\vec{k})\, e^{i\vec{r}\cdot\vec{k}-i\omega t}\, d^3\vec{k}
$$

se démontre donc ainsi :

1. on décompose la fonction d’onde initiale en ondes planes par transformation de Fourier en 3D ;
2. chaque onde plane élémentaire évolue dans le temps avec le facteur $e^{-i\omega t}$ ;
3. la somme continue de toutes ces composantes donne l’expression intégrale du paquet d’ondes.

En résumé, cette intégrale triple n’est rien d’autre que la version tridimensionnelle de la superposition d’ondes planes, principe rendu possible par la linéarité de l’équation de Schrödinger.
