# 📄 Résumé du Projet Numérique en Physique Moderne

## 🎯 Thème Central et Objectif Principal

Ce projet porte sur l'**effet tunnel en mécanique quantique**, phénomène par lequel une particule peut franchir une barrière de potentiel même si son énergie classique est insuffisante. L'objectif principal est d'étudier ce phénomène à travers une approche à la fois **analytique et numérique**, en se limitant à une dimension d'espace avec une barrière rectangulaire de potentiel. 

---

## 📚 Structure et Progression du Projet

Le projet est organisé en **quatre grandes parties** :

### 1️⃣ Ondes Planes
- Rappel de l'expression d'une onde plane (1D et 3D), signification de $\vec{k}$ et $\omega$
- Étude de la fonction d'onde comme solution de l'équation de Schrödinger pour une particule libre
- Calcul de la **relation de dispersion**, vitesse de phase et vitesse de groupe
- Vérification de la condition de normalisation et des limites physiques des ondes planes 
- **Implémentation Python** : programme `OndePlane1dXY.py` pour visualiser les parties réelle et imaginaire d'une onde plane 

### 2️⃣ Superposition d'Ondes Planes
- Justification de la linéarité de l'équation de Schrödinger 
- Étude de la superposition de trois ondes planes et calcul de la **densité de probabilité de présence** 
- Représentation graphique avec enveloppe sur l'intervalle $$[-\pi/\Delta k,\ \pi/\Delta k]$$ 

### 3️⃣ Paquets d'Ondes Gaussiens
- Expression générale d'un paquet d'ondes en 3D et 1D 
- Étude du **paquet d'ondes gaussien** : cas particulier où $g(k)$ est une gaussienne 
$$g(k) = \sqrt{a}\,[2\pi]^{-1/4}\exp\left[-\frac{a^2(k-k_0)^2}{4}\right]$$
- Calcul analytique du paquet d'ondes à l'instant $t$, vérification de la normalisation 
- Lien avec la **transformée de Fourier** 
- **Implémentation Python** : programme `PaquetOndeGauss1dXY.py` pour simuler l'évolution temporelle du paquet d'ondes gaussien 

### 4️⃣ Résolution Numérique & Temps de Traversée
- Résolution numérique de l'équation de Schrödinger pour un paquet d'ondes rencontrant une barrière de potentiel 
- Détermination du **temps de traversée de la barrière** (travail hors séances de TD) 

---

## 💡 Idées Clés et Points Importants

| Concept | Description |
|---|---|
| **Effet tunnel** | Une particule quantique peut franchir une barrière même sans énergie suffisante  |
| **Fonction d'onde** | Décrit la probabilité de présence, remplace la trajectoire classique  |
| **Équation de Schrödinger** | Gouverne l'évolution de l'état quantique (linéaire)  |
| **Paquet d'ondes** | Superposition d'ondes planes, représentation plus réaliste d'une particule  |
| **Approche numérique** | Simulation Python indispensable pour les cas non solubles analytiquement  |

---

## ⚠️ Remarques Importantes

- **Esprit du projet** : L'essentiel est de maîtriser chaque étape intermédiaire, pas nécessairement de tout terminer. 
- **Utilisation de l'IA** : Strictement encadrée — l'IA ne peut servir qu'à **relire** le travail, non à le produire. Tout usage non déclaré est considéré comme une fraude. 
- **Outils Python** utilisés : `numpy`, `matplotlib` pour les calculs et visualisations scientifiques. 