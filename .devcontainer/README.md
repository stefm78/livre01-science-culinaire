# 🚀 GitHub Codespaces - Environnement de Développement

## 🎯 Objectif

Configuration Codespaces prête à l'emploi pour le projet **Livre Science Culinaire**.

---

## 🛠️ Fonctionnalités

### Environnement Pré-configuré

✅ **Python 3.11** avec dépendances projet  
✅ **Git** configuré avec vos identifiants  
✅ **GitHub CLI** (gh) installé  
✅ **Extensions VS Code** optimisées :  
- Python + Pylance
- Markdown All in One
- GitHub Preview Styles
- Correcteur orthographique (FR/EN)
- Prettier (formatage auto)
- GitHub Pull Requests

### Alias Bash Pratiques

**Navigation rapide** :
- `src` : Aller dans sources/
- `rec` : Aller dans recettes/
- `img` : Aller dans images/tests/
- `scr` : Aller dans scripts/

**Workflow recettes** :
- `nouvelle-recette <nom>` : Créer nouvelle recette depuis templates
- `validate <dossier>` : Valider une recette
- `validate-all` : Valider toutes les recettes
- `genindex` : Générer index automatique

**Git shortcuts** :
- `gs` : git status
- `ga` : git add
- `gc '<msg>'` : git commit -m
- `gp` : git push origin main
- `gl` : git log (10 derniers)
- `gd` : git diff

**Projet** :
- `stats` : Statistiques projet (recettes, images, schémas)
- `help-projet` : Afficher aide complète

---

## 🚀 Lancer Codespaces

### Première Utilisation

1. Aller sur https://github.com/stefm78/livre01-science-culinaire
2. Cliquer **Code** (bouton vert)
3. Onglet **Codespaces**
4. Cliquer **Create codespace on main**
5. Attendre ~30 secondes (initialisation)

➡️ Codespace prêt avec tous les outils !

### Utilisations Suivantes

1. Aller sur https://github.com/codespaces
2. Choisir le Codespace existant
3. Cliquer **Open** (instantané)

---

## 📝 Cas d'Usage Typiques

### 1. Déplacer les Photos 01-07 (Maintenant)

```bash
# Dans le terminal Codespaces
cd /workspaces/livre01-science-culinaire

# Déplacer les 7 photos
git mv sources/images/test-photo-0{1..7}.png images/tests/

# Commit et push
gc "fix(images): déplacement photos tests 01-07 vers images/tests/"
gp

# Vérifier
ls -l images/tests/test-photo-*.png | wc -l
# Attendu : 15
```

**Temps** : 30 secondes ⚡

---

### 2. Créer une Nouvelle Recette

```bash
# Créer structure depuis template
nouvelle-recette risotto-parmesan

# Éditer les fichiers
code recettes/risotto-parmesan/recette.md
code recettes/risotto-parmesan/metadata.json

# Générer images (via ChatGPT, puis uploader)
# ...

# Valider
validate recettes/risotto-parmesan

# Commit
ga recettes/risotto-parmesan
gc "feat(recettes): ajout Risotto Parmesan - Chapitre 1"
gp

# Mettre à jour index
genindex
```

---

### 3. Valider Toutes les Recettes

```bash
# Validation complète + génération index
validate-all

# Voir statistiques
stats
```

---

### 4. Modifier un Template

```bash
# Éditer template
code recettes/_template/recette.md

# Commiter
ga recettes/_template/
gc "feat(templates): ajout section [nouvelle section]"
gp
```

---

## 📊 Spécifications Techniques

### Image Docker
- **Base** : `mcr.microsoft.com/devcontainers/python:3.11`
- **OS** : Debian Linux
- **Python** : 3.11
- **Node.js** : Inclus

### Dépendances Python
- `requests` : API calls
- `pillow` : Traitement images (si nécessaire)

### Extensions VS Code
- Python (IntelliSense, debugging)
- Markdown (prévisualisation, édition)
- Spell Checker (FR + EN)
- GitHub integration

### Configuration Git
- User : stefm78
- Email : smagnand@gmail.com
- Auth : Via GitHub (automatique)

---

## 🔍 Troubleshooting

### Codespace ne Démarre Pas

**Problème** : Erreur au lancement

**Solutions** :
1. Vérifier quota Codespaces (https://github.com/settings/billing)
2. Supprimer ancien Codespace et recréer
3. Vérifier `.devcontainer/devcontainer.json` valide

### Alias Non Disponibles

**Problème** : Commandes `nouvelle-recette`, `stats` non reconnues

**Solutions** :
1. Redémarrer terminal : `Ctrl+D` puis nouveau terminal
2. Charger manuellement : `source ~/.bash_aliases`
3. Vérifier `.devcontainer/bash_aliases` existe

### Scripts Python Ne Fonctionnent Pas

**Problème** : Erreurs d'exécution scripts

**Solutions** :
1. Vérifier dépendances : `pip list`
2. Réinstaller : `pip install requests pillow`
3. Permissions : `chmod +x scripts/*.py`

---

## ⚡ Optimisations

### Pré-build (Optionnel)

Pour démarrage instantané, configurer pre-build :

1. Aller dans **Settings** → **Codespaces**
2. Activer **Prebuild**
3. Configuration : Branch `main`, région `Europe West`

➡️ Codespace démarre en ~5 secondes au lieu de 30

### Rétentions

**Par défaut** : Codespace conservé 30 jours d'inactivité

**Personnaliser** : GitHub Settings → Codespaces → Retention

---

## 💰 Coûts

### Plan Gratuit GitHub

- **60 heures/mois** : Codespaces 2-core
- **15 GB stockage**
- **Suffit largement** pour ce projet

### Estimation Usage Projet

- **Migration photos** : ~1 minute
- **Création recette** : ~30 minutes par recette
- **Validation batch** : ~5 minutes
- **Total projet (30 recettes)** : ~20 heures

➡️ **Bien en dessous** de la limite gratuite !

---

## 🔗 Liens Utiles

- **Documentation Codespaces** : https://docs.github.com/codespaces
- **Vos Codespaces** : https://github.com/codespaces
- **Quota/Usage** : https://github.com/settings/billing

---

**Version** : 1.0  
**Date** : 2025-11-10  
**Maintenu par** : Chef de Projet IA
