# 🤖 Instructions pour les 4 IA du Projet

## 🎯 Mission Globale

Vous êtes l'une des 4 IA travaillant sur le projet **livre01-science-culinaire**. Ce fichier contient les instructions EXPLICITES pour vous coordonner avec les autres IA.

---

## 📋 Procédure de Connexion et Prise en Charge

### 1️⃣ Identifier Votre Persona

**Lisez `AI_CORE.yml` et `constitution-projet-ai.md`** pour comprendre votre rôle.

Personas disponibles:
- **chef-de-projet** (IA #1)
- **researcher-veilleur** (IA #2)
- **creatif-designer** (IA #3)
- **communicant-redacteur** (IA #4)

### 2️⃣ Trouver Votre Issue

**Commande GitHub CLI:**
```bash
gh issue list --label "ia-available" --label "persona:VOTRE_PERSONA"
```

**Via Interface Web:**
- Allez sur l'onglet "Issues"
- Filtrez par labels: `ia-available` + `persona:votre-persona`

### 3️⃣ Poser le Verrou (MANUEL)

**⚠️ CRITICAL: Système de verrous NON automatisé**

Avant de commencer, **VOUS DEVEZ** :

1. **Commenter l'issue** :
```markdown
🔒 **Verrou IA Posé**
- Persona: [VOTRE_PERSONA]
- Identifiant IA: [VOTRE_NOM/ID]
- Heure début: [TIMESTAMP]
- Timeout: 30 minutes
```

2. **Demander l'ajout du label `ia-locked`** (vous ou l'initiateur)

3. **Retirer le label `ia-available`** (vous ou l'initiateur)

### 4️⃣ Travailler Sur Votre Issue

**Respectez strictement:**
- ✅ **Checklist** de l'issue (3 items max)
- ✅ **Définition de fini** (critères mesurables)
- ✅ **Gouvernance** (niveau d'autonomie GREEN/YELLOW/RED)
- ✅ **Documentation préalable** pour actions YELLOW/RED

**Workflow type:**
1. Lire contexte, objectif, ressources
2. Commenter votre proposition/avancement dans l'issue
3. Attendre validation si niveau YELLOW/RED
4. Créer les fichiers/livrables
5. Cocher les items de la checklist

### 5️⃣ Libérer le Verrou

**Quand vous avez terminé:**

1. **Commenter l'issue** :
```markdown
✅ **Travail Terminé**
- Livrable créé: [LIEN_FICHIER]
- Commit SHA: [SHA_COMPLET]
- Durée: [XX minutes]

🔓 Verrou libéré - Issue prête pour validation
```

2. **Retirer label `ia-locked`**
3. **Ajouter label `ia-completed`** (ou `needs-validation`)
4. **Passer à l'issue suivante** si disponible

---

## 🛡️ Garde-Fous Anti-Conflit

### Si Une Autre IA Travaille Déjà

**Vérifiez TOUJOURS avant de prendre une issue:**

```bash
# Vérifier les commentaires récents (< 30min)
gh issue view NUMERO --comments
```

**Si vous voyez un verrou `ia-locked` posé il y a < 30min:**
- ❌ **NE PRENEZ PAS** cette issue
- ✅ Passez à une autre issue `ia-available`

**Si verrou `ia-locked` posé il y a > 30min (timeout):**
- ✅ Vous POUVEZ prendre la relève
- ⚠️ Commentez: "Timeout détecté, je prends la relève"
- 🔄 Posez VOTRE verrou

### Si Plusieurs Issues Disponibles

**Ordre de priorité** (sauf indication contraire):
1. Issues **sans dépendances**
2. Issues avec label `priority:high`
3. Issues créées en premier (FIFO)

---

## 📊 Coordination Entre IA

### Communication Asynchrone

**Toute coordination se fait via commentaires d'issues:**

**Exemples:**
- "@IA-Researcher: J'ai besoin de la bibliographie avant de finaliser #2"
- "@IA-Designer: Proposition de palette couleurs dans #4, merci de valider"

**Utilisez les mentions** pour notifier:
- `@stefm78` (Initiateur - décisions stratégiques)
- `@IA-ChefProjet` (coordination générale)
- `@IA-[Persona]` (demande à un persona spécifique)

### Dépendances Entre Issues

**Chaque issue indique ses dépendances dans la section "Méta".**

**Si une issue dépend d'une autre:**
1. Vérifiez l'état de l'issue dépendante
2. Si non terminée: travaillez sur une autre issue parallèle
3. Si terminée: vous pouvez démarrer

---

## 🔄 Workflow Complet Exemple

**IA Researcher-Veilleur prend l'issue #3:**

1. ✅ Filtre issues: `ia-available` + `persona:researcher-veilleur`
2. ✅ Trouve issue #3 (Base Documentaire)
3. ✅ Vérifie commentaires (aucun verrou actif)
4. ✅ Commente: "🔒 Verrou posé - Researcher IA #2 - 13h47 CET"
5. ✅ Demande ajout label `ia-locked`
6. ✅ Commence recherche bibliographique
7. ✅ Commente avancement toutes les heures
8. ✅ Trouve 20 sources, crée `sources/base-documentaire.md`
9. ✅ Commit avec SHA: `abc123...`
10. ✅ Commente: "✅ Terminé - SHA: abc123 - 🔓 Verrou libéré"
11. ✅ Demande retrait `ia-locked` + ajout `ia-completed`
12. ✅ Passe à issue suivante si disponible

---

## 📚 Ressources Essentielles

**Fichiers à lire OBLIGATOIREMENT:**
1. `constitution-projet-ai.md` - Règles fondamentales
2. `AI_CORE.yml` - Configuration personas et workflow
3. `PROJECT_DNA.yml` - État actuel du projet
4. `README.md` - Philosophie ADN minimal

**Pour chaque issue:**
- Lire ENTIÈREMENT le corps de l'issue
- Comprendre Contexte, Objectif, Définition de fini
- Respecter Gouvernance (niveau d'autonomie)
- Suivre Méta (dépendances, durée estimée)

---

## ⚠️ Erreurs à Éviter

❌ Prendre une issue sans poser de verrou  
❌ Créer un fichier sans documenter dans l'issue  
❌ Dépasser 30min sans donner de nouvelles  
❌ Ignorer les dépendances entre issues  
❌ Travailler sur une issue `ia-locked` par une autre IA  
❌ Modifier les fichiers vitaux (constitution, AI_CORE, PROJECT_DNA) sans validation RED  

✅ Toujours commenter avant d'agir  
✅ Respecter la matrice d'autonomie (GREEN/YELLOW/RED)  
✅ Documenter chaque action dans l'issue  
✅ Vérifier état des verrous avant de prendre une issue  
✅ Libérer le verrou après travail  

---

## 🚨 En Cas de Blocage

**Si vous êtes bloqué(e):**

1. **Commenter l'issue** avec description précise du blocage
2. **Taguer `@stefm78`** (Initiateur) pour arbitrage
3. **Ajouter label `blocked`**
4. **Libérer le verrou** (autre IA peut prendre relève)
5. **Passer à une autre issue** en parallèle

**Types de blocages courants:**
- Besoin de validation Initiateur (YELLOW/RED)
- Dépendance non terminée
- Ressources externes inaccessibles
- Ambiguïté dans les instructions

---

## 📈 Suivi de l'Avancement

**Tableau de bord visuel (GitHub Projects - optionnel):**
- Colonne "Available" (issues `ia-available`)
- Colonne "In Progress" (issues `ia-locked`)
- Colonne "Validation" (issues `ia-completed`)
- Colonne "Done" (issues closed)

**Via CLI:**
```bash
gh issue list --label "ia-locked"     # Issues en cours
gh issue list --label "ia-completed"  # Issues terminées
gh issue list --label "ia-available"  # Issues disponibles
```

---

**Version:** 1.0  
**Date:** 2025-11-07  
**Auteur:** Chef de Projet IA  
**Mise à jour:** À chaque évolution du workflow  