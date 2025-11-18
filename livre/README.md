# 📚 Production Livre - Organisation

**Version** : MVP 1.0  
**Objectif** : Livre 100-120 pages, 16 recettes, 4 chapitres  
**Deadline** : 27 décembre 2025  

---

## 📌 Vue d'Ensemble

Ce dossier `livre/` centralise **tout le contenu et la production du livre final**, distinct des recettes individuelles dans `recettes/`.

---

## 📁 Structure Dossiers

### `content/` - Contenu Éditorial

Contenu spécifique au livre (hors recettes) :

```
content/
├── 00-introduction/
│   ├── introduction.md      # 10 pages introduction
│   └── images/              # Photos d'ambiance
│
├── 01-bases/
│   └── intercalaire.md      # Page intercalaire Ch.1
│
├── 02-viandes/
│   └── intercalaire.md      # Page intercalaire Ch.2
│
├── 03-poissons/
│   └── intercalaire.md      # Page intercalaire Ch.3
│
├── 04-legumes/
│   └── intercalaire.md      # Page intercalaire Ch.4
│
└── 99-annexes/
    ├── glossaire.md         # 6 pages glossaire
    ├── index-recettes.md    # 2 pages index
    ├── bibliographie.md     # 2 pages biblio
    └── credits.md           # 2 pages crédits
```

**Note** : Les recettes elles-mêmes restent dans `recettes/` et sont référencées depuis le livre.

---

### `production/` - Mise en Page PAO

Fichiers de production professionnelle :

```
production/
├── templates/
│   ├── master-pages.indd       # Templates InDesign
│   ├── styles-texte.indd       # Styles typographiques
│   └── styles-images.indd      # Cadres images
│
├── fonts/
│   ├── PlayfairDisplay/        # Police titres
│   ├── Inter/                  # Police corps
│   └── CrimsonText/            # Police citations
│
├── images-optimized/
│   ├── recettes/               # Images recettes 300dpi CMJN
│   ├── schemas/                # Schémas scientifiques optimisés
│   └── ambiance/               # Photos d'ambiance introduction
│
└── exports/
    ├── livre-mvp-v1.0-print.pdf    # PDF impression (CMJN, 300dpi)
    ├── livre-mvp-v1.0-web.pdf      # PDF web (RGB, 150dpi)
    └── sources/
        └── livre-mvp-v1.0.indd     # Fichier source InDesign
```

---

### `scripts/` - Automatisation

Scripts spécifiques production livre :

```python
# generate-book-content.py
# Assemble contenu depuis recettes/ et content/ vers format PAO

# optimize-images.py
# Optimise images : 300dpi, CMJN, compression

# export-to-indesign.py
# Génère fichiers importés InDesign (IDML/XML)
```

---

## 📋 MVP-PLAN.md

Plan détaillé production MVP avec :
- Planning hebdomadaire
- Checklist complète
- État d'avancement
- Dépendances recettes

---

## 🛠️ Workflow Production

### Phase 1 : Complétion Recettes (Semaines 1-2)
```bash
# Compléter Ch.1 + Sprint 4
# Résultat : 16 recettes dans recettes/
```

### Phase 2 : Rédaction Contenu Éditorial (Semaine 3)
```bash
cd livre/content/
# Rédiger introduction.md
# Rédiger 4 intercalaires
# Rédiger annexes
```

### Phase 3 : Optimisation Images (Semaine 3)
```bash
python livre/scripts/optimize-images.py
# Optimise toutes images pour impression
```

### Phase 4 : Mise en Page PAO (Semaine 4)
```bash
# InDesign/Publisher :
# 1. Créer templates
# 2. Importer contenu
# 3. Placer images
# 4. Appliquer styles
# 5. Exporter PDF
```

---

## 📊 Progression MVP

### Recettes (16 totales)
- ✅ Chapitre 1 : 0/4 (en cours)
- ✅ Chapitre 2 : 4/4 (complet)
- ✅ Chapitre 3 : 4/4 (complet)
- ⌛ Chapitre 4 : 0/4 (semaine 2)

### Contenu Éditorial
- ⌛ Introduction : 0/10 pages
- ⌛ Intercalaires : 0/4 pages
- ⌛ Annexes : 0/12 pages

### Mise en Page
- ⌛ Templates PAO : 0%
- ⌛ Import contenu : 0%
- ⌛ Optimisation images : 0%
- ⌛ Export final : 0%

---

## 🔗 Liens Utiles

- 📋 [MVP-PLAN.md](MVP-PLAN.md) : Plan détaillé complet
- 📖 [RECETTES_LISTE.md](../RECETTES_LISTE.md) : Liste 31 recettes
- 🗺️ [ROADMAP.md](../ROADMAP.md) : Planning global
- 🎨 [Charte Visuelle](../sources/charte-visuelle.md)

---

**Créé le** : 18 novembre 2025  
**Maintenu par** : Chef Projet IA  
**Version** : MVP 1.0