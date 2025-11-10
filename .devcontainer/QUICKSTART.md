# ⚡ Quick Start - Correction Photos 01-07 via Codespaces

## 🎯 Mission Immédiate

Déplacer les 7 photos de `sources/images/` vers `images/tests/` en **30 secondes**.

---

## 🚀 Étapes (30 secondes)

### 1. Lancer Codespaces (10 sec)

1. Aller sur https://github.com/stefm78/livre01-science-culinaire
2. Cliquer **Code** (bouton vert)
3. Onglet **Codespaces**
4. Cliquer **Create codespace on main**

⏳ Attendre ~20 secondes (initialisation)

---

### 2. Ouvrir le Terminal (5 sec)

Dans Codespaces :
- Cliquer **Terminal** (menu du haut)
- Ou raccourci : `` Ctrl+` `` (backtick)

---

### 3. Exécuter les Commandes (15 sec)

Copier-coller dans le terminal :

```bash
# Déplacer les 7 photos (préserve l'historique Git)
git mv sources/images/test-photo-0{1..7}.png images/tests/

# Commit
git commit -m "fix(images): déplacement photos tests 01-07 vers images/tests/

- Correction emplacement (étaient dans sources/images/)
- Centralisation 15 photos tests dans images/tests/
- Finalisation issue #7"

# Push
git push origin main
```

---

### 4. Vérifier (5 sec)

```bash
# Compter les photos dans images/tests/
ls -1 images/tests/test-photo-*.png | wc -l
```

**Attendu** : `15`

```bash
# Vérifier que sources/images/ ne contient plus de test-photo
ls -1 sources/images/test-photo-*.png 2>/dev/null | wc -l
```

**Attendu** : `0`

---

## ✅ Résultat

✅ 15 photos tests dans `images/tests/`  
✅ 3 maquettes seulement dans `sources/images/`  
✅ Historique Git préservé  
✅ Issue #7 prête à finaliser  

---

## 🔗 Vérification Web

Après le push, consulter :

- https://github.com/stefm78/livre01-science-culinaire/tree/main/images/tests  
  ➡️ Doit afficher **16 fichiers** (15 PNG + README.md)

- https://github.com/stefm78/livre01-science-culinaire/tree/main/sources/images  
  ➡️ Doit afficher **3 fichiers** (3 maquettes PNG)

---

## 🛠️ Utilisation Future Codespaces

Après cette correction, vous pourrez utiliser Codespaces pour :

- ✅ Créer nouvelles recettes : `nouvelle-recette <nom>`
- ✅ Valider recettes : `validate recettes/<nom>`
- ✅ Générer index : `genindex`
- ✅ Voir stats : `stats`
- ✅ Éditer fichiers avec VS Code complet
- ✅ Tester scripts Python

**Commandes disponibles** : `help-projet`

---

## 💰 Coût

**Gratuit** (Plan GitHub Free) :
- 60 heures/mois
- 15 GB stockage

**Usage estimé ce projet** : ~20 heures total

---

## 💡 Conseils

✅ **Laisser le Codespace ouvert** pendant travail  
✅ **Arrêter après utilisation** (30 min inactivité = arrêt auto)  
✅ **Réutiliser même Codespace** (démarrage instantané)  
❌ **Ne pas créer multiples Codespaces** (consomme quota)  

---

**Créé le** : 2025-11-10  
**Par** : Chef de Projet IA  
**Statut** : ✅ Prêt à l'emploi
