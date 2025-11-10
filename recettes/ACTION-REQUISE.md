# 🚨 ACTION REQUISE - Photos 01-07 Mal Placées

## ⚠️ Problème Détecté

Les photos **test-photo-01.png à 07.png** sont dans le **mauvais dossier** :

- ❌ Actuellement : `sources/images/`
- ✅ Destination : `images/tests/`

**Impact** : Bloque finalisation issue #7

---

## ⚡ Solution Rapide (30 secondes)

### Via Codespaces (Recommandé)

1. **Ouvrir Codespaces** :
   - Aller sur https://github.com/stefm78/livre01-science-culinaire
   - Cliquer **Code** → **Codespaces** → **Create codespace on main**

2. **Ouvrir terminal** (`` Ctrl+` ``)

3. **Copier-coller ces commandes** :

```bash
# Déplacer les 7 photos
git mv sources/images/test-photo-0{1..7}.png images/tests/

# Commit
git commit -m "fix(images): déplacement photos tests 01-07 vers images/tests/"

# Push
git push origin main

# Vérifier (doit afficher 15)
ls -1 images/tests/test-photo-*.png | wc -l
```

4. ✅ **Terminé !**

---

## 📚 Documentation Codespaces

Guide complet : [.devcontainer/QUICKSTART.md](../.devcontainer/QUICKSTART.md)

---

## ✅ Après Correction

1. Supprimer ce fichier :
   ```bash
   git rm recettes/ACTION-REQUISE.md
   git commit -m "docs: suppression ACTION-REQUISE après correction photos"
   git push
   ```

2. Finaliser issue #7 avec commentaire de clôture

3. Démarrer issue #8 (schémas scientifiques)

---

**Urgence** : 🔴 HAUTE  
**Temps estimé** : 30 secondes  
**Créé le** : 2025-11-10 18:36 CET
