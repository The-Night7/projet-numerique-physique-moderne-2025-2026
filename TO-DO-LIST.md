**Partie 4**

- [X] `Partie 4/réponses-aux-questions.md` : ajouter l'explication du décrochage de τ_t,num au-delà de a≈1.5 (filtrage spectral / signal transmis trop faible face au bruit numérique) — actuellement seule la remarque vague à la ligne 77 en parle, sans la justification claire qui est dans le README de soutenance.
- [X] `Partie 4/réponses-aux-questions.md` : ajouter l'explication de l'écart 8,1 % (mesuré) vs 2,5 % (|T(k₀)|² théorique) — paquet non monochromatique, transmission préférentielle des composantes rapides. Déjà bien rédigée diapo 8, juste à copier/adapter.
- [ ] `Partie 4/Figure_3_influence_a.png` : corriger le titre (« saturation de τ_t ») qui contredit la courbe numérique affichée, ou n'afficher τ_t,num que pour a≤1 avec une annotation indiquant que la mesure n'est plus fiable au-delà.
- [X] `Partie 4/EffetTunnel1d2A.py` : relancer la simulation avec nx/nt doublés (ex. nx=3000, nt=6000) pour vérifier si l'écart de 33 % sur τ_t,num à a=1 se réduit — préparer ce chiffre pour la soutenance.
- [ ] `Partie 4/réponses-aux-questions.md` : corriger les coquilles dans les tableaux — « 4.1.47 » → 4.472, « 14.1.0 » → 14.0, « 4.1.9×10⁻² » → 4.9×10⁻².

**Partie 2**

- [X] `Partie 2/réponses-aux-questions.md` (question 2.2.1.b) : remplacer votre g(k) = (2a/π)^{1/4}exp[-a(k-k0)²] par la formule officielle déjà donnée dans le sujet (g(k) = √a(2π)^{-1/4}exp[-a²(k-k0)²/4]) et dérouler le calcul de (c) avec ce même a, pour éviter le changement de variable silencieux.
- [X] `Partie 2/réponses-aux-questions.md` (question 2.2.1.d) : remplacer l'affirmation « l'intégration donnera bien 1 » par le calcul explicite de l'intégrale gaussienne.
- [X] `Partie 2/PaquetOndeGauss1d2A.py` : soit passer le code en unités atomiques/nm-fs-eV comme indiqué dans votre propre réponse à la question (e), soit préciser dans le texte que le correctif n'est appliqué qu'à partir de la Partie 3.

**Partie 3**

- [X] `Partie 3/réponses-aux-questions.md` (question 3.1.1.d) : corriger « schéma progressif, erreur d'ordre 1 » → schéma centré, erreur d'ordre 2 (cohérent avec le code).
- [X] `Partie 3/EquaSchro1d2A.py` ou le markdown : ajouter un test de convergence avec une fonction non polynomiale (ex. sin(x)) à plusieurs dx, et tracer log(erreur) vs log(dx) pour démontrer l'ordre 2 — le test sur x² actuel ne le permet pas (dérivées d'ordre 3+ nulles).

**Support Soutenance**

- [ ] `presentation.tex` : ajouter une diapositive ou quelques puces de transition sur la Partie 1 (ondes planes/battements), même brève, pour respecter la consigne du mail du prof.

**Dépôt GitHub**

- [X] Ajouter un `.gitignore` (au minimum : `__pycache__/`, `*.pyc`, `*.aux`, `*.log`, `*.fls`, `*.fdb_latexmk`, `*.synctex.gz`, `*.out`, `*.nav`, `*.snm`, `*.vrb`).
- [X] Supprimer du dépôt les fichiers de compilation déjà commités (`Partie 3/__pycache__`, `Partie 4/__pycache__`, fichiers `.aux/.log/.fls/...` dans `Support Soutenance/` et `Support Soutenance/Scripts/`).

**Révision générale (pas un fichier à corriger, mais à ne pas oublier)**

- [ ] Réviser le cours de physique moderne au sens large (Panorama, Mécanique du point, Électromagnétisme, Ondes) puisque les questions du jury peuvent porter dessus, pas seulement sur le projet.
