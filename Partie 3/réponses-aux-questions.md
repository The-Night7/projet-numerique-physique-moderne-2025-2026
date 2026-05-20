# 3 Résolution numérique de l’équation de Schrödinger

L’objectif de cette dernière étape est d’élaborer un premier algorithme de résolution de l’équation de Schrödinger qui permettra de déterminer l’évolution du paquet d’ondes initial [1]. Pour une particule libre et un paquet d’ondes gaussien, l’algorithme doit produire des résultats concordants avec la théorie [1].

## 3.1 Algorithme de dérivation

### 1. Dérivée première

**a. Rappeler la définition de la dérivée d’une fonction réelle en un point.**

**Réponse :** La dérivée d'une fonction réelle $f$ en un point $x$ est définie par la limite du taux d'accroissement lorsque l'intervalle $h$ tend vers 0 :
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

**b. Si cette fonction est un tableau 1d de `npts` éléments, écrire un algorithme (pseudo-code ou Python) calculant cette dérivée.**

**Réponse :** Pour un tableau NumPy `y` avec un pas constant `dx`, on utilise une approximation par différences finies [2]. Voici une implémentation vectorisée utilisant les "slices" de NumPy pour plus d'efficacité :

```python
import numpy as np

def derivee_premiere(y, dx):
    dy = np.zeros(len(y))
    dy[:-1] = (y[1:] - y[:-1]) / dx 
    dy[-1] = (y[-1] - y[-2]) / dx   
    return dy

```

**c. Écrire en Python une fonction renvoyant le carré $x²$ d’un nombre $x$ et une autre renvoyant $2x$. <br>**

**Réponse :**
```python
import numpy as np

def carre(x):
    return x**2

def double(x):
    return 2*x

```
**d. À l’aide de votre algorithme, calculer numériquement la dérivée de la fonction x² et comparer les valeurs obtenues avec celles renvoyées par la fonction 2x. Vous pouvez, par exemple, regarder l’erreur relative commise par votre algorithme. <br>**

**Réponse :** En appliquant l'algorithme à un tableau généré par np.linspace, on compare la dérivée numérique à la valeur théorique $2x$. L'erreur relative est d'ordre 1 par rapport au pas $dx$ pour un schéma progressif.Plus $dx$ est petit (nombre de points élevé), plus l'erreur diminue.

### 2. Reprendre les questions précédentes, mais pour la dérivée seconde.

**Réponse :**

Définition : La dérivée seconde $f′′(x)$ représente la dérivée de la dérivée première, mesurant la courbure de la fonction.

Algorithme : On utilise le schéma des différences finies centrées, plus précis:
```python
import numpy as np

def calculer_derivee_seconde(y, dx):
    d2y = np.zeros(len(y))
    d2y[1:-1] = (y[:-2] - 2*y[1:-1] + y[2:])
    dx**2
    return d2y
```
Comparaison : La dérivée seconde de $x²$
  est la constante 2. L'algorithme renverra une valeur quasi identique à 2 pour les points intérieurs, avec une erreur d'ordre $dx²$.

## 3.2 Algorithme pour l’équation de Schrödinger

L’équation de Schrödinger décrit l’évolution de la fonction d’onde dans le temps et l’espace. Dès lors, la fonction d’onde ne peut pas être stockée dans un tableau 1d, mais un tableau 4d. Dans la mesure où nous n’étudions que des problèmes à une dimension d’espace, des tableaux 2d seront suffisants.

1. Rappeler l’équation de Schrödinger à une dimension d’espace pour une particule dans un potentiel constant `V0`.

2. Définir une fonction d’onde (tableau 2d) contenant `nx` lignes et `nt` colonnes. La première ligne doit contenir un paquet d’ondes gaussien à instant donné et le reste du tableau doit contenir des zéros (ou mieux, des nombres aléatoires `empty`).

3. Définir (`numpy.linspace`) des tableaux 1d pour les intervalles d’espace `x` et de temps `t`.

4. Écrire un algorithme combinant les dérivées première par rapport au temps et seconde par rapport à l’espace pour décrire l’évolution de la fonction d’ondes initiale (paquet d’ondes dans notre cas) selon l’équation de Schrödinger.

5. Confronter les résultats de l’algorithme, dans le cas `V0 = 0`, avec le programme `PaquetOndes.py`. La comparaison peut, dans un premier temps, se faire sans représenter les paquets d’ondes.
