# ⚡ Onboarding IA - Contexte Rapide (< 5 min)

**Dernière MAJ** : 2025-11-10  
**Lecture** : 3-5 minutes  
**Objectif** : Vous rendre opérationnel(le) immédiatement

---

## 🎯 L'ESSENTIEL EN 30 SECONDES

**Projet** : Livre de cuisine scientifique (200-250 pages)  
**Cible** : 30 recettes + 60 images + 8 schémas  
**Phase** : Production Contenu (Nov 2025 - Jan 2026)  
**Statut** : 0/30 recettes produites

**Votre mission** : Contribuer selon votre persona spécialisé

---

## 🆔 ÉTAPE 1 : Identifier Votre Rôle (30 sec)

### Quel Persona Êtes-Vous ?

**🏅 Chef Projet IA**
- Coordination globale
- Création issues & roadmap
- Intégration Git finale

**📝 Rédacteur-Scientifique**
- Recherche documentaire
- Rédaction recettes (recette.md)
- Explications scientifiques

**🎨 Créatif-Designer**
- Génération images IA
- Respect charte visuelle
- Post-production

**✅ Reviewer-Qualité**
- Validation scientifique
- Contrôle cohérence
- Scripts validation

**🔍 Researcher-Veilleur**
- Enrichissement base documentaire
- Veille scientifique
- Sourcing références

➡️ **Votre persona** détermine quelle(s) issue(s) prendre

---

## 📋 ÉTAPE 2 : Trouver Votre Tâche (1 min)

### Issues Actives Prioritaires

**Phase 1 (Semaine 46 - Critique)**
- **#11** 🔴 Finalisation Fondations → Chef Projet
- **#12** 🟠 Liste 30 Recettes → Rédacteur + Chef Projet
- **#6** 🟡 Base Documentaire → Researcher-Veilleur
- **#8** 🟡 Schémas (merge requis) → Créatif-Designer

**Phase 2 (Semaine 47+)**
- **#13** 🟠 Sprint 1 - Chapitre 1 → Tous personas
- Issues sprints 2-8 : À créer

### Comment Trouver Issues Pour Vous

**Via GitHub Web** :
1. Onglet "Issues"
2. Filtre : `is:open label:persona:votre-nom`
3. Prendre issue sans label `ia-locked`

**Ordre priorité** :
1. Label `critique` ou `haute`
2. Issues sans dépendances
3. Plus anciennes (FIFO)

---

## 📚 ÉTAPE 3 : Contexte Minimum (2 min)

### 3 Documents à Lire OBLIGATOIREMENT

#### 1️⃣ [PERSONAS_IA.md](PERSONAS_IA.md) (2 min)
**CE QUE VOUS DEVEZ SAVOIR** :
- Votre rôle détaillé (missions, outils, KPIs)
- Niveau autonomie (🟢 GREEN / 🟡 YELLOW / 🔴 RED)
- Workflow collaboratif avec autres personas

#### 2️⃣ [ROADMAP.md](ROADMAP.md) (2 min - scan visuel)
**CE QUE VOUS DEVEZ SAVOIR** :
- Phase actuelle + prochaine
- Timeline globale (jalons)
- Sprints 1-8 planifiés

#### 3️⃣ Issue que vous prenez (1 min)
**CE QUE VOUS DEVEZ SAVOIR** :
- 🎯 Objectif clair
- ✅ Définition de fini
- 🔗 Dépendances (issues bloquantes)
- 🔒 Niveau autonomie

### Documents Contexte Optionnels (si besoin)

**Si Rédacteur-Scientifique** :
- [sources/cadrage-editorial.md](sources/cadrage-editorial.md) : Structure 8 chapitres
- [sources/base-documentaire.md](sources/base-documentaire.md) : Sources scientifiques
- [recettes/README.md](recettes/README.md) : Workflow détaillé

**Si Créatif-Designer** :
- [sources/charte-visuelle.md](sources/charte-visuelle.md) : Style photos
- [recettes/README.md](recettes/README.md) : Conventions images

**Si Reviewer-Qualité** :
- [recettes/README.md](recettes/README.md) : Checklist validation
- Scripts : `validate-recipe.py`

**Si Researcher-Veilleur** :
- [sources/base-documentaire.md](sources/base-documentaire.md) : Structure actuelle

---

## 🔐 ÉTAPE 4 : Poser Verrou & Travailler (1 min setup)

### Avant de Commencer

**⚠️ CRITIQUE : Toujours poser verrou avant travail**

1. **Commenter l'issue** :
```markdown
🔒 **Verrou Posé**
- Persona: [VOTRE_PERSONA]
- Début: [HH:MM CET]
- Durée estimée: [XX min]
```

2. **Demander ajout label** `ia-locked` (dans commentaire)

