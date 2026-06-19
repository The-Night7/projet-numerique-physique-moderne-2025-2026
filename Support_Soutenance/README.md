# Support de soutenance

Présentation Beamer (16:9) pour la soutenance orale (23 juin), à déposer en PDF
au plus tard le **samedi 20 juin à 12h**.

## Compilation

```bash
pdflatex presentation.tex
pdflatex presentation.tex   # deux passes pour la pagination
```

Produit `presentation.pdf` (13 diapositives). Les figures sont des copies de
celles des parties 1, 2 et 4 (dossier `figures/`) — si les scripts sont
relancés, recopier les PNG mis à jour.

> Les études d'influence du paquet lui-même (k₀, a_wp — sections 4.1.f/4.1.g
> de `Partie 4/explication.md`) ont été retirées du périmètre du projet, trop
> volumineuses pour le temps imparti. Elles n'apparaissent donc plus dans le
> diaporama ; l'idée qu'elles portaient (filtrage spectral) reste mentionnée
> en perspective sur la diapo de conclusion.

## Plan et minutage mesuré par moi à l'oral (≈15 min 30 sec)

| Diapo | Contenu | Durée |
|---|---|---|
| 1–2 | Titre, problématique et démarche | 1,5 min |
| 3 | Motivation : onde plane → superposition → paquet d'ondes | 0,5 min |
| 4 | Paquet d'ondes gaussien (v_g, Δk, dispersion) | 1,5 min |
| 5 | États stationnaires de la barrière (**indispensable**) | 2 min |
| 6 | Méthode numérique : Crank–Nicolson + Thomas | 1,5 min |
| 7 | Validation particule libre (τ₀ à 4 %) | 1 min |
| 8–9 | Évolution face à la barrière, réflexion/transmission | 2 min |
| 10 | Temps de groupe de Hartman, τ_t < τ₀ (**résultat central**, approfondi) | 2,5 min |
| 11–12 | Influence de la barrière : a (saturation) et V₀ | 1,5 min |
| 13 | Conclusion et perspectives (dont k₀/a_wp, écartés du périmètre) | 1,5 min |