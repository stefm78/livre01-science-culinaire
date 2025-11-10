# 🏗️ Infrastructure Projet - Livre Science Culinaire

**Version** : 1.0  
**Date** : 2025-11-10  
**Statut** : ✅ Opérationnelle

---

## 📊 Vue d'Ensemble

Ce document décrit l'infrastructure complète du projet de production du livre.

### Architecture Globale

```
livre01-science-culinaire/
├── sources/                   # Documentation projet
│   ├── cadrage-editorial.md
│   ├── charte-visuelle.md
│   ├── base-documentaire.md
│   ├── maquettes-visuelles-recettes.md
│   ├── images/               # Maquettes visuelles
│   └── schemas/              # Schémas scientifiques réutilisables
│
├── images/
│   └── tests/                # Photos tests validation charte
│       ├── test-photo-01.png à 15.png
│       └── README.md
│
├── recettes/                  # ⭐ Production recettes (30 fiches)
│   ├── README.md              # Documentation workflow
│   ├── _template/             # Templates standardisés
│   │   ├── recette.md
│   │   └── metadata.json
│   │
│   ├── [nom-recette]/        # Architecture self-contained
│   │   ├── recette.md
│   │   ├── metadata.json
│   │   └── images/
│   │       ├── hero.png
│   │       ├── process-XX.png
│   │       └── final.png
│   │
│   ├── index.json             # Index généré automatiquement
│   └── INDEX.md               # Index lisible Markdown
│
├── scripts/                   # Outils automatisation
│   ├── validate-recipe.py     # Validation recette individuelle
│   └── generate-index.py      # Génération index automatique
│
├── .github/
│   └── workflows/             # GitHub Actions (CI/CD)
│
├── PROJECT_DNA.yml           # Métadonnées projet
├── INFRASTRUCTURE.md         # Ce fichier
└── README.md                 # Documentation principale
```

---

## 📝 Composants Principaux

### 1. Sources (`sources/`)

**Objectif** : Documentation de cadrage et ressources transversales

**Contenu** :
- Cadrage éditorial (structure 8 chapitres, 30 recettes)
- Charte visuelle (palette, style photo, typographie)
- Base documentaire scientifique
- Maquettes visuelles
- Schémas scientifiques réutilisables

**Statut** : ✅ Complète et validée

---

### 2. Images Tests (`images/tests/`)

**Objectif** : Validation charte visuelle avant production

**Contenu** :
- 15 photos culinaires tests
- Documentation prompts IA
- Comparatif outils (Perplexity, ChatGPT)