3. **Retirer label** `ia-available` si présent

### Pendant le Travail

**Respecter strictement** :
- ✅ Checklist de l'issue (cocher au fur et à mesure)
- ✅ Définition de fini (critères mesurables)
- ✅ Niveau autonomie (GREEN = go / YELLOW = validation / RED = escalade)

**Si niveau YELLOW** :
- Documenter proposition dans commentaire issue
- Attendre validation Chef Projet ou @stefm78
- Ne pas créer fichiers avant validation

**Si niveau RED** :
- Documenter analyse + options dans commentaire
- Escalade obligatoire @stefm78
- Attendre décision avant action

**Donner nouvelles** :
- Commenter avancement toutes les 30 min si long
- Ou commenter à chaque étape majeure

### Après le Travail

1. **Commenter résultat** :
```markdown
✅ **Travail Terminé**
- Livrable: [LIEN ou DESCRIPTION]
- Commit: [SHA si applicable]
- Durée réelle: [XX min]

🔓 Verrou libéré
```

2. **Cocher toutes les cases** de la checklist

3. **Demander retrait** `ia-locked` + ajout `ia-completed`

4. **Passer à issue suivante** si disponible

---

## 🚀 RACCOURCIS PAR PERSONA

### Vous êtes Rédacteur-Scientifique ?

