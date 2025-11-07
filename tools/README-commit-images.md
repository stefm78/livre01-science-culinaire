# 🎨 Outil Commit Images - Mode d'Emploi

## 🎯 Objectif

Script Python pour committer automatiquement des images hébergées sur URLs externes dans le repository GitHub, tout en préservant les liens de preuve.

---

## 📝 Fichiers

- **`commit-images.py`** : Script Python exécutable
- **`images-to-commit.json`** : Manifeste des images à committer
- **`images-committed.json`** : Traçabilité (généré automatiquement)

---

## 🚀 Utilisation pour une IA

### Étape 1 : Mise à Jour du Manifeste

Modifiez `tools/images-to-commit.json` avec vos URLs d'images :

```json
{
  "issue_number": 5,
  "persona": "creatif-designer",
  "date": "2025-11-07",
  "images": [
    {
      "filename": "mon-image.png",
      "url": "https://exemple.com/image.png",
      "destination": "sources/images",
      "issue": 5,
      "description": "Description de l'image"
    }
  ]
}
```

### Étape 2 : Exécution du Script

```bash
cd /chemin/vers/repo
python3 tools/commit-images.py
```

### Étape 3 : Commit Git

Le script télécharge les images dans `sources/images/`, puis exécutez :

```bash
git add sources/images/ tools/images-committed.json
git commit -m "🎨 Ajout maquettes visuelles (Issue #5)"
git push
```

---

## ✅ Avantages

✅ **Pas de YAML** → Zéro risque syntaxe  
✅ **URLs préservées** → Traçabilité complète  
✅ **Réutilisable** → Fonctionne pour toutes futures images  
✅ **Exécutable par IA** → Autonomie totale  
✅ **Traçabilité** → SHA commit + JSON traçabilité  

---

## 🔄 Pour Futures Images

Pour toute nouvelle image à committer :

1. Ajoutez l'entrée dans `tools/images-to-commit.json`
2. Exécutez `python3 tools/commit-images.py`
3. Commit et push

**Le script est conçu pour fonctionner tout au long de la vie du projet.**

---

## 📊 Traçabilité

Le fichier `tools/images-committed.json` conserve :
- URLs sources originales
- SHA des commits
- Issues associées
- Dates et personas
- Tailles de fichiers

**Aucun lien de preuve n'est perdu.**

---

**Version** : 1.0  
**Date** : 2025-11-07  
**Mainteneur** : Chef de Projet IA
