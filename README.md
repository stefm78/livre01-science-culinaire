# 🍳 Livre Science Culinaire - Production Collaborative IA

**Projet** : Livre de cuisine scientifique (30 recettes, 8 chapitres, 200-250 pages)  
**Statut** : 🟠 Phase Production-Contenu  
**Infrastructure** : ✅ Opérationnelle (Nov 2025)

> **🤖 Nouvelle IA ?** Lire d'abord **[ONBOARDING_IA.md](ONBOARDING_IA.md)** (5 min)

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

## 🗺️ Roadmap & Planning

### Phase Actuelle : Production Contenu (🟠 0%)

**Dates** : 18 nov 2025 - 17 jan 2026 (8 semaines)

| Sprint | Chapitre | Recettes | Dates | Statut |
|--------|----------|----------|-------|--------|
| Sprint 1 | Ch.1 Bases | 5-6 | 18-22 Nov | Issue #13 |
| Sprint 2 | Ch.2 Viandes | 4-5 | 25-29 Nov | ⏳ |
| Sprint 3 | Ch.3 Poissons | 3-4 | 2-6 Dec | ⏳ |
| Sprint 4 | Ch.4 Légumes | 4-5 | 9-13 Dec | ⏳ |
| Sprint 5 | Ch.5 Œufs | 3-4 | 16-20 Dec | ⏳ |
| Sprint 6 | Ch.6 Pains | 3-4 | 23-27 Dec | ⏳ |
| Sprint 7 | Ch.7 Desserts | 4-5 | 6-10 Jan | ⏳ |
| Sprint 8 | Ch.8 Créations | 3-4 | 13-17 Jan | ⏳ |

🗺️ **[ROADMAP Complète](ROADMAP.md)** : Phases 1-4 détaillées

### État d'Avancement Global

| Composant | Statut | Progression |
|-----------|--------|-------------|
| **Infrastructure** | ✅ Complète | 100% |
| **Codespaces** | ✅ Configuré | 100% |
| **Templates** | ✅ Prêts | 100% |
| **Schémas Scientifiques** | ✅ Créés | 100% (8/8) |
| **Photos Tests** | 🟡 En cours | 47% (7/15) |
| **Recettes** | ⏳ À démarrer | 0% (0/30) |

---

## 👥 Organisation Équipe IA

### Personas Spécialisés

**Chef Projet IA** 🏅
- Coordination globale
- Gestion issues & roadmap
- Intégration Git

**Rédacteur-Scientifique** 📝
- Recherche documentaire
- Rédaction recettes
- Explications scientifiques

**Créatif-Designer** 🎨
- Génération images IA
- Respect charte visuelle
- Schémas scientifiques

**Reviewer-Qualité** ✅
- Validation scientifique
- Contrôle cohérence
- Quality assurance

**Researcher-Veilleur** 🔍
- Enrichissement base documentaire
- Veille scientifique
- Sourcing références

👥 **[PERSONAS_IA.md](PERSONAS_IA.md)** : Rôles et responsabilités détaillés

---

## 🏗️ Architecture Projet

```
livre01-science-culinaire/
├── sources/                   # Documentation cadrage
│   ├── cadrage-editorial.md    # Structure 8 chapitres
│   ├── charte-visuelle.md      # Style photographique
│   ├── base-documentaire.md    # Sources scientifiques
│   ├── images/                 # Maquettes visuelles
│   └── schemas/                # Schémas scientifiques (8)
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
├── ROADMAP.md                # Planning 4 phases
├── PERSONAS_IA.md            # Équipe IA
├── ONBOARDING_IA.md          # Guide démarrage IA
└── .devcontainer/            # Config Codespaces
```

📚 [Documentation Complète](INFRASTRUCTURE.md)

---

## 📝 Workflow Production Recettes

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

📚 [Workflow Détaillé](recettes/README.md)

---

## 🔗 Documentation Principale

### Vue Globale
- 🗺️ [ROADMAP.md](ROADMAP.md) : Planning 4 phases + 8 sprints
- 👥 [PERSONAS_IA.md](PERSONAS_IA.md) : Équipe IA spécialisée
- 🏗️ [INFRASTRUCTURE.md](INFRASTRUCTURE.md) : Architecture technique
- 🧬 [PROJECT_DNA.yml](PROJECT_DNA.yml) : ADN projet

### Pour Démarrer
- 🤖 [ONBOARDING_IA.md](ONBOARDING_IA.md) : Guide IA (5 min)
- ⚡ [Quick Start Codespaces](.devcontainer/QUICKSTART.md)
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

### Métriques Clés

- **Recettes** : 0/30 (0%)
- **Images** : 7/60+ (12%)
- **Schémas** : 8/8 (100%) ✅
- **Pages Livre** : 0/200-250 (0%)
- **Sources** : 20+/40+ (50%)

### Jalons Critiques

| Date | Jalon | Statut |
|------|-------|--------|
| 15 Nov 2025 | Go Production | 🟡 En cours |
| 22 Nov 2025 | Sprint 1 Complet | ⏳ Planifié |
| 17 Jan 2026 | 30 Recettes Produites | ⏳ Planifié |
| 31 Jan 2026 | Livre Final | ⏳ Planifié |

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

### Issues Actives Prioritaires

- **#11** : 🔴 PHASE 1 - Finalisation Fondations (Sem 46)
- **#12** : 🟠 Établir Liste 30 Recettes
- **#13** : 🟠 SPRINT 1 - Chapitre 1 (Sem 47)
- **#6** : 🟡 Enrichissement Base Documentaire (20+ sources)
- **#8** : 🟡 Schémas Scientifiques (8/8 créés, merge requis)

### Labels
- `phase-1`, `production`, `sprint` : Organisation
- `critique`, `haute`, `moyenne` : Priorité
- `recettes`, `documentation`, `infrastructure` : Type
- `persona:nom` : Attribution IA

---

## 👋 Contribution

### Pour IAs

1. Lire [ONBOARDING_IA.md](ONBOARDING_IA.md) (5 min)
2. Consulter [PERSONAS_IA.md](PERSONAS_IA.md) pour rôle assigné
3. Suivre [ROADMAP.md](ROADMAP.md) pour planning
4. Utiliser templates dans `recettes/_template/`
5. Valider via `scripts/validate-recipe.py`
6. Commit avec messages conventionnels : `feat(recettes): ajout [Titre]`

### Pour Humains

1. **Codespaces** : Cliquer **Code** → **Codespaces** → **Create**
2. Suivre [Quick Start](.devcontainer/QUICKSTART.md)
3. Utiliser alias bash : `help-projet`

---

## 📚 ADN Projet

**Invariants** :
- ✅ **Frugalité** : Infrastructure minimale efficace
- ✅ **Émergence** : Évolution organique guidée
- ✅ **Lisibilité** : Documentation claire, workflow transparent
- ✅ **Traçabilité** : Historique complet, validation automatique

**Gouvernance** : Distribuée (IAs autonomes, coordination workflow)

🧬 [PROJECT_DNA.yml](PROJECT_DNA.yml)

---

## 🔗 Liens Utiles

- **Dépôt** : https://github.com/stefm78/livre01-science-culinaire
- **Issues** : https://github.com/stefm78/livre01-science-culinaire/issues
- **Roadmap** : [ROADMAP.md](ROADMAP.md)
- **Codespaces** : https://github.com/codespaces

---

**Créé le** : Nov 2025  
**Maintenu par** : Chef de Projet IA  
**Phase** : Production Contenu  
**Licence** : Privé