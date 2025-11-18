# 🍳 Livre Science Culinaire - Production Collaborative IA

**Projet** : Livre de cuisine scientifique (31 recettes, 8 chapitres, 200-250 pages)  
**Statut** : 🟢 Phase Production Contenu (26% complète)  
**Infrastructure** : ✅ Opérationnelle (Nov 2025)

---

> ## 🤖 **IA SANS CONTEXTE ?**
> ### → **[START_HERE.md](START_HERE.md)** ← **LIS ÇA D'ABORD (2 min)**
> Tu sauras exactement quoi faire.

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
- 👨‍🍳 Recettes pratiques (31 fiches, 8 chapitres)
- 📸 Photographies IA (style minimaliste scientifique)
- 📈 Schémas pédagogiques (8 concepts clés)

### Cible

**200-250 pages** | **31 recettes** | **8 chapitres** | **60+ images**

---

## 🗺️ Roadmap & Planning

### Phase Actuelle : Production Contenu (🟢 26%)

**Dates** : 18 nov 2025 - 17 jan 2026 (8 semaines)

| Sprint | Chapitre | Recettes | Dates | Statut |
|--------|----------|----------|-------|--------|
| Sprint 1 | Ch.1 Bases | 5 | 18-22 Nov | Issue #13 ✅ |
| Sprint 2 | Ch.2 Viandes | 4 | 25-29 Nov | ✅ |
| Sprint 3 | Ch.3 Poissons | 4 | 2-6 Dec | ✅ TERMINÉ |
| Sprint 4 | Ch.4 Légumes | 4 | 9-13 Dec | ⏳ |
| **Sprint 5** | **Ch.5 Œufs** | **4** | **16-20 Dec** | **🟢 EN COURS** |
| Sprint 6 | Ch.6 Pains | 3 | 23-27 Dec | ⏳ |
| Sprint 7 | Ch.7 Desserts | 4 | 6-10 Jan | ⏳ |
| Sprint 8 | Ch.8 Créations | 3 | 13-17 Jan | ⏳ |

🗺️ **[ROADMAP Complète](ROADMAP.md)** : Phases 1-4 détaillées  
📋 **[RECETTES_LISTE.md](RECETTES_LISTE.md)** : 31 recettes définies

### État d'Avancement Global

| Composant | Statut | Progression |
|-----------|--------|-------------|
| **Infrastructure** | ✅ Complète | 100% |
| **Codespaces** | ✅ Configuré | 100% |
| **Templates** | ✅ Prêts | 100% |
| **Templates Prompts IA** | ✅ Créés | 100% |
| **Schémas Scientifiques** | ✅ Créés | 100% (8/8) |
| **Liste Recettes** | ✅ Définie | 100% (31/31) |
| **Recettes** | 🟢 En cours | 26% (8/31) |
| **Images** | 🟢 En cours | 30% (18/60+) |

### Dernières Recettes Produites (Sprint 5 - 18 nov 2025)

**Chapitre 5 - Œufs & Laitages** :
- ✅ 5.1 - Œuf Mollet Parfait (6 min 30) - Coagulation protéines
- ✅ 5.2 - Mousse au Chocolat Aérienne - Foisonnement protéines  
- ✅ 5.3 - Panna Cotta Gélification - Gélatine
- ✅ 5.4 - Crème Brûlée Caramélisée - Coagulation + Caramélisation

**Sources scientifiques** : 13 références (INRA, Agriculture Institute, PMC, Je Pense donc Je Cuis, Joel Robuchon, etc.)

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

## 🏭 Architecture Projet

```
livre01-science-culinaire/
├── sources/                   # Documentation cadrage
│   ├── cadrage-editorial.md    # Structure 8 chapitres
│   ├── charte-visuelle.md      # Style photographique
│   ├── base-documentaire.md    # Sources scientifiques
│   ├── images/                 # Maquettes visuelles
│   ├── schemas/                # Schémas scientifiques (8) ✅
│   └── templates/              # Templates prompts IA ✅
│
├── recettes/                  # ⭐ Production 31 fiches
│   ├── _template/             # Templates standardisés
│   └── [nom-recette]/        # Architecture self-contained
│       ├── recette.md
│       ├── metadata.json
│       └── images/
│
├── images/tests/             # Photos validation charte
├── scripts/                  # Outils automatisation
├── ROADMAP.md                # Planning 4 phases
├── RECETTES_LISTE.md         # 31 recettes définies ✅
├── PERSONAS_IA.md            # Équipe IA
├── START_HERE.md             # 🚀 Point d'entrée IA
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
- 📋 [RECETTES_LISTE.md](RECETTES_LISTE.md) : 31 recettes définies ✅
- 👥 [PERSONAS_IA.md](PERSONAS_IA.md) : Équipe IA spécialisée
- 🏭 [INFRASTRUCTURE.md](INFRASTRUCTURE.md) : Architecture technique
- 🧬 [PROJECT_DNA.yml](PROJECT_DNA.yml) : ADN projet

### Pour Démarrer
- 🚀 **[START_HERE.md](START_HERE.md)** : IA sans contexte ← **POINT D'ENTRÉE**
- ⚡ [Quick Start Codespaces](.devcontainer/QUICKSTART.md)
- 📚 [Workflow Recettes](recettes/README.md)

### Cadrage Projet
- 📝 [Cadrage Éditorial](sources/cadrage-editorial.md)
- 🎨 [Charte Visuelle](sources/charte-visuelle.md)
- 📖 [Base Documentaire](sources/base-documentaire.md)
- 📈 [Schémas Scientifiques](sources/schemas/README.md) ✅

### Templates

#### Templates Recettes
- 📝 [Template Recette](recettes/_template/recette.md)
- 🗂️ [Template Métadonnées](recettes/_template/metadata.json)

#### Templates Prompts IA ⭐
- 🤖 [Template Prompt IA](sources/templates/TEMPLATE_PROMPT_IA.md) : Framework modulaire délégation tâches
- 📚 [Guide Utilisation Templates](sources/templates/README.md) : Documentation complète

**Usage** : Générer des prompts structurés pour IAs spécialisées (Rédacteur, Designer, Reviewer, Researcher)

---

## 📊 Progression Projet

### Métriques Clés

- **Recettes définies** : 31/31 (100%) ✅
- **Recettes produites** : 8/31 (26%)
- **Images** : 18/60+ (30%)
- **Schémas** : 8/8 (100%) ✅
- **Pages Livre** : 0/200-250 (0%)
- **Sources** : 60+/50+ (120%) ✅
- **Templates IA** : 1/1 (100%) ✅

### Jalons Critiques

| Date | Jalon | Statut |
|------|-------|--------|
| 10 Nov 2025 | Schémas + Liste Recettes | ✅ Complété |
| 18 Nov 2025 | Template Prompt IA + Sprint 3 + Sprint 5 Démarré | ✅ Complété |
| 20 Nov 2025 | Sprint 5 Images IA | 🟢 En cours |
| 22 Nov 2025 | Sprint 5 Validation Complète | ⏳ Planifié |
| 13 Dec 2025 | Sprint 4 Complet | ⏳ Planifié |
| 17 Jan 2026 | 31 Recettes Produites | ⏳ Planifié |
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

- **#19** : 🟢 SPRINT 5 - Chapitre 5 Œufs & Laitages (EN COURS - Rédaction terminée 18 nov)
- **#16** : ✅ SPRINT 3 - Chapitre 3 Poissons & Fruits de Mer (TERMINÉ - 18 nov 2025)
- **#23** : ✅ Template Prompt IA (TERMINÉE - 18 nov 2025)
- **#11** : 🟡 PHASE 1 - Finalisation Fondations (Sem 46) - 40% complété
- **#13** : 🟠 SPRINT 1 - Chapitre 1 (Sem 47) - Prêt à démarrer
- **#8** : ✅ Schémas Scientifiques (FERMÉE - 8/8 mergés)
- **#12** : ✅ Liste 30 Recettes (FERMÉE - 31 recettes définies)

### Labels
- `phase-1`, `production`, `sprint` : Organisation
- `critique`, `haute`, `moyenne` : Priorité
- `recettes`, `documentation`, `infrastructure` : Type
- `persona:nom` : Attribution IA

---

## 👋 Contribution

### Pour IAs

**Nouvelle IA ?** → [**START_HERE.md**](START_HERE.md) (2 min)

**Ensuite** :
1. Consulter [PERSONAS_IA.md](PERSONAS_IA.md) pour rôle assigné
2. Suivre [ROADMAP.md](ROADMAP.md) pour planning
3. Utiliser templates dans `recettes/_template/`
4. Consulter [Template Prompt IA](sources/templates/TEMPLATE_PROMPT_IA.md) pour délégation tâches
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
- **Recettes** : [RECETTES_LISTE.md](RECETTES_LISTE.md)
- **Codespaces** : https://github.com/codespaces

---

**Créé le** : Nov 2025  
**Maintenu par** : Chef de Projet IA  
**Phase** : Production Contenu (26%)  
**Licence** : Privé

**Dernière mise à jour** : 18 novembre 2025 (Sprint 5 - 4 recettes Chapitre 5 produites)