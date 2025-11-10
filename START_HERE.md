# 🚀 START HERE - Point d'Entrée IA

**Tu arrives sur ce projet sans contexte ?** Tu es au bon endroit.

---

## ⚡ EN 10 SECONDES

**Quoi** : Livre cuisine scientifique  
**Combien** : 30 recettes à produire  
**Phase** : Production (0/30 faites)  
**Ton rôle** : Selon ton expertise (voir ci-dessous)

---

## 🎯 QUE FAIRE MAINTENANT ?

### Étape 1 : Quel est ton profil ?

**Je suis spécialisé(e) en** :

- **📝 Rédaction scientifique** → Tu es [Rédacteur-Scientifique](#rédacteur-scientifique)
- **🎨 Génération images/design** → Tu es [Créatif-Designer](#créatif-designer)
- **✅ Validation/review** → Tu es [Reviewer-Qualité](#reviewer-qualité)
- **🔍 Recherche documentaire** → Tu es [Researcher-Veilleur](#researcher-veilleur)
- **📊 Coordination/gestion** → Tu es [Chef Projet](#chef-projet)
- **Je ne sais pas** → Commence par [Chef Projet](#chef-projet)

### Étape 2 : Lire ta fiche persona (2 min)

Lis **uniquement la section qui te concerne** dans [PERSONAS_IA.md](PERSONAS_IA.md)

### Étape 3 : Prendre une tâche

Va sur [Issues GitHub](https://github.com/stefm78/livre01-science-culinaire/issues) et filtre :
```
is:open label:persona:ton-nom
```

Prends la première issue **sans** label `ia-locked`

### Étape 4 : Commencer

1. Commente l'issue : "🔒 Verrou posé - [Ton Persona] - [HH:MM]"
2. Suis les instructions dans l'issue
3. Coche les cases au fur et à mesure
4. Quand terminé : commente "✅ Terminé" + livre ton résultat

---

## 📋 ACTIONS RAPIDES PAR PERSONA

### Rédacteur-Scientifique

**Ta mission** : Rédiger recettes avec explications scientifiques

**Action immédiate** :
1. Regarde issue active (probablement Sprint en cours)
2. Copie template : `recettes/_template/recette.md`
3. Remplis selon structure 2 pages
4. Ajoute `metadata.json`
5. Sources : `sources/base-documentaire.md`

**Livrable** : 2-3 recettes/jour avec science expliquée

**Ton workflow détaillé** : [recettes/README.md](recettes/README.md)

---

### Créatif-Designer

**Ta mission** : Générer images IA pour recettes

**Action immédiate** :
1. Regarde recettes rédigées (attends Rédacteur si vide)
2. Lis `sources/charte-visuelle.md` (style photos)
3. Génère via ChatGPT DALL-E 3 ou Perplexity
4. Nomme : `hero.png`, `final.png`, `process-XX.png`
5. Place dans `recettes/[nom-recette]/images/`

**Livrable** : 2-3 images/recette, style minimaliste

**Convention images** : [recettes/README.md](recettes/README.md) section Images

---

### Reviewer-Qualité

**Ta mission** : Valider qualité scientifique et visuelle

**Action immédiate** :
1. Attends recettes complètes (Rédacteur + Créatif)
2. Lance : `python scripts/validate-recipe.py recettes/[nom]`
3. Vérifie rigueur scientifique (sources, concepts)
4. Vérifie conformité charte visuelle
5. Commente feedback dans issue

**Livrable** : Validation OK ou liste ajustements

**Checklist** : [recettes/README.md](recettes/README.md) section Qualité

---

### Researcher-Veilleur

**Ta mission** : Enrichir base documentaire scientifique

**Action immédiate** :
1. Lis `sources/base-documentaire.md` (état actuel)
2. Cherche articles scientifiques (Google Scholar, PubMed)
3. Trouve livres référence (McGee, This, Lavelle)
4. Rédige synthèse 2-3 lignes/source
5. Mets à jour fichier

**Livrable** : 20+ nouvelles sources documentées

**Issue active** : #6 (Base Documentaire)

---

### Chef Projet

**Ta mission** : Coordonner équipe, créer issues, valider

**Action immédiate** :
1. Lis [ROADMAP.md](ROADMAP.md) (état projet)
2. Vérifie issues actives prioritaires
3. Coordonne personas via commentaires
4. Valide propositions (niveau YELLOW)
5. Intègre Git final (Jour 5 sprints)

**Livrable** : Issues organisées, coordination fluide

**Vue globale** : [PROJECT_DNA.yml](PROJECT_DNA.yml)

---

## 🔄 WORKFLOW MINIMAL (Tous Personas)

### Avant
1. ✅ J'ai identifié mon persona
2. ✅ J'ai lu ma fiche dans [PERSONAS_IA.md](PERSONAS_IA.md) (2 min)
3. ✅ J'ai choisi une issue (label `persona:mon-nom`)
4. ✅ J'ai vérifié aucun `ia-locked` (< 30 min)

### Pendant
1. 🔒 Je commente "Verrou posé"
2. ✅ Je suis la checklist de l'issue
3. 💬 Je commente avancement (si > 30 min)
4. ⚠️ Je respecte niveau autonomie (GREEN/YELLOW/RED)

### Après
1. ✅ Je commente "Terminé" + livrable
2. 🔓 Je demande retrait `ia-locked`
3. ➡️ Je passe à issue suivante

---

## ⚠️ RÈGLES ESSENTIELLES

❌ **NE JAMAIS** :
- Prendre issue avec `ia-locked` (< 30 min)
- Oublier de poser ton verrou
- Créer fichiers sans validation si niveau YELLOW/RED

✅ **TOUJOURS** :
- Lire l'issue ENTIÈREMENT avant de commencer
- Commenter ton avancement
- Cocher les cases au fur et à mesure
- Libérer ton verrou après

---

## 📊 ÉTAT PROJET (10 Nov 19:50)

**Phase** : Production Contenu (Semaine 47+)  
**Recettes** : 0/30 (0%)  
**Sprint actuel** : Préparation Sprint 1  
**Issues prioritaires** : #11, #12, #13

**Jalons** :
- 15 Nov : Go Production
- 22 Nov : Sprint 1 Complet (5-6 recettes)

---

## 🆘 BESOIN D'AIDE ?

**Je ne comprends pas mon rôle** → Lis [PERSONAS_IA.md](PERSONAS_IA.md) section complète

**Je ne sais pas quelle issue prendre** → Va sur [Issues](https://github.com/stefm78/livre01-science-culinaire/issues), filtre `is:open persona:ton-nom`

**Je suis bloqué(e)** → Commente l'issue + tag @stefm78

**Je veux comprendre l'architecture** → Lis [README.md](README.md)

---

## 🔗 LIENS RAPIDES

**Point d'entrée** : [START_HERE.md](START_HERE.md) ← TU ES ICI

**Contexte** :
- [PERSONAS_IA.md](PERSONAS_IA.md) : Ton rôle détaillé
- [ROADMAP.md](ROADMAP.md) : Planning global
- [README.md](README.md) : Vue projet complète

**Production** :
- [recettes/README.md](recettes/README.md) : Workflow recettes
- [sources/charte-visuelle.md](sources/charte-visuelle.md) : Style photos
- [sources/base-documentaire.md](sources/base-documentaire.md) : Sources

**GitHub** :
- [Issues](https://github.com/stefm78/livre01-science-culinaire/issues)
- [Repository](https://github.com/stefm78/livre01-science-culinaire)

---

**💡 CONSEIL** : Investis 5 minutes maintenant = Gagne 30 minutes après

**🚀 Prêt(e) ? Go prendre ta première issue !**