**Action immédiate** :
1. Lire issue active (ex: #13 Sprint 1)
2. Consulter template : `recettes/_template/recette.md`
3. Lire `sources/base-documentaire.md` pour sources
4. Suivre workflow : `recettes/README.md`
5. Produire 2-3 recettes/jour selon sprint

**Livrables types** :
- Fichiers `recette.md` (structure 2 pages)
- Fichiers `metadata.json` (métadonnées)
- Sources scientifiques citées

### Vous êtes Créatif-Designer ?

**Action immédiate** :
1. Lire issue active (ex: #8 schémas ou #13 images recettes)
2. Consulter `sources/charte-visuelle.md`
3. Utiliser outil : ChatGPT DALL-E 3, Perplexity
4. Respecter conventions : `hero.png`, `final.png`
5. Optimiser poids < 3 MB

**Livrables types** :
- Images PNG 2048x2048px min
- Schémas SVG/PNG/PDF
- Documentation prompts utilisés

### Vous êtes Reviewer-Qualité ?

**Action immédiate** :
1. Attendre recettes complètes (Jour 4 sprint)
2. Exécuter `scripts/validate-recipe.py`
3. Vérifier rigueur scientifique (sources, concepts)
4. Contrôler conformité visuelle (charte)
5. Feedback constructif en commentaire issue

**Livrables types** :
- Validation OK ou liste ajustements
- Rapport qualité dans commentaire issue

### Vous êtes Researcher-Veilleur ?

**Action immédiate** :
1. Lire issue #6 (enrichissement base)
2. Rechercher articles scientifiques (Google Scholar, PubMed)
3. Identifier livres référence (McGee, This, Lavelle)
4. Rédiger synthèse 2-3 lignes par source
5. Mettre à jour `sources/base-documentaire.md`

**Livrables types** :
- 20+ nouvelles sources documentées
- Organisation thématique claire

### Vous êtes Chef Projet ?

**Action immédiate** :
1. Vérifier état Phase 1 (issue #11)
2. Coordonner personas via commentaires issues
3. Valider propositions niveau YELLOW
4. Intégrer commits finaux (Jour 5 sprints)
5. Générer index : `scripts/generate-index.py`

**Livrables types** :
- Issues créées et organisées
- Validation finale avant merge
- Documentation mise à jour

---

## 📊 SUIVI RAPIDE DE L'ÉTAT PROJET

### Métriques Instantanées

**Recettes** : 0/30 (0%) → Objectif : 4-5/semaine  
**Images** : 7/60+ (12%) → Objectif : 2-3/recette  
**Schémas** : 8/8 (100%) ✅ → Merger branche  
**Sprints** : 0/8 (0%) → Lancer Sprint 1 Sem 47

### Jalons Immédiats

- **12 Nov** : Go Technique (photos + schémas OK)
- **13 Nov** : Fiche pilote validée
- **15 Nov** : Go Production (liste 30 recettes définie)
- **22 Nov** : Sprint 1 complet (5-6 recettes Ch.1)

---

## ⚠️ ERREURS FRÉQUENTES À ÉVITER

❌ **Prendre issue sans lire contexte minimum** (3 docs obligatoires)  
❌ **Oublier de poser verrou** (risque conflit avec autre IA)  
❌ **Créer fichiers avant validation YELLOW/RED**  
❌ **Ignorer checklist de l'issue**  
❌ **Ne pas commenter avancement**  
❌ **Travailler > 30 min sans nouvelles**  
❌ **Oublier de libérer verrou après travail**

✅ **Lire 3 docs obligatoires** (5 min investies = gain efficacité)  
✅ **Toujours poser verrou** avant travail  
✅ **Respecter niveau autonomie** de l'issue  
✅ **Cocher checklist** au fur et à mesure  
✅ **Commenter régulièrement** (coordination asynchrone)  
✅ **Libérer verrou** dès terminé  
✅ **Passer à issue suivante** si disponible

---

## 🆘 EN CAS DE BLOCAGE

**Si vous ne comprenez pas l'issue** :
1. Commenter : "❓ Besoin clarification sur [point précis]"
2. Taguer @stefm78 ou @Chef-Projet-IA
3. Passer temporairement à autre issue

**Si dépendance bloquante** :
1. Vérifier état issue dépendante
2. Si non terminée : travailler sur issue parallèle
3. Commenter : "⏸️ En attente issue #X"

**Si conflit avec autre IA** :
1. Vérifier commentaires récents (< 30 min)
2. Si verrou actif : prendre autre issue
3. Si timeout (> 30 min) : prendre relève (commenter)

**Si erreur technique** :
1. Documenter erreur précisément dans commentaire
2. Ajouter label `blocked`
3. Taguer @stefm78
4. Libérer verrou (autre IA peut aider)

---

## 🎓 RÉCAPITULATIF : CHECKLIST DÉMARRAGE

**Avant de commencer** (5 min) :
- [ ] J'ai lu ce fichier (ONBOARDING_IA.md)
- [ ] J'ai identifié mon persona dans [PERSONAS_IA.md](PERSONAS_IA.md)
- [ ] J'ai scanné [ROADMAP.md](ROADMAP.md) (phase actuelle)
- [ ] J'ai choisi une issue adaptée à mon persona
- [ ] J'ai lu ENTIÈREMENT l'issue (objectif + checklist + DoF)
- [ ] J'ai vérifié aucun verrou actif (< 30 min)

**Au démarrage** (1 min) :
- [ ] J'ai commenté "🔒 Verrou posé"
- [ ] J'ai demandé ajout label `ia-locked`
- [ ] J'ai identifié niveau autonomie (GREEN/YELLOW/RED)
- [ ] Je connais mes livrables attendus

**Pendant le travail** :
- [ ] Je respecte la checklist de l'issue
- [ ] Je commente mon avancement (toutes les 30 min si long)
- [ ] Je demande validation si niveau YELLOW/RED
- [ ] Je coche les items terminés au fur et à mesure

**À la fin** (1 min) :
- [ ] J'ai commenté "✅ Terminé" avec livrables
- [ ] J'ai coché toutes les cases de la checklist
- [ ] J'ai demandé retrait `ia-locked` + ajout `ia-completed`
- [ ] J'ai commenté "🔓 Verrou libéré"

---

## 🔗 LIENS RAPIDES ESSENTIELS

**Documentation Onboarding** :
- ⚡ Ce fichier : [ONBOARDING_IA.md](ONBOARDING_IA.md)
- 👥 Votre rôle : [PERSONAS_IA.md](PERSONAS_IA.md)
- 🗺️ Planning : [ROADMAP.md](ROADMAP.md)

**Documentation Projet** :
- 📖 Vue générale : [README.md](README.md)
- 🏗️ Architecture : [INFRASTRUCTURE.md](INFRASTRUCTURE.md)
- 🧬 ADN projet : [PROJECT_DNA.yml](PROJECT_DNA.yml)

**Documentation Production** :
- 📝 Workflow recettes : [recettes/README.md](recettes/README.md)
- 📋 Template recette : [recettes/_template/recette.md](recettes/_template/recette.md)
- 🎨 Charte visuelle : [sources/charte-visuelle.md](sources/charte-visuelle.md)
- 📚 Base documentaire : [sources/base-documentaire.md](sources/base-documentaire.md)

**GitHub** :
- 🐛 Issues : https://github.com/stefm78/livre01-science-culinaire/issues
- 📂 Repository : https://github.com/stefm78/livre01-science-culinaire

---

**Version** : 1.0  
**Créé** : 2025-11-10  
**Objectif** : IA opérationnelle en < 5 minutes  
**Feedback** : Commenter amélioration via issue dédiée

---

## 💡 CONSEIL FINAL

**Investissez 5 minutes de lecture = Gagnez 30 minutes d'efficacité**

Les 3 documents obligatoires (PERSONAS_IA.md, ROADMAP.md, issue) contiennent TOUT ce dont vous avez besoin pour être immédiatement productif(ve).

**Ne sautez pas cette étape** → Vous travaillerez mieux et plus vite.

**Bonne contribution ! 🚀**