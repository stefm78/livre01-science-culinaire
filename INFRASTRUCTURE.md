# 🏗️ Infrastructure Projet - Livre Science Culinaire

**Version** : 1.1  
**Date** : 2025-11-11  
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
├── _inbox/                    # ⭐ NOUVEAU : Pipeline images IA
│   └── images/
│       ├── BATCH-TEMPLATE.md         # Template instructions IA
│       ├── manifest-*.json           # Manifests en attente
│       └── manifest-*-processed.json # Archives traitées
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
├── import_batch_images.py     # ⭐ NOUVEAU : Import batch images IA
│
├── .github/
│   └── workflows/             # GitHub Actions (CI/CD)
│       └── import-images.yml      # ⭐ NOUVEAU : Workflow import images
│
├── PROJECT_DNA.yml           # Métadonnées projet
├── INFRASTRUCTURE.md         # Ce fichier
└── README.md                 # Documentation principale
```

---

## 🖼️ Pipeline Images IA Automatisé ⭐ NOUVEAU

### Vue d'ensemble

Le projet utilise un pipeline automatisé pour l'intégration des images générées par IA (ChatGPT, DALL-E, etc.) dans les dossiers des recettes.

### Workflow

```
1. IA génère images selon BATCH-TEMPLATE.md
   ↓
2. Upload images + manifest dans _inbox/images/
   ↓
3. GitHub Action détecte nouveau manifest
   ↓
4. Script Python lit manifest et déplace images
   ↓
5. Commit automatique + archivage manifest
   ↓
6. Images disponibles dans recettes/*/images/
```

### Processus pour générer un nouveau batch

#### 1. Préparer les instructions

- Copier `_inbox/images/BATCH-TEMPLATE.md`
- Créer `BATCH-XX-INSTRUCTIONS.md` (remplacer XX par le numéro)
- Personnaliser :
  - `{{BATCH_ID}}` → ex: batch3
  - `{{DATE}}` → ex: 20251112
  - `{{DATE_ISO}}` → ex: 2025-11-12T23:00:00Z
  - Ajouter les prompts d'images spécifiques
  - Compléter le manifest avec les bonnes recettes/types
- **IMPORTANT : Ne jamais dépasser 10-12 images par batch**

#### 2. Fournir à l'IA

- Copier tout le contenu du fichier BATCH-XX-INSTRUCTIONS.md
- Le coller dans ChatGPT ou l'IA de génération
- Attendre la génération des images + manifest
- Si plus de 12 images nécessaires : diviser en plusieurs batchs

#### 3. Upload dans le repo

- Télécharger toutes les images générées
- Télécharger le fichier `manifest-batchXX.json`
- Uploader dans `_inbox/images/` sur GitHub (via interface web ou ligne de commande)

#### 4. Traitement automatique

- Le workflow GitHub Actions se déclenche automatiquement
- Le script `import_batch_images.py` déplace les images vers leurs destinations
- Archivage du manifest avec status "processed"
- Commit automatique des changements

### Conventions de nommage

#### Fichiers manifest
- Format : `manifest-{batch_id}.json`
- Exemple : `manifest-batch3-20251112.json`
- Après traitement : `manifest-batch3-20251112-processed.json`

#### Fichiers images dans le batch
- Format : `{recette}-{type}.png`
- Exemples :
  - `bouillon-volaille-hero.png`
  - `steak-maillard-final.png`
  - `mayonnaise-process-01.png`

#### Fichiers images finaux (dans recettes)
- Format : `{type}.png`
- Exemples : `hero.png`, `final.png`, `process-01.png`, `process-02.png`

### Types d'images

- **hero** : Image principale de la recette (plat fini, mise en scène)
- **final** : Résultat final du plat (présentation assiette)
- **process-XX** : Étapes de préparation (XX = 01, 02, 03, etc.)

### Limite de taille des batchs

🚨 **IMPORTANT : Maximum 10-12 images par batch**

Raisons :
- Évite surcharge cognitive humain/IA
- Facilite traçabilité et débogage
- Réduit risque erreurs dans manifest
- Permet validation incrémentale

### Dépannage pipeline images

#### Le workflow ne se déclenche pas
- Vérifier que le fichier est nommé `manifest-*.json`
- Vérifier qu'il est dans `_inbox/images/`
- Vérifier que le status est `"pending"`

#### Les images ne sont pas déplacées
- Vérifier les noms de fichiers dans le manifest
- Vérifier les chemins `target_path`
- Consulter les logs du workflow GitHub Actions

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
3. Générer images IA (via pipeline automatisé)
4. Valider via script
5. Commit sur GitHub

**Statut** : ✅ Infrastructure prête, production en cours (Sprint 1)

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

### Phase 1 : Préparation

- [x] Infrastructure créée
- [x] Templates standardisés
- [x] Scripts de validation
- [x] Pipeline images IA automatisé ⭐ NOUVEAU
- [ ] Finalisation photos tests (issue #7)
- [ ] Création schémas scientifiques (issue #8)

### Phase 2 : Sprint 1 (EN COURS)

- [x] Migration fiche pilote steak-maillard
- [ ] Production Chapitre 1 (5-6 recettes)
- [ ] Génération images via pipeline automatisé
- [ ] Validation workflow complet

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

## 🔗 Liens Utiles

### Documentation Principale

- [README.md](README.md) : Vue générale projet
- [recettes/README.md](recettes/README.md) : Workflow production détaillé
- [sources/cadrage-editorial.md](sources/cadrage-editorial.md) : Structure livre
- [sources/charte-visuelle.md](sources/charte-visuelle.md) : Style visuel

### Templates

- [recettes/_template/recette.md](recettes/_template/recette.md)
- [recettes/_template/metadata.json](recettes/_template/metadata.json)
- [_inbox/images/BATCH-TEMPLATE.md](_inbox/images/BATCH-TEMPLATE.md) ⭐ NOUVEAU

### Outils

- [scripts/validate-recipe.py](scripts/validate-recipe.py)
- [scripts/generate-index.py](scripts/generate-index.py)
- [import_batch_images.py](import_batch_images.py) ⭐ NOUVEAU

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
4. Vérifier traitement batch dans GitHub Actions

---

## 📌 Version History

### v1.1 (2025-11-11) ⭐ NOUVEAU

- ✅ Ajout pipeline images IA automatisé
- ✅ Script `import_batch_images.py`
- ✅ Workflow GitHub Actions `import-images.yml`
- ✅ Template `BATCH-TEMPLATE.md` pour génération IA
- ✅ Documentation complète workflow images

### v1.0 (2025-11-10)

- ✅ Infrastructure complète créée
- ✅ Templates standardisés
- ✅ Scripts validation + génération index
- ✅ Documentation workflow
- 🟡 Migration fiche pilote (en cours)
- ⏳ Production 30 recettes (en cours Sprint 1)

---

**Maintenu par** : Chef de Projet IA  
**Contact** : Issues GitHub avec label `infrastructure`  
**Dernière mise à jour** : 2025-11-11