**Statut** : 🟡 8/15 photos (issue #7 en cours)

---

### 3. Recettes (`recettes/`) ⭐

**Objectif** : Production des 30 fiches recettes finales

**Architecture** : Self-contained (une recette = un dossier autonome)

**Templates** :
- `_template/recette.md` : Structure markdown 2 pages
- `_template/metadata.json` : Métadonnées structurées

**Workflow** :
1. Copier templates
2. Rédiger contenu
3. Générer images IA
4. Valider via script
5. Commit sur GitHub

**Statut** : ✅ Infrastructure prête, production à démarrer

---

### 4. Scripts (`scripts/`)

**Objectif** : Automatisation qualité et génération

**Outils disponibles** :

#### `validate-recipe.py`
Validation complète d'une recette :
- Fichiers obligatoires présents
- JSON valide
- Images référencées existent
- Structure markdown conforme

**Usage** :
```bash
python scripts/validate-recipe.py recettes/steak-maillard
```

#### `generate-index.py`
Génération automatique des index :
- `recettes/index.json` : Format structuré (API-ready)
- `recettes/INDEX.md` : Format lisible (humains)

**Usage** :
```bash
python scripts/generate-index.py
```

**Statut** : ✅ Opérationnels

---

## 🔄 Workflow de Production

### Phase 1 : Préparation (Actuelle)

- [x] Infrastructure créée
- [x] Templates standardisés
- [x] Scripts de validation
- [ ] Finalisation photos tests (issue #7)
- [ ] Création schémas scientifiques (issue #8)

### Phase 2 : Migration Pilote

- [ ] Transformer `sources/steak-maillard.md` en format production
- [ ] Générer images pour steak-maillard
- [ ] Valider workflow complet
- [ ] Ajuster templates si nécessaire

### Phase 3 : Production Masse (30 Recettes)

**Par chapitre** (selon `sources/cadrage-editorial.md`) :

1. **Bases fondamentales** (5-6 recettes)
2. **Viandes & Volailles** (4-5 recettes)
3. **Poissons & Fruits de mer** (3-4 recettes)
4. **Légumes révélés** (4-5 recettes)
5. **Œufs & Laitages** (3-4 recettes)
6. **Pains & Pâtisseries** (3-4 recettes)
7. **Desserts scientifiques** (4-5 recettes)
8. **Créations audacieuses** (3-4 recettes)

**Pour chaque recette** :
1. Rédaction contenu (`recette.md`)
2. Remplissage métadonnées (`metadata.json`)
3. Génération images (ChatGPT DALL-E 3)
4. Validation automatique (`validate-recipe.py`)
5. Commit Git structuré
6. Mise à jour index (`generate-index.py`)

### Phase 4 : Finalisation

- [ ] Validation complète 30 recettes
- [ ] Génération index final
- [ ] Build PDF/ePub (via Pandoc)
- [ ] Relecture éditoriale
- [ ] Publication

---

## 🛡️ Contrôle Qualité

### Validation Automatique

**Chaque commit recette** déclenche :
1. Validation structure
2. Vérification JSON
3. Contrôle présence images
4. Lint markdown

### Checklist Manuelle

Avant validation finale :
- [ ] Concept scientifique clair
- [ ] Associations moléculaires documentées
- [ ] Étapes reproductibles
- [ ] Variantes pertinentes
- [ ] Images conformes charte
- [ ] Sources citées

---

## 📊 Suivi et KPIs

### Métriques Projet

**Générées via** : `scripts/generate-index.py`

- Total recettes complétées / 30
- Répartition par chapitre
- Répartition par difficulté
- Temps moyen par recette
- Taux de validation automatique

### Issues GitHub

**Organisation** :
- Issue par recette (optionnel)
- Issue par chapitre (recommandé)
- Labels : `recettes`, `chapitre-X`, `validation`

---

## 🔗 Liens Utiles

### Documentation Principale

- [README.md](README.md) : Vue générale projet
- [recettes/README.md](recettes/README.md) : Workflow production détaillé
- [sources/cadrage-editorial.md](sources/cadrage-editorial.md) : Structure livre
- [sources/charte-visuelle.md](sources/charte-visuelle.md) : Style visuel

### Templates

- [recettes/_template/recette.md](recettes/_template/recette.md)
- [recettes/_template/metadata.json](recettes/_template/metadata.json)

### Outils

- [scripts/validate-recipe.py](scripts/validate-recipe.py)
- [scripts/generate-index.py](scripts/generate-index.py)

---

## 🔍 Troubleshooting

### Erreur Validation Recette

**Problème** : `validate-recipe.py` échoue

**Solutions** :
1. Vérifier présence `recette.md` et `metadata.json`
2. Valider JSON sur [jsonlint.com](https://jsonlint.com)
3. Contrôler chemins images dans metadata
4. Vérifier structure markdown (sections obligatoires)

### Images Manquantes

**Problème** : Images référencées mais absentes

**Solutions** :
1. Vérifier noms fichiers (case-sensitive)
2. Contrôler chemins relatifs dans metadata
3. Vérifier présence dossier `images/`

### Index Non Généré

**Problème** : `generate-index.py` ne trouve pas les recettes

**Solutions** :
1. Exécuter depuis racine projet
2. Vérifier structure dossiers
3. Contrôler `metadata.json` valides

---

## 🛠️ Maintenance

### Mise à Jour Templates

**Si modifications nécessaires** :

1. Modifier `recettes/_template/`
2. Documenter changements dans `recettes/README.md`
3. Commit avec message : `feat(templates): [description]`
4. Notifier dans issue projet

### Ajout Nouveaux Scripts

**Pour nouveaux outils** :

1. Créer dans `scripts/`
2. Ajouter shebang Python : `#!/usr/bin/env python3`
3. Documenter usage dans docstring
4. Mettre à jour cette documentation
5. Commit : `feat(scripts): [description]`

---

## 📌 Version History

### v1.0 (2025-11-10)

- ✅ Infrastructure complète créée
- ✅ Templates standardisés
- ✅ Scripts validation + génération index
- ✅ Documentation workflow
- 🟡 Migration fiche pilote (en cours)
- ⏳ Production 30 recettes (à démarrer)

---

**Maintenu par** : Chef de Projet IA  
**Contact** : Issues GitHub avec label `infrastructure`  
**Dernière mise à jour** : 2025-11-10
