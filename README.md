# Projet Numérique : Physique Moderne 2025-2026

Ce projet explore l'**effet tunnel en mécanique quantique**, phénomène par lequel une particule peut franchir une barrière de potentiel même si son énergie classique est insuffisante. L'objectif est d'étudier ce phénomène à travers une approche **analytique et numérique** (en 1D avec une barrière rectangulaire de potentiel).

---

## Structure du Référentiel

Le projet est divisé en plusieurs parties correspondant aux étapes d'apprentissage et de modélisation :

### Partie 1 : Ondes Planes et Superposition

**Dossier :** [`Partie 1/`](./Partie%201)  <br>
**Script Python :** [`OndePlane1d2A.py`](./Partie%201/OndePlane1d2A.py)<br>
**Réponses aux questions :** : [`réponses-aux-questions.md`](./Partie%201/réponses-aux-questions.md)


Cette partie vise à modéliser et visualiser une onde plane à une dimension (1D), puis d'étudier le phénomène d'interférence (battements) obtenu en superposant trois ondes planes de nombres d'onde légèrement différents, illustrant ainsi la formation rudimentaire d'un "paquet d'ondes".

- **Onde Plane Simple :** Représentation de $\Psi(x, t) = A \cdot e^{i(kx - \omega t)}$ (parties réelle et imaginaire).
- **Superposition :** Addition d'une onde centrale et de deux ondes satellites pour illustrer le principe de superposition linéaire.
- **Densité de Probabilité :** Calcul et visualisation de la densité de probabilité ($|\Psi|^2$), montrant la localisation émergente de la particule.

### Partie 2 : Paquets d'Ondes Gaussiens

**Dossier :** [`Partie 2/`](./Partie%202)  <br>
**Script Python :** [`PaquetOndeGauss1d2A.py`](./Partie%202/PaquetOndeGauss1d2A.py) <br>
**Réponses aux questions :** : [`réponses-aux-questions.md`](./Partie%202/réponses-aux-questions.md)

Cette section modélise un paquet d'ondes gaussien en 1D, qui constitue une représentation mathématique classique d'une particule en mécanique quantique (ex. un électron libre).

- Définition de l'amplitude de probabilité et de l'enveloppe gaussienne.
- Introduction du facteur d'étalement du paquet d'ondes au cours du temps et calcul de la vitesse de groupe.
- Tracé des parties réelle et imaginaire de la fonction d'onde quantique à un instant donné.

### Partie 2 : Paquets d'Ondes Gaussiens

**Dossier :** [`Partie 3/`](./Partie%203)  <br>
**Script Python :** [`uncertainnom.py`](./Partie%203/uncertainnom.py) <br>
**Réponses aux questions :** : [`réponses-aux-questions.md`](./Partie%203/réponses-aux-questions.md)

---

## Concepts Abordés

- **Fonction d'onde $\Psi(x,t)$ :** Décrit l'amplitude de probabilité de présence, remplaçant la notion de trajectoire classique.
- **Équation de Schrödinger :** Gouverne l'évolution de l'état quantique (équation linéaire).
- **Paquet d'ondes :** Superposition d'ondes planes pour représenter de façon plus réaliste une particule localisée.
- **Densité de probabilité $\rho = |\Psi|^2$ :** Représente la probabilité de trouver la particule à une position $x$.

---

## Outils et Technologies

- **Langage :** Python 3 (plus précisemment 3.14)
- **Bibliothèques :** 
  - `numpy` : Pour les calculs numériques, les vecteurs et les nombres complexes.
  - `matplotlib` : Pour la visualisation scientifique des ondes et de leur comportement.

---

## Remarques/Commentaires ?

- L'essentiel du projet réside dans la maîtrise de chaque étape intermédiaire (physique et code) plutôt que dans la complétion exhaustive.
- L'utilisation d'intelligences artificielles est strictement encadrée (tolérée uniquement pour la relecture/correction de forme). Tout usage abusif (génération de code non comprise) est proscrit. Nous ne l'avons utilisé que pour vérifier certaines notions de cours sous la forme de NotebookLM.
- Pour davantage de détails sur le cahier des charges d'origine, consultez le fichier [Projet_2526.pdf](./Projet_2526.pdf).



## Projet réalisé dans le cadre de l'UE Sciences - Module Introduction à la Physique Moderne - CY Tech - 2025/2026.