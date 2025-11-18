# 🤖 Guide des Workflows GitHub Actions

## Vue d'ensemble

Ce repository utilise plusieurs workflows GitHub Actions pour automatiser la gestion des images et des index. Chaque workflow est numéroté et peut être déclenché manuellement via l'interface GitHub.

## 📌 Accès rapide

**Déclencher manuellement un workflow** :
1. Aller sur [Actions](https://github.com/stefm78/livre01-science-culinaire/actions)
2. Choisir le workflow dans la liste de gauche
3. Cliquer sur "Run workflow" à droite
4. Sélectionner la branche (généralement `main`)
5. Cliquer sur "Run workflow"

---

## 🎨 Workflows Images

### 01-Images 🎨 Commit depuis Cloud

**Fichier** : `.github/workflows/commit-images.yml`

**Fonction** : Télécharge des images depuis un cloud externe et les committe dans `sources/images/`

**Déclenchement** :
- ⚙️ Manuel via bouton "Run workflow"
- 🔄 Automatique sur push de `tools/images-to-commit.json`

**Ce qu'il fait** :
1. Lit le fichier `tools/images-to-commit.json` contenant les URLs des images
2. Télécharge chaque image depuis le cloud
3. Sauvegarde dans `sources/images/`
4. Committe avec message indiquant le nombre d'images
5. Commente l'issue associée avec un récapitulatif

**Usage typique** : Après génération d'images IA stockées temporairement sur cloud, ce workflow les intègre définitivement au repo Git.

---

### 02-Images 📦 Import Batch IA

**Fichier** : `.github/workflows/import-images.yml`

**Fonction** : Importe des images depuis `_inbox/images/` (ZIP ou JSON) vers les dossiers recettes correspondants

**Déclenchement** :
- ⚙️ Manuel via bouton "Run workflow"
- 🔄 Automatique sur push de fichiers `*.json` ou `*.zip` dans `_inbox/images/`

**Ce qu'il fait** :
1. Extrait les archives ZIP si présentes dans `_inbox/images/`
2. Exécute `import_batch_images.py` qui :
   - Lit les fichiers JSON de métadonnées
   - Déplace les images vers `recettes/[nom-recette]/images/`
   - Renomme selon conventions (hero.png, final.png, etc.)
3. Committe les changements

**Usage typique** : Après génération d'un batch d'images IA, déposer le ZIP + JSON dans `_inbox/images/` et laisser le workflow dispatcher automatiquement.

---

### 03-Images 🔍 Scan Backlog Auto

**Fichier** : `.github/workflows/scan-images-backlog-direct.yml`

**Fonction** : Scanne toutes les recettes pour détecter les images manquantes et génère un rapport

**Déclenchement** :
- ⚙️ Manuel via bouton "Run workflow"
- ⏰ Automatique tous les **lundis à 9h** (schedule cron)

**Ce qu'il fait** :
1. Exécute `scripts/scan-images-backlog.py`
2. Génère 2 rapports :
   - `_inbox/images/backlog-scan.json` (format machine)
   - `_inbox/images/BACKLOG-REPORT.md` (format humain)
3. Committe les rapports
4. Poste un commentaire sur l'issue #25 avec le rapport

**Usage typique** : Vérifier régulièrement quelles images sont manquantes pour planifier la production IA.

**Rapport généré** : Indique pour chaque recette :
- ✅ Images présentes (hero, final, process)
- ❌ Images manquantes
- 📏 Récapitulatif global (% complétion, priorités)

---

### 04-Images 💬 Scan Backlog Commande

**Fichier** : `.github/workflows/scan-images-backlog.yml`

**Fonction** : Identique à 03-Images mais déclenché par commande dans une issue

**Déclenchement** :
- 💬 Commande `/scan-images` dans un commentaire d'issue

**Ce qu'il fait** :
1. Détecte la commande `/scan-images` dans un commentaire
2. Ajoute une réaction 🚀 au commentaire ("en cours")
3. Exécute le scan backlog
4. Poste les résultats **directement dans l'issue courante**
5. Ajoute réaction 🎉 (succès) ou 😕 (échec)
6. Committe les rapports

**Usage typique** : Lors d'une discussion sur une issue, taper `/scan-images` pour obtenir instantanément l'état du backlog images.

**Différence avec 03-Images** :
- 03 = Planifié (hebdomadaire) + bouton manuel
- 04 = À la demande dans une issue spécifique

---

## 📚 Workflow Index

### 05-Index 📚 Mise à jour

**Fichier** : `.github/workflows/update-index.yml`

**Fonction** : Génère `recettes/index.json` et `recettes/INDEX.md` depuis tous les `metadata.json`

**Déclenchement** :
- ⚙️ Manuel via bouton "Run workflow" (avec raison optionnelle)

**Ce qu'il fait** :
1. Exécute `scripts/generate-index.py` qui :
   - Scanne tous les `recettes/*/metadata.json`
   - Agrège les données (titre, chapitre, concept, tags, etc.)
   - Génère `index.json` (format machine)
   - Génère `INDEX.md` (format humain avec tableaux)
2. Détecte si changements (diff Git)
3. Si changements :
   - Affiche le diff
   - Committe avec message incluant la raison fournie
   - Pousse les changements
4. Affiche statistiques (total recettes, chapitres, date)

**Usage typique** : Après ajout/modification de recettes, relancer ce workflow pour synchroniser l'index central.

**Paramètre optionnel** : `reason` - permet de spécifier pourquoi la mise à jour est nécessaire (ex: "Ajout recettes Sprint 5")

---

## 🔄 Workflows Supplémentaires

### Lint Guard

**Fichier** : `.github/workflows/lint-guard.yml`  
**Fonction** : Validation automatique de la qualité du code et des fichiers  
**Déclenchement** : Sur chaque pull request  

### Evolution

**Fichier** : `.github/workflows/evolution.yml`  
**Fonction** : Suivi de l'évolution du projet (métriques, statistiques)  
**Déclenchement** : Manuel ou automatisé  

### Issue Orchestration

**Fichier** : `.github/workflows/issue-orchestration.yml`  
**Fonction** : Gestion automatisée des issues (labels, assignations, etc.)  
**Déclenchement** : Sur création/modification d'issues  

### QA Recipe Dispatch

**Fichier** : `.github/workflows/qa-recipe-dispatch.yml`  
**Fonction** : Validation qualité des recettes  
**Déclenchement** : Manuel ou sur demande  

---

## 🛠️ Utilisation Pratique

### Scénario 1 : Ajouter des images générées par IA

1. Générer images IA (ex: ChatGPT DALL-E 3)
2. Télécharger le ZIP
3. Créer fichier JSON de mapping (voir `_inbox/images/README-GENERATE-BATCH-IMAGES.md`)
4. Déposer ZIP + JSON dans `_inbox/images/`
5. Workflow **02-Images** se déclenche automatiquement
6. Vérifier commit automatique dans Git

### Scénario 2 : Vérifier images manquantes

**Option A - Automatique hebdomadaire** :
- Attendre le lundi 9h
- Consulter issue #25 pour le rapport

**Option B - Manuel immédiat** :
- Aller sur Actions > **03-Images 🔍 Scan Backlog Auto**
- Run workflow
- Consulter issue #25

**Option C - Depuis une issue** :
- Dans n'importe quelle issue, commenter `/scan-images`
- Résultat posté dans l'issue courante

### Scénario 3 : Mettre à jour l'index après nouveaux metadata.json

1. Modifier/ajouter `recettes/*/metadata.json`
2. Aller sur Actions > **05-Index 📚 Mise à jour**
3. Run workflow avec raison (ex: "Mise à jour metadata Sprint 5")
4. Vérifier commit automatique de `index.json` et `INDEX.md`

---

## 🔔 Notifications

Tous les workflows :
- ✅ Affichent des logs détaillés avec emojis pour lisibilité
- 💬 Commentent les issues concernées (sauf 05-Index)
- 🎯 Génèrent des commits avec messages conventionnels
- ⚠️ Signalent les erreurs via reactions/comments

---

## 📚 Références

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Guide Images Batch](./_inbox/images/README-GENERATE-BATCH-IMAGES.md)

---

**Dernière mise à jour** : 18 novembre 2025  
**Mainteneur** : Chef Projet IA
