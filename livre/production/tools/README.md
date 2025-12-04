# Outils PAO - Scribus Portable

## 📥 Installation Scribus Portable

### Téléchargement

**Version recommandée** : Scribus Portable 1.6.4  
**Lien** : https://portableapps.com/apps/office/scribus_portable  
**Taille** : 132 MB

### Installation Pas à Pas

1. **Télécharger** `ScribusPortable_1.6.4_Multilingual.paf.exe`

2. **Exécuter** l'installeur

3. **Choisir destination** : 
   ```
   C:\Users\[vous]\Documents\livre01-science-culinaire\livre\production\tools\scribus-portable\
   ```
   OU le chemin où vous avez cloné le repo

4. **Attendre** fin installation (~500 MB)

5. **Lancer** : `scribus-portable\ScribusPortable.exe`

### Premier Lancement - Configuration

**Ouvrir Préférences** : Fichier → Préférences

#### 1. Unités de mesure
```
Général → Unités :
- Document : Millimètres
- Écran : Millimètres
```

#### 2. Polices
```
Polices → Chemins supplémentaires :
Ajouter : ..\..\fonts\
(Chemin relatif vers livre/production/fonts/)
```

#### 3. Guides et Grilles
```
Guides :
☑ Magnétisme des guides : 5 px
☑ Magnétisme de la grille : 2 mm

Grille :
☑ Afficher la grille : Oui
Espacement : 5 mm
```

#### 4. Couleurs (Palette projet)
```
Couleurs à ajouter :
- #2C3E50 (Texte principal)
- #34495E (Titres)
- #7F8C8D (Sous-titres)
- #3498DB (Accents bleu)
- #95A5A6 (Citations)
```

---

## 📁 Fichier Principal PAO

**Emplacement** : `livre/production/exports/livre-mvp.sla`

**Ouvrir** :
```bash
cd livre/production/tools/scribus-portable
ScribusPortable.exe ..\..\exports\livre-mvp.sla
```

Ou double-clic sur `livre-mvp.sla` (associer à Scribus au premier lancement)

---

## 🤖 Scripts IA Disponibles

Les IA peuvent manipuler le fichier `.sla` (format XML) via scripts Python.

### 1. Analyser Qualité PAO
```bash
python livre/scripts/pao-analyze.py
```

**Vérifie** :
- ✅ Marges conformes (15mm)
- ✅ Fonds perdus (3mm)
- ✅ Résolution images (300dpi minimum)
- ✅ Débordements texte
- ✅ Informations document

**Sortie exemple** :
```
============================================================
📊 RAPPORT QUALITÉ PAO - Scribus
============================================================
📁 Fichier : livre-mvp.sla

📄 Informations document...
  📏 Format : 210.0 x 297.0 mm
  📖 Pages : 120
  📝 Titre : Livre Science Culinaire MVP

🔍 Vérification marges...
  ✅ Toutes les marges conformes (15mm) sur 120 pages

🔍 Vérification fonds perdus...
  ✅ Fonds perdus conformes (3mm)

============================================================
✅ Aucun problème majeur détecté
============================================================
```

### 2. Ajuster Automatiquement
```bash
python livre/scripts/pao-auto-adjust.py
```

**Ajuste** :
- 🔧 Marges uniformes 15mm sur toutes pages
- 🔧 Fonds perdus 3mm
- 💾 Crée backup automatique avant modification
- 📝 Génère message commit

**Sortie exemple** :
```
🤖 Ajustements automatiques Scribus PAO
============================================================
📁 Fichier : livre-mvp.sla
💾 Backup créé : livre-mvp.sla.20251204_223000.bak

🔧 Ajustement marges à 15mm...
  ✅ 120 pages modifiées

🔧 Configuration fonds perdus 3mm...
  ✅ Fonds perdus ajustés

💾 Fichier sauvegardé : livre-mvp.sla

============================================================
✅ Ajustements terminés
📝 2 modifications effectuées

📝 Message commit suggéré :
------------------------------------------------------------
fix(PAO): ajustements automatiques

- Marges ajustées sur 120 pages
- Fonds perdus configurés : 3mm
------------------------------------------------------------

🔙 Backup disponible : livre-mvp.sla.20251204_223000.bak
   Pour restaurer : copier le .bak vers .sla
```

### 3. Extraire Contenu Markdown
```bash
python livre/scripts/sla-import-content.py recettes/steak-maillard/recette.md
```

**Extrait** sections recette pour import manuel dans Scribus :
- 🎯 Titre
- 🔬 Section Science
- 📝 Ingrédients
- 👨‍🍳 Étapes préparation
- 🌟 Variantes

**Utilisation** :
1. Exécuter script
2. Copier sections affichées
3. Coller dans cadres texte Scribus
4. Appliquer styles appropriés

---

## 🔄 Workflow Collaboratif Humain ↔ IA

### Matin - VOUS (Humain)

```bash
# 1. Synchroniser
cd livre01-science-culinaire
git pull origin main

# 2. Lancer Scribus
livre\production\tools\scribus-portable\ScribusPortable.exe

# 3. Ouvrir fichier PAO
# Fichier → Ouvrir : livre/production/exports/livre-mvp.sla

# 4. Travailler sur mise en page
# ... création pages 10-15 ...

# 5. Sauvegarder (Ctrl+S)

# 6. Commit changements
git add livre/production/exports/livre-mvp.sla
git commit -m "feat(PAO): mise en page pages 10-15"
git push origin main
```

### Soir - IA (Scripts Automatiques)

```bash
# 1. Synchroniser
git pull origin main

# 2. Analyser qualité
python livre/scripts/pao-analyze.py

# 3. Si problèmes détectés : ajuster
python livre/scripts/pao-auto-adjust.py

# 4. Commit corrections
git add livre/production/exports/livre-mvp.sla
git commit -m "fix(PAO): ajustements marges pages 10-15"
git push origin main

# 5. Notifier via GitHub Issue
gh issue comment 55 --body "✅ QA automatique pages 10-15 : OK"
```

### Validation - VOUS (Matin suivant)

```bash
# 1. Pull corrections IA
git pull origin main

# 2. Ouvrir Scribus
ScribusPortable.exe

# 3. Vérifier pages modifiées par IA
# - Marges OK ? ✅
# - Texte intact ? ✅
# - Qualité visuelle ? ✅

# 4. Si OK : continuer votre travail
# Si KO : ajuster manuellement + commit
```

---

## ⚠️ Important : Fichiers Git

### ✅ Versionnés dans Git

- Fichiers `.sla` (PAO)
- Scripts Python
- Documentation (README, guides)
- Configuration VSCode
- Polices projet
- Images optimisées

### ❌ NON versionnés

- Application Scribus Portable (~500 MB)
- Fichiers temporaires (`.sla~`, `.sla.bak`)
- Cache Python (`__pycache__`)
- Fichiers système (`.DS_Store`, `Thumbs.db`)

**Raison** : Le `.gitignore` filtre automatiquement ces fichiers.

---

## 💾 Sauvegarde et Sécurité

### Backups Automatiques

Les scripts IA créent **automatiquement** des backups avant toute modification :

```
livre/production/exports/
├── livre-mvp.sla                    # Fichier actuel
├── livre-mvp.sla.20251204_220000.bak  # Backup 22h00
├── livre-mvp.sla.20251204_223000.bak  # Backup 22h30
└── livre-mvp.sla.20251205_080000.bak  # Backup 08h00
```

### Restaurer un Backup

```bash
# 1. Identifier backup à restaurer
dir livre\production\exports\*.bak

# 2. Copier backup vers fichier principal
copy livre-mvp.sla.20251204_220000.bak livre-mvp.sla

# 3. Ouvrir dans Scribus
ScribusPortable.exe livre-mvp.sla
```

### Git comme Backup Ultime

Git conserve **tout l'historique** des modifications :

```bash
# Voir historique fichier
git log --oneline livre/production/exports/livre-mvp.sla

# Restaurer version précédente
git checkout HEAD~1 livre/production/exports/livre-mvp.sla

# Ou version spécifique
git checkout abc1234 livre/production/exports/livre-mvp.sla
```

---

## 📚 Ressources Scribus

- **Documentation officielle** : https://wiki.scribus.net/
- **Tutoriels** : https://www.scribus.net/tutorials/
- **Forum** : https://forums.scribus.net/
- **Manuel PDF** : https://wiki.scribus.net/canvas/Official_Scribus_Manual

---

## ❓ Dépannage

### Scribus ne démarre pas

1. Vérifier installation complète dans `scribus-portable/`
2. Vérifier présence `ScribusPortable.exe`
3. Réinstaller si nécessaire

### Fichier .sla corrompu

Le `.sla` est du **XML** → réparable manuellement :

```bash
# 1. Ouvrir avec éditeur texte (VSCode)
code livre/production/exports/livre-mvp.sla

# 2. Vérifier structure XML valide
# 3. Corriger balises fermées
# 4. Sauvegarder

# Ou restaurer backup
copy livre-mvp.sla.*.bak livre-mvp.sla
```

### Scripts Python échouent

```bash
# Vérifier Python installé
python --version
# Doit afficher : Python 3.8+

# Vérifier emplacement fichier
dir livre\production\exports\livre-mvp.sla

# Exécuter avec chemin explicite
python livre/scripts/pao-analyze.py livre/production/exports/livre-mvp.sla
```

---

**Créé le** : 2025-12-04  
**Version** : 1.0  
**Maintenu par** : IA + stefm78  
**Projet** : livre01-science-culinaire
