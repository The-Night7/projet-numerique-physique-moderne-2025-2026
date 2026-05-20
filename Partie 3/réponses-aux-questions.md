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

2. Définir une fonction d’onde (tableau 2d) contenant `nx` lignes et `nt` colonnes. La première ligne doit contenir un paquet d’ondes gaussien à instant donné et le reste du tableau doit contenir des zéros (ou mieux, des nombres aléatoires `empty`).

3. Définir (`numpy.linspace`) des tableaux 1d pour les intervalles d’espace `x` et de temps `t`.

4. Écrire un algorithme combinant les dérivées première par rapport au temps et seconde par rapport à l’espace pour décrire l’évolution de la fonction d’ondes initiale (paquet d’ondes dans notre cas) selon l’équation de Schrödinger.

5. Confronter les résultats de l’algorithme, dans le cas `V0 = 0`, avec le programme `PaquetOndes.py`. La comparaison peut, dans un premier temps, se faire sans représenter les paquets d’ondes.
