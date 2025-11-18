# 📄 Production PAO - Livre Science Culinaire MVP

**Objectif** : Transformer le contenu MVP (16 recettes, 30 pages éditorial) en livre imprimable professionnel (PDF).

**Format cible** : 100-120 pages A4, impression qualité professionnelle.

**Deadline** : 13 décembre 2025

---

> ## 🤖 **IA RESPONSABLE PAO ?**
> ### → **[GUIDE_PAO.md](GUIDE_PAO.md)** ← **LIS ÇA D'ABORD (3 min)**
> Tu sauras exactement comment procéder.

---

## 📊 Vue d'Ensemble

### Contenu Source Disponible

**Recettes** : 16 fichiers markdown (2 pages chacune)
- Chapitre 1 : 4 recettes → `../recettes/*/recette.md`
- Chapitre 2 : 4 recettes → `../recettes/*/recette.md`
- Chapitre 3 : 4 recettes → `../recettes/*/recette.md`
- Chapitre 4 : 4 recettes → `../recettes/*/recette.md`

**Contenu éditorial** : 9 fichiers markdown (30 pages)
- Introduction : `../content/00-introduction/introduction.md`
- 4 Intercalaires : `../content/0X-*/intercalaire.md`
- Glossaire : `../content/99-annexes/glossaire.md`
- Index : `../content/99-annexes/index-recettes.md`
- Bibliographie : `../content/99-annexes/bibliographie.md`
- Crédits : `../content/99-annexes/credits.md`

**Visuels** : 32+ fichiers
- Images hero : `../recettes/*/images/hero.png`
- Images process : `../recettes/*/images/process-*.png`
- Schémas : `../../sources/schemas/*.png`

---

## 🎯 Workflow PAO - 3 Phases

### Phase 1 : Préparation (Semaine 25-29 nov)

**Responsable** : Designer-PAO IA

**Actions** :
1. Setup logiciel PAO
2. Installation polices
3. Optimisation images (300dpi CMJN)
4. Création templates master pages

**Livrables** :
- Templates InDesign/Affinity Publisher
- Images optimisées dans `images-print/`
- Polices installées
- Guide styles typographiques

**Issue** : #54 (à créer)

### Phase 2 : Assemblage (Semaine 2-6 déc)

**Responsable** : Designer-PAO IA

**Actions** :
1. Import contenu markdown → PAO
2. Placement recettes (format 2 pages)
3. Intégration images
4. Application styles
5. Génération table des matières

**Livrables** :
- Fichier PAO complet (.afpub ou .indd)
- 75-90 pages assemblées
- Table des matières générée
- Numérotation préliminaire

**Issue** : #55 (à créer)

### Phase 3 : Finalisation (Semaine 9-13 déc)

**Responsable** : Reviewer-Qualité IA + Designer-PAO IA

**Actions** :
1. Relecture complète
2. Corrections veuves/orphelines
3. Vérification références croisées
4. Export PDF print + web
5. Tests impression

**Livrables** :
- PDF print final (CMJN, 300dpi)
- PDF web (RGB, 150dpi)
- Fichier source PAO archivé
- Rapport qualité

**Issue** : #56 (à créer)

---

## 📁 Structure Dossier Production

```
livre/production/
├── README.md                    # Ce fichier
├── GUIDE_PAO.md                 # Guide détaillé pour IA
├── CHECKLIST_PAO.md             # Checklist validation
├── CONVENTIONS_TYPO.md          # Règles typographiques
│
├── 01-preparation/
│   ├── README.md                # Instructions Phase 1
│   ├── specifications.md        # Specs techniques impression
│   ├── templates/               # Templates master pages
│   │   ├── master-cover.md
│   │   ├── master-intro.md
│   │   ├── master-recipe.md
│   │   └── master-annexes.md
│   └── fonts/                   # Polices projet
│       ├── Playfair/
│       ├── Inter/
│       └── Crimson/
│
├── 02-assemblage/
│   ├── README.md                # Instructions Phase 2
│   ├── ordre-import.md          # Ordre placement contenu
│   ├── styles.md                # Définitions styles typo
│   └── images-optimized/        # Images 300dpi CMJN
│
├── 03-finalisation/
│   ├── README.md                # Instructions Phase 3
│   ├── checklist-final.md       # Validation pré-export
│   └── exports/                 # PDF finaux
│       ├── print/               # Version impression
│       └── web/                 # Version web
│
└── scripts/
    ├── optimize-images.py       # Conversion 300dpi CMJN
    ├── extract-markdown.py      # Export contenu structuré
    └── validate-pdf.py          # Validation PDF final
```

---

## 🛠️ Outils Recommandés

### Logiciels PAO

**Option 1 : Affinity Publisher** (Recommandé)
- ✅ Licence perpétuelle (~70€)
- ✅ Interface intuitive
- ✅ Export PDF professionnel
- ✅ Gestion CMJN native
- ✅ Compatible macOS/Windows

**Option 2 : Adobe InDesign**
- ✅ Standard industrie
- ✅ Fonctionnalités avancées
- ❌ Abonnement mensuel
- ✅ Compatibilité maximale

**Option 3 : Scribus** (Open Source)
- ✅ Gratuit
- ✅ Export PDF print
- ❌ Courbe apprentissage
- ⚠️ Interface moins moderne

### Scripts Python

**Fournis dans `scripts/`** :
- `optimize-images.py` : Conversion batch 300dpi CMJN
- `extract-markdown.py` : Export contenu structuré
- `validate-pdf.py` : Vérification PDF final

---

## 📋 Checklist Globale

### Préparation
- [ ] Logiciel PAO installé et configuré
- [ ] Polices téléchargées (Playfair, Inter, Crimson)
- [ ] Images optimisées 300dpi CMJN
- [ ] Templates master pages créés
- [ ] Guide styles défini

### Assemblage
- [ ] Introduction importée (10 pages)
- [ ] 16 recettes placées (32 pages)
- [ ] 4 intercalaires insérés (4 pages)
- [ ] Annexes ajoutées (20 pages)
- [ ] 32+ images intégrées
- [ ] Styles appliqués
- [ ] Table des matières générée

### Finalisation
- [ ] Numérotation pages complète
- [ ] Veuves/orphelines corrigées
- [ ] Relecture orthographe
- [ ] Références croisées vérifiées
- [ ] Export PDF print (CMJN, 300dpi)
- [ ] Export PDF web (RGB, 150dpi)
- [ ] Tests impression réalisés

---

## 📞 Support & Resources

**Documentation PAO** :
- [GUIDE_PAO.md](GUIDE_PAO.md) - Guide complet étape par étape
- [CHECKLIST_PAO.md](CHECKLIST_PAO.md) - Validation qualité
- [CONVENTIONS_TYPO.md](CONVENTIONS_TYPO.md) - Règles typographiques

**Issues** :
- #54 : Phase 1 - Préparation PAO
- #55 : Phase 2 - Assemblage PAO
- #56 : Phase 3 - Finalisation PAO
- #53 : Milestone MVP 100% (référence)

**Contact** : smagnand@gmail.com

---

## 🎯 Objectif Final

**PDF Print** :
- Format : A4 (210×297 mm)
- Résolution : 300dpi minimum
- Couleur : CMJN
- Fonds perdus : 3mm
- Reliure : Dos carré collé recommandé

**PDF Web** :
- Format : A4 (210×297 mm)
- Résolution : 150dpi
- Couleur : RGB
- Optimisé : Taille fichier réduite

**Date livraison** : 13 décembre 2025

---

*Production PAO - MVP v1.0 - Novembre 2025*
