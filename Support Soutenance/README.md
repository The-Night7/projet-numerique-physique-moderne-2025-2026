# Support de soutenance

Présentation Beamer (16:9) pour la soutenance orale (22–26 juin), à déposer en PDF
au plus tard le **vendredi 19 juin à 12h**.

## Compilation

```bash
pdflatex presentation.tex
pdflatex presentation.tex   # deux passes pour la pagination
```

Produit `presentation.pdf` (14 diapositives). Les figures sont des copies de
celles des parties 2 et 4 (dossier `figures/`) — si les scripts sont relancés,
recopier les PNG mis à jour.

## Plan et minutage suggéré (15 min)

| Diapo | Contenu | Durée |
|---|---|---|
| 1–2 | Titre, problématique et démarche | 1,5 min |
| 3 | Paquet d'ondes gaussien (v_g, Δk, dispersion) | 1,5 min |
| 4 | États stationnaires de la barrière (**indispensable**) | 2 min |
| 5 | Méthode numérique : Crank–Nicolson + Thomas | 1,5 min |
| 6 | Validation particule libre (τ₀ à 4 %) | 1 min |
| 7–8 | Évolution face à la barrière, réflexion/transmission | 2 min |
| 9 | Temps de groupe de Hartman, τ_t < τ₀ | 2 min |
| 10–11 | Influence de la barrière : a (saturation) et V₀ | 1,5 min |
| 12–13 | Influence du paquet : k₀ (temps négatifs !) et a_wp (filtrage spectral) | 2 min |
| 14 | Conclusion et perspectives | 1 min |

## Questions probables du jury

- Refaire le raccordement des états stationnaires au tableau (diapo 4).
- Pourquoi Crank–Nicolson plutôt qu'Euler explicite ? (unitarité, stabilité).
- Les temps négatifs de la diapo 12 violent-ils la causalité ? (non : filtrage
  spectral, le pic n'est pas un objet qui se propage — voir
  `Partie 4/explication.md`, section 4.1.f).
- Pourquoi P_trans mesurée > |T(k₀)|² ? (paquet non monochromatique, diapo 13).
- Effet Hartman et superluminalité apparente : que se passe-t-il pour a → ∞ ?
