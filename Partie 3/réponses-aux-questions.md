# 3 Résolution numérique de l’équation de Schrödinger

L’objectif de cette dernière étape va être d’élaborer un premier algorithme de résolution de l’équation de Schrödinger qui permettra de déterminer l’évolution du paquet d’ondes initial. Pour une particule libre et un paquet d’ondes gaussien à l’instant initial, l’évolution du paquet d’ondes est connue (partie 2). Si l’algorithme élaboré est correct, il donnera les mêmes résultats que la théorie.

C’est dans un dernier temps que nous étudierons l’évolution d’un paquet d’ondes qui rencontre une barrière de potentiel. Le traitement rigoureux du problème est relativement complexe et la résolution numérique constituera la voie privilégiée dans ce projet.

## 3.1 Algorithme de dérivation

La fonction d’onde à un instant donné peut être vue comme un tableau 1d (`numpy.array` en Python avec la librairie `numpy`) contenant autant d’éléments que le nombre de points `npts` utilisés pour l’intervalle d’espace (`x` dans les codes précédents).

1. Dérivée première

   a. Rappeler la définition de la dérivée d’une fonction réelle en un point.

   b. Si cette fonction est un tableau 1d de `npts` éléments, écrire un algorithme (pseudo-code ou Python) calculant cette dérivée.

   c. Écrire en Python une fonction renvoyant le carré `x²` d’un nombre `x` et une autre renvoyant `2x`.

   d. À l’aide de votre algorithme, calculer numériquement la dérivée de la fonction `x²` et comparer les valeurs obtenues avec celles renvoyées par la fonction `2x`. Vous pouvez, par exemple, regarder l’erreur relative commise par votre algorithme.

2. Reprendre les questions précédentes, mais pour la dérivée seconde.

## 3.2 Algorithme pour l’équation de Schrödinger

L’équation de Schrödinger décrit l’évolution de la fonction d’onde dans le temps et l’espace. Dès lors, la fonction d’onde ne peut pas être stockée dans un tableau 1d, mais un tableau 4d. Dans la mesure où nous n’étudions que des problèmes à une dimension d’espace, des tableaux 2d seront suffisants.

1. Rappeler l’équation de Schrödinger à une dimension d’espace pour une particule dans un potentiel constant `V0`.

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

2. Définir une fonction d’onde (tableau 2d) contenant `nx` lignes et `nt` colonnes. La première ligne doit contenir un paquet d’ondes gaussien à instant donné et le reste du tableau doit contenir des zéros (ou mieux, des nombres aléatoires `empty`).

   En pratique, il est plus cohérent de stocker la fonction d’onde sous la forme `psi[j, i] = psi(t_j, x_i)`, donc dans un tableau de taille `(nt, nx)` :

   - chaque **ligne** correspond à un instant ;
   - chaque **colonne** correspond à une position.

   Ainsi, la première ligne `psi[0, :]` contient naturellement l’état initial à `t = 0`.

   ```python
   import numpy as np

   psi = np.zeros((nt, nx), dtype=complex)
   psi[0, :] = GaussWP(k0, a, x, 0)
   ```

   Si l’on veut suivre strictement l’idée de l’énoncé, on peut dire que la première ligne contient le paquet d’ondes gaussien initial et que toutes les autres cases sont initialisées à zéro en attendant le calcul de l’évolution temporelle.

3. Définir (`numpy.linspace`) des tableaux 1d pour les intervalles d’espace `x` et de temps `t`.

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

4. Écrire un algorithme combinant les dérivées première par rapport au temps et seconde par rapport à l’espace pour décrire l’évolution de la fonction d’ondes initiale (paquet d’ondes dans notre cas) selon l’équation de Schrödinger.



5. Confronter les résultats de l’algorithme, dans le cas `V0 = 0`, avec le programme `PaquetOndes.py`. La comparaison peut, dans un premier temps, se faire sans représenter les paquets d’ondes.
