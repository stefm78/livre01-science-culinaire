# 🍳 Livre Science Culinaire - Production Collaborative IA

**Projet** : Livre de cuisine scientifique (30 recettes, 8 chapitres, 200-250 pages)  
**Statut** : 🟡 Phase Conception-Validation  
**Infrastructure** : ✅ Opérationnelle (Nov 2025)

---

## 🚀 Démarrage Rapide

### ⚡ Via GitHub Codespaces (Recommandé)

**Environnement prêt en 20 secondes** :

1. Cliquer sur **Code** → **Codespaces** → **Create codespace on main**
2. Ouvrir terminal (`` Ctrl+` ``)
3. Utiliser commandes projet : `help-projet`

**Fonctionnalités** :
- ✅ Python 3.11 + dépendances
- ✅ Git pré-configuré
- ✅ VS Code avec extensions
- ✅ Alias bash pratiques
- ✅ Scripts validation prêts

📚 [Guide Codespaces](.devcontainer/README.md) | ⚡ [Quick Start](.devcontainer/QUICKSTART.md)

---

## 📊 Vue d'Ensemble Projet

### Objectif

Créer un livre de cuisine scientifique combinant :
- 🔬 Science culinaire (réactions chimiques, associations moléculaires)
- 👨‍🍳 Recettes pratiques (30 fiches, 8 chapitres)
- 📸 Photographies IA (style minimaliste scientifique)
- 📈 Schémas pédagogiques (8 concepts clés)

### Cible

**200-250 pages** | **30 recettes** | **8 chapitres** | **60+ images**

---

## 🏗️ Architecture

```
livre01-science-culinaire/
├── sources/                   # Documentation cadrage
│   ├── cadrage-editorial.md    # Structure 8 chapitres
│   ├── charte-visuelle.md      # Style photographique
│   ├── base-documentaire.md    # Sources scientifiques
│   ├── images/                 # Maquettes visuelles
│   └── schemas/                # Schémas scientifiques
│
├── recettes/                  # ⭐ Production 30 fiches
│   ├── _template/             # Templates standardisés
│   └── [nom-recette]/        # Architecture self-contained
│       ├── recette.md
│       ├── metadata.json
│       └── images/
│
├── images/tests/             # Photos validation charte
├── scripts/                  # Outils automatisation
└── .devcontainer/            # Config Codespaces
```

📚 [Documentation complète](INFRASTRUCTURE.md)

---

## 📝 Workflow Production

### Pour les IAs Contributrices

**1. Créer une recette** :
```bash
nouvelle-recette nom-recette  # Via Codespaces
```

**2. Rédiger contenu** :
- `recette.md` : Structure 2 pages (template fourni)
- `metadata.json` : Métadonnées structurées

**3. Générer images** :
- Via ChatGPT DALL-E 3 (ou autre)
- Placer dans `images/` de la recette

**4. Valider** :
```bash
validate recettes/nom-recette
```

**5. Commit** :
```bash
ga recettes/nom-recette
gc "feat(recettes): ajout [Titre]"
gp
```

📚 [Workflow détaillé](recettes/README.md)

---

## 🔗 Documentation Principale

### Pour Démarrer
- ⚡ [Quick Start Codespaces](.devcontainer/QUICKSTART.md)
- 🏗️ [Infrastructure Production](INFRASTRUCTURE.md)
- 📚 [Workflow Recettes](recettes/README.md)

### Cadrage Projet
- 📝 [Cadrage Éditorial](sources/cadrage-editorial.md)
- 🎨 [Charte Visuelle](sources/charte-visuelle.md)
- 📖 [Base Documentaire](sources/base-documentaire.md)

### Templates
- 📝 [Template Recette](recettes/_template/recette.md)
- 🗂️ [Template Métadonnées](recettes/_template/metadata.json)

---

## 📊 Progression Projet

| Composant | Statut | Progression |
|-----------|--------|-------------|
| **Infrastructure** | ✅ Complète | 100% |
| **Codespaces** | ✅ Configuré | 100% |
| **Templates** | ✅ Prêts | 100% |
| **Photos Tests** | 🟡 En cours | 100% (correction emplacement requise) |
| **Schémas** | ⏳ À démarrer | 0% (0/8) |
| **Recettes** | ⏳ À démarrer | 0% (0/30) |

**Phase actuelle** : Conception-Validation  
**Phase suivante** : Production-Contenu (~15 nov 2025)

---

## 🛠️ Outils Disponibles

### Scripts Automatisation
- `scripts/validate-recipe.py` : Validation complète recette
- `scripts/generate-index.py` : Génération index automatique

### Commandes Codespaces
- `nouvelle-recette <nom>` : Créer depuis template
- `validate <dossier>` : Valider recette
- `validate-all` : Valider tout
- `genindex` : Générer index
- `stats` : Statistiques projet
- `help-projet` : Aide complète

---

## 💬 Issues et Suivi

### Issues Actives

- **#7** : 🟡 Banque 15 photos tests (correction emplacement requise)
- **#8** : ⏳ Création 8 schémas scientifiques
- **#9** : ✅ Infrastructure production recettes

### Labels
- `infrastructure` : Outillage et configuration
- `documentation` : Cadrage et guides
- `recettes` : Production fiches recettes
- `validation` : Contrôle qualité

---

## 👥 Contribution

### Pour IAs

1. Consulter documentation dans `sources/` et `recettes/README.md`
2. Utiliser templates dans `recettes/_template/`
3. Valider via `scripts/validate-recipe.py`
4. Commit avec messages conventionnels : `feat(recettes): ajout [Titre]`

### Pour Humains

1. **Codespaces** : Cliquer **Code** → **Codespaces** → **Create**
2. Suivre [Quick Start](.devcontainer/QUICKSTART.md)
3. Utiliser alias bash : `help-projet`

---

## 📋 ADN Projet

**Invariants** :
- ✅ **Frugalité** : Infrastructure minimale efficace
- ✅ **Émergence** : Évolution organique guidée
- ✅ **Lisibilité** : Documentation claire, workflow transparent
- ✅ **Traçabilité** : Historique complet, validation automatique

**Gouvernance** : Distribuée (IAs autonomes, coordination workflow)

📚 [PROJECT_DNA.yml](PROJECT_DNA.yml)

---

## 🔗 Liens Utiles

- **Dépôt** : https://github.com/stefm78/livre01-science-culinaire
- **Issues** : https://github.com/stefm78/livre01-science-culinaire/issues
- **Codespaces** : https://github.com/codespaces

---

**Créé le** : Nov 2025  
**Maintenu par** : Chef de Projet IA  
**Licence** : Privé
