# 📚 Recettes - Structure et Workflow de Production

## 📊 Vue d'Ensemble

Ce dossier contient les **30 fiches recettes** du livre, organisées selon une architecture self-contained.

**Statut actuel** : 🟡 Infrastructure prête, production à démarrer après validation issue #7

---

## 🏗️ Structure par Recette

Chaque recette suit cette architecture :

```
recettes/
└── [nom-recette]/
    ├── recette.md              # Contenu markdown (2 pages)
    ├── metadata.json           # Métadonnées structurées
    └── images/
        ├── hero.png            # Photo principale (page 1)
        ├── process-01.png      # Photo(s) étapes (optionnel)
        ├── process-02.png      # Photo(s) étapes (optionnel)
        └── final.png           # Photo présentation finale (page 2)
```

### Exemple Concret

```
recettes/
├── steak-maillard/
│   ├── recette.md
│   ├── metadata.json
│   └── images/
│       ├── hero.png
│       ├── process-01.png
│       └── final.png
│
├── risotto-parmesan/
│   ├── recette.md
│   ├── metadata.json
│   └── images/
│       ├── hero.png
│       └── final.png
│
└── panna-cotta/
    ├── recette.md
    ├── metadata.json
    └── images/
        ├── hero.png
        ├── layers.png
        └── final.png
```

---

## 📝 Format recette.md

### Structure Obligatoire (2 pages)

```markdown
# [Titre Recette]

---

## Page 1 : Présentation + Science

![Photo principale](images/hero.png)

**[TITRE EN MAJUSCULES]**

🔬 **LA SCIENCE**
[Explication du concept scientifique principal]

🌿 **ASSOCIATIONS CLÉS**
- Association 1 → Molécules/effet
- Association 2 → Molécules/effet

⏱️ **INFOS PRATIQUES**
Préparation : X min | Cuisson : Y min | Difficulté : ●○○ | Pour N personnes

---

## Page 2 : Recette + Variantes

🧑‍🍳 **INGRÉDIENTS**
- Ingrédient 1 (quantité)
- Ingrédient 2 (quantité)
- ...

🔥 **PRÉPARATION**
1. Étape 1
2. Étape 2
3. ...

![Photo étape/finale](images/final.png)

🔄 **VARIANTES**
- Variante 1 : ...
- Variante 2 : ...

💡 **ASTUCE SCIENCE**
[Conseil basé sur la science pour réussir la recette]
```

### Conventions Markdown

- **Liens images** : Toujours relatifs (`images/xxx.png`)
- **Émojis** : Standardisés (🔬 🌿 ⏱️ 🧑‍🍳 🔥 🔄 💡)
- **Formatage** : Gras pour titres sections
- **Schémas** : Références vers `../../sources/schemas/` si nécessaire

---

## 🗂️ Format metadata.json

### Structure Complète

```json
{
  "recette": {
    "id": "nom-recette",
    "titre": "Titre Complet de la Recette",
    "slug": "nom-recette",
    "chapitre": "Nom du Chapitre (selon cadrage-editorial.md)",
    "numero_chapitre": 1,
    "numero_recette": 1,
    "difficulte": 1,
    "temps_preparation": 10,
    "temps_cuisson": 5,
    "temps_repos": 0,
    "portions": 2,
    "tags": ["tag1", "tag2", "tag3"]
  },
  
  "science": {
    "concept_principal": "Nom du Concept",
    "temperature": "XXX°C",
    "schemas_associes": ["nom-schema"],
    "associations": [
      {
        "ingredient_a": "Ingrédient A",
        "ingredient_b": "Ingrédient B",
        "molecule": "Molécule ou Effet"
      }
    ]
  },
  
  "images": {
    "hero": {
      "fichier": "images/hero.png",
      "description": "Description de l'image",
      "angle": "top-down|45-degree|macro",
      "page": 1,
      "credits": "ChatGPT DALL-E 3|Perplexity|Autre",
      "date_generation": "YYYY-MM-DD"
    },
    "process": [
      {
        "fichier": "images/process-01.png",
        "description": "Description",
        "angle": "top-down|45-degree|macro",
        "etape": "Nom de l'étape",
        "page": 2
      }
    ],
    "final": {
      "fichier": "images/final.png",
      "description": "Description",
      "angle": "top-down|45-degree|macro",
      "page": 2
    }
  },
  
  "sources_documentaires": [
    "Référence bibliographique 1",
    "Référence bibliographique 2"
  ],
  
  "version": "1.0",
  "date_creation": "YYYY-MM-DD",
  "date_modification": "YYYY-MM-DD",
  "auteur": "Nom de l'auteur/IA",
  "statut": "brouillon|révision|validé|publié"
}
```

### Champs Obligatoires

- `recette.id`, `recette.titre`, `recette.chapitre`
- `science.concept_principal`
- `images.hero.fichier`
- `version`, `date_creation`, `auteur`, `statut`

---

## 🖼️ Conventions Images

### Nomenclature

- `hero.png` : Photo principale (toujours)
- `process-XX.png` : Photos étapes (01, 02, 03...)
- `final.png` : Photo présentation finale (toujours)
- `detail-XX.png` : Détails spécifiques (optionnel)

### Spécifications Techniques

- **Format** : PNG (privilégié) ou JPG
- **Résolution** : 300 DPI minimum
- **Taille** : 2048×2048px minimum
- **Poids** : < 3 MB par image (optimisation requise)
- **Style** : Conforme à `sources/charte-visuelle.md`

### Angles Standardisés

- **top-down** : Vue dessus (plongée 90°)
- **45-degree** : Vue 45° (perspective)
- **macro** : Gros plan détail

---

## 🔄 Workflow de Production

### Étape 1 : Création Structure

```bash
# Créer dossier recette
mkdir -p recettes/nom-recette/images

# Copier templates
cp recettes/_template/recette.md recettes/nom-recette/
cp recettes/_template/metadata.json recettes/nom-recette/
```

### Étape 2 : Rédaction Contenu

1. Rédiger `recette.md` selon template
2. Remplir `metadata.json` avec informations complètes
3. Vérifier conformité format

### Étape 3 : Génération Images

1. Générer images via ChatGPT DALL-E 3 (ou autre outil)
2. Télécharger et renommer selon conventions
3. Placer dans `recettes/nom-recette/images/`
4. Optimiser poids si > 3 MB

### Étape 4 : Validation

```bash
# Valider la recette
python scripts/validate-recipe.py recettes/nom-recette
```

### Étape 5 : Commit

```bash
git add recettes/nom-recette
git commit -m "feat(recettes): ajout [Nom Recette] - Chapitre X"
git push origin main
```

---

## 🛠️ Scripts Disponibles

### Validation Recette

```bash
# Valider une recette spécifique
python scripts/validate-recipe.py recettes/steak-maillard

# Valider toutes les recettes
python scripts/validate-all-recipes.py
```

### Génération Index

```bash
# Générer index.json automatique
python scripts/generate-index.py
```

### Statistiques

```bash
# Afficher stats projet
python scripts/stats-recettes.py
```

---

## 📋 Checklist Qualité

Avant de considérer une recette comme **validée** :

### Contenu
- [ ] `recette.md` suit le template 2 pages
- [ ] Concept scientifique clairement expliqué
- [ ] Associations moléculaires documentées
- [ ] Étapes de préparation claires et testables
- [ ] Variantes proposées
- [ ] Astuce science pertinente

### Métadonnées
- [ ] `metadata.json` complet et valide (JSON)
- [ ] Tous les champs obligatoires remplis
- [ ] Tags pertinents et cohérents
- [ ] Sources documentaires citées

### Images
- [ ] Photo hero présente et conforme charte
- [ ] Photo final présente et conforme charte
- [ ] Images référencées existent physiquement
- [ ] Poids images < 3 MB
- [ ] Style cohérent avec charte visuelle

### Technique
- [ ] Validation script OK
- [ ] Liens relatifs fonctionnels
- [ ] Pas d'erreurs markdown
- [ ] Commit message descriptif

---

## 📊 Suivi Production

### Objectif Final

**30 recettes** réparties en **8 chapitres** (selon `sources/cadrage-editorial.md`)

### État Actuel

- ✅ Infrastructure créée
- ✅ Templates disponibles
- 🟡 Fiche pilote à migrer (steak-maillard)
- ⏳ Production 29 recettes restantes

### Prochaines Étapes

1. **Issue #7** : Finaliser banque 15 photos tests
2. **Issue #8** : Créer 8 schémas scientifiques
3. **Migration** : Transformer `sources/steak-maillard.md` en format production
4. **Production** : Rédiger et illustrer 29 recettes restantes
5. **Build** : Générer livre complet (PDF/ePub)

---

## 🔗 Ressources

### Documentation Projet

- `sources/cadrage-editorial.md` : Structure chapitres et recettes
- `sources/charte-visuelle.md` : Style photographique
- `sources/base-documentaire.md` : Sources scientifiques
- `sources/schemas/` : Schémas scientifiques réutilisables

### Templates

- `recettes/_template/recette.md` : Template contenu
- `recettes/_template/metadata.json` : Template métadonnées

### Scripts

- `scripts/validate-recipe.py` : Validation individuelle
- `scripts/validate-all-recipes.py` : Validation complète
- `scripts/generate-index.py` : Génération index
- `scripts/stats-recettes.py` : Statistiques projet

---

## 🆘 Support

Pour toute question ou problème :

1. Consulter cette documentation
2. Vérifier les templates dans `recettes/_template/`
3. Créer une issue GitHub avec label `recettes`
4. Mentionner @Chef-Projet-IA

---

**Version** : 1.0  
**Date** : 2025-11-10  
**Auteur** : Chef de Projet IA  
**Statut** : ✅ Infrastructure opérationnelle
