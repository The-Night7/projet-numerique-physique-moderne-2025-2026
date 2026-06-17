# Support de soutenance

Présentation Beamer (16:9) pour la soutenance orale (22–26 juin), à déposer en PDF
au plus tard le **vendredi 19 juin à 12h**.

## Compilation

```bash
pdflatex presentation.tex
pdflatex presentation.tex   # deux passes pour la pagination
```

Produit `presentation.pdf` (12 diapositives). Les figures sont des copies de
celles des parties 2 et 4 (dossier `figures/`) — si les scripts sont relancés,
recopier les PNG mis à jour.

> Les études d'influence du paquet lui-même (k₀, a_wp — sections 4.1.f/4.1.g
> de `Partie 4/explication.md`) ont été retirées du périmètre du projet, trop
> volumineuses pour le temps imparti. Elles n'apparaissent donc plus dans le
> diaporama ; l'idée qu'elles portaient (filtrage spectral) reste mentionnée
> en perspective sur la diapo de conclusion.

## Plan et minutage suggéré (15 min)

| Diapo | Contenu | Durée |
|---|---|---|
| 1–2 | Titre, problématique et démarche | 1,5 min |
| 3 | Paquet d'ondes gaussien (v_g, Δk, dispersion) | 1,5 min |
| 4 | États stationnaires de la barrière (**indispensable**) | 2 min |
| 5 | Méthode numérique : Crank–Nicolson + Thomas | 1,5 min |
| 6 | Validation particule libre (τ₀ à 4 %) | 1 min |
| 7–8 | Évolution face à la barrière, réflexion/transmission | 2 min |
| 9 | Temps de groupe de Hartman, τ_t < τ₀ (**résultat central**, approfondi) | 2,5 min |
| 10–11 | Influence de la barrière : a (saturation) et V₀ | 1,5 min |
| 12 | Conclusion et perspectives (dont k₀/a_wp, écartés du périmètre) | 1,5 min |

## Questions probables du jury

- Refaire le raccordement des états stationnaires au tableau (diapo 4).
- Pourquoi Crank–Nicolson plutôt qu'Euler explicite ? (unitarité, stabilité).
- Avez-vous étudié l'influence des caractéristiques du paquet lui-même
  (k₀, a_wp) ? (Oui, mais écarté du périmètre final par souci de temps.
  L'idée : à $k_0$ fixé, un paquet étroit en $x$ est large en $k$, et la
  barrière transmet préférentiellement ses composantes rapides — d'où des
  temps apparents parfois négatifs à petit $k_0$, qui convergent vers la
  théorie de Hartman quand le paquet redevient quasi monochromatique.)
- Pourquoi P_trans mesurée > |T(k₀)|² ? (paquet non monochromatique, la
  barrière favorise les composantes rapides — diapo 8).
- Effet Hartman et superluminalité apparente : que se passe-t-il pour a → ∞ ?
