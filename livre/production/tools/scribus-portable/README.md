# Scribus Portable - Installation

⚠️ **Ce dossier est EXCLU de Git** (voir `.gitignore` racine)

## 📥 Installation

### 1. Télécharger

**Lien** : https://portableapps.com/apps/office/scribus_portable

**Version recommandée** : Scribus Portable 1.6.4

**Fichier** : `ScribusPortable_1.6.4_Multilingual.paf.exe` (132 MB)

### 2. Installer

1. **Exécuter** le fichier `.paf.exe` téléchargé
2. **Choisir destination** : Ce dossier (`livre/production/tools/scribus-portable/`)
3. **Attendre** fin installation (~500 MB extraits)
4. **Vérifier** présence de `ScribusPortable.exe` ici

### 3. Lancer

**Windows** :
```bash
ScribusPortable.exe
```

**Ou double-clic** sur `ScribusPortable.exe`

---

## 📂 Structure Après Installation

```
scribus-portable/
├── ScribusPortable.exe    # Lanceur principal
├── help.html              # Aide
├── App/                   # Application (~400 MB)
├── Data/                  # Données utilisateur
└── Other/                 # Documentation
```

**Taille totale** : ~500 MB

---

## 🚫 Git Ignore

**Git NE versionne PAS** :
- ❌ Application (`App/`)
- ❌ Données locales (`Data/`)
- ❌ Exécutables (`*.exe`)
- ❌ Configs (`*.ini`)

**Git versionne SEULEMENT** :
- ✅ Ce README
- ✅ Documentation projet

**Raison** : Application trop lourde (500 MB), chaque contributeur l'installe localement.

---

## 🔧 Configuration Première Utilisation

Voir guide complet : `livre/production/tools/README.md`

**Essentiel** :
1. **Unités** : Millimètres
2. **Polices** : Ajouter chemin `../../fonts/`
3. **Guides** : Magnétisme 5px
4. **Couleurs** : Importer palette projet

---

## 📖 Documentation Complète

**Guide complet** : [`livre/production/tools/README.md`](../README.md)

**Contient** :
- Configuration détaillée
- Scripts IA disponibles
- Workflow collaboratif
- Dépannage

---

## ✅ Vérification Installation

```bash
# Vérifier présence exécutable
dir ScribusPortable.exe

# Lancer Scribus
.\ScribusPortable.exe

# Vérifier Git ignore bien tout
cd ..\..\..\..  # Retour racine projet
git status livre/production/tools/scribus-portable/
# Résultat attendu : nothing to commit
```

---

**Créé le** : 2025-12-04  
**Projet** : livre01-science-culinaire  
**Maintenu par** : stefm78
