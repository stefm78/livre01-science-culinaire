# 📚 Templates - Projet Livre Science Culinaire

**Créé** : 2025-11-18  
**Maintenu par** : Chef Projet IA  
**Statut** : ✅ Opérationnel

---

## 🎯 Vue d'Ensemble

Ce dossier contient les **templates et modèles réutilisables** pour structurer et déléguer les tâches aux IAs spécialisées du projet.

**Objectif** : Garantir cohérence, qualité et efficacité dans la production du livre de 31 recettes.

---

## 📁 Contenu du Dossier

### Templates Disponibles

#### 1. TEMPLATE_PROMPT_IA.md ⭐

**Usage** : Framework modulaire pour générer des prompts détaillés destinés aux IAs spécialisées.

**Cible** :  
- Rédacteur-Scientifique  
- Créatif-Designer  
- Reviewer-Qualité  
- Researcher-Veilleur

**Structure** :  
10 modules couvrant identification, mission, ressources, contraintes, livrables, validation, autonomie, timeline, exemples et clôture.

**Quand utiliser** :  
- Au démarrage de chaque sprint (Sprints 2-8)  
- Pour chaque nouvelle recette à produire  
- Pour toute tâche complexe nécessitant délégation structurée

**Issue associée** : #23

🔗 [Consulter TEMPLATE_PROMPT_IA.md](TEMPLATE_PROMPT_IA.md)

---

## 🛠️ Guide d'Utilisation Rapide

### Pour Chef Projet IA

#### Étape 1 : Identifier le Besoin

**Questions à se poser** :  
- Quel persona doit réaliser la tâche ? (Rédacteur, Designer, Reviewer)  
- Quelle est la complexité ? (P1 Facile, P2 Intermédiaire, P3 Expert)  
- Quelle est l'urgence ? (Critique, Haute, Moyenne)  
- Y a-t-il des contraintes spécifiques ? (Date limite, dépendances)

#### Étape 2 : Sélectionner les Modules

**Modules obligatoires** (toujours inclure) :  
1. Identification et Contexte  
2. Mission Spécifique  
4. Contraintes et Standards  
5. Livrables Attendus  
10. Clôture et Communication

**Modules optionnels** (selon besoin) :  
3. Ressources (si sources spécifiques à consulter)  
6. Validation (si processus complexe)  
7. Autonomie (si ambiguité possible)  
8. Timeline (si contraintes temporelles strictes)  
9. Exemples (si tâche nécessite références concrètes)

#### Étape 3 : Personnaliser le Prompt

**Champs à remplir** :
- `[Persona Cible]` : Rédacteur-Scientifique, Créatif-Designer, etc.  
- `[Type de Tâche]` : Rédaction Recette, Génération Images, Validation Qualité  
- `[Nom Recette/Ressource]` : Steak Parfait Maillard, Mayonnaise Stable, etc.  
- `[Numéro Sprint]` : Sprint 2, Sprint 3, etc.  
- `[Nom Chapitre]` : Chapitre 2 - Viandes & Volailles  
- `[Priorité]` : 🔴 CRITIQUE, 🟠 HAUTE, 🟡 MOYENNE  
- `[Durée Estimée]` : X heures/jours

**Adapter le détail** :  
- **P1 Facile** : Prompt concis, modules essentiels uniquement  
- **P2 Intermédiaire** : Prompt détaillé, tous modules standards  
- **P3 Expert** : Prompt exhaustif, tous modules + exemples + validation renforcée

#### Étape 4 : Poster et Assigner

**Où poster le prompt** :  
- Dans l'issue GitHub dédiée (commentaire)  
- Dans un fichier markdown séparé (si très long)

**Comment assigner** :  
- Mentionner le persona concerné : `@Rédacteur-Scientifique`  
- Ajouter label persona : `persona:redacteur-scientifique`  
- Définir priorité : `priorité:haute`

---

## 📊 Exemples d'Utilisation

### Exemple 1 : Sprint 2 - Recette "Steak Parfait Maillard"

**Besoin** : Rédiger fiche recette complète avec explication scientifique Maillard.

**Prompt à générer** :  
- Persona : Rédacteur-Scientifique  
- Modules : 1, 2, 3, 4, 5, 6, 10  
- Durée : 4-6 heures  
- Priorité : 🟠 HAUTE  
- Complexité : P1 (Facile)

**Livrables attendus** :  
- `recettes/steak-maillard/recette.md`  
- `recettes/steak-maillard/metadata.json`

### Exemple 2 : Sprint 2 - Images "Mayonnaise Stable"

**Besoin** : Générer 4 images IA conformes charte visuelle.

**Prompt à générer** :  
- Persona : Créatif-Designer  
- Modules : 1, 2, 3 (charte), 4, 5, 9 (prompts), 10  
- Durée : 3-4 heures  
- Priorité : 🟠 HAUTE  
- Complexité : P1 (Standard)

**Livrables attendus** :  
- `images/hero.png`  
- `images/final.png`  
- `images/process-01.png`  
- `images/process-02.png`

### Exemple 3 : Sprint 2 - Validation Chapitre 2

**Besoin** : Valider 4 recettes du Chapitre 2 (scientifique + éditorial + visuel).

**Prompt à générer** :  
- Persona : Reviewer-Qualité  
- Modules : 1, 2, 4, 5, 6, 7 (autonomie), 10  
- Durée : 8-10 heures (4 recettes x 2-2.5h)  
- Priorité : 🔴 CRITIQUE  
- Complexité : P2 (Intermédiaire)

**Livrables attendus** :  
- Rapports validation pour chaque recette  
- Feedback GitHub structuré  
- Approbation ou demandes ajustements

---

## 📚 Ressources Complémentaires

### Documentation Projet à Connaître

**Cadrage** :  
- `START_HERE.md` : Point d'entrée projet (2 min)  
- `PERSONAS_IA.md` : Rôles et responsabilités détaillés  
- `ROADMAP.md` : Planning global 4 phases + 8 sprints

**Standards** :  
- `sources/cadrage-editorial.md` : Structure 8 chapitres  
- `sources/charte-visuelle.md` : Style photographique IA  
- `sources/base-documentaire.md` : Sources scientifiques  
- `recettes/README.md` : Workflow production recettes

**Templates Recettes** :  
- `recettes/_template/recette.md` : Structure 2 pages  
- `recettes/_template/metadata.json` : Métadonnées JSON

### Scripts de Validation

```bash
# Valider une recette
python scripts/validate-recipe.py recettes/[nom-recette]

# Valider toutes les recettes
python scripts/validate-all-recipes.py

# Générer index automatique
python scripts/generate-index.py
```

---

## ✅ Checklist Utilisation Template

**Avant de générer un prompt** :

- [ ] Identifier persona cible (Rédacteur, Designer, Reviewer)
- [ ] Définir objectif clair et mesurable
- [ ] Lister ressources nécessaires (sources, templates, schémas)
- [ ] Spécifier contraintes (charte, workflow, deadline)
- [ ] Détailler livrables attendus (fichiers, formats, emplacement)
- [ ] Estimer durée réaliste
- [ ] Définir jalons intermédiaires si tâche longue (> 1 jour)
- [ ] Prévoir processus validation
- [ ] Inclure exemples si tâche nouvelle ou complexe

**Après avoir posté le prompt** :

- [ ] Assigner persona dans l'issue GitHub
- [ ] Ajouter labels pertinents (`persona:`, `priorité:`, `sprint:`)
- [ ] Mentionner persona dans commentaire issue
- [ ] Suivre avancement via checkboxes issue
- [ ] Valider livraison selon critères définis

---

## 🔄 Évolutions Futures

### Prévu (optionnel)

- **Exemples complets de prompts** : 3 exemples détaillés (Rédacteur, Designer, Reviewer)  
  Emplacement : `sources/templates/exemples/`

- **Template Researcher-Veilleur** : Module spécialisé pour enrichissement base documentaire

- **Template Phase 3** : Adaptation pour phase Consolidation & Build (revue globale, mise en page)

### Retours d'Expérience

À mettre à jour après Sprints 2-3 :
- Ajustements modules selon retours IAs  
- Optimisations durées estimées  
- Identification points de friction workflow  
- Améliorations processus validation

---

## 🔗 Liens Utiles

**Templates Projet** :  
- [TEMPLATE_PROMPT_IA.md](TEMPLATE_PROMPT_IA.md) : Framework modulaire prompts  
- [recettes/_template/](../../recettes/_template/) : Templates recettes  

**Documentation** :  
- [PERSONAS_IA.md](../../PERSONAS_IA.md) : Rôles IAs  
- [ROADMAP.md](../../ROADMAP.md) : Planning projet  
- [sources/charte-visuelle.md](../charte-visuelle.md) : Standards visuels  

**Issues GitHub** :  
- [Issue #23](https://github.com/stefm78/livre01-science-culinaire/issues/23) : Création template prompt  
- [Toutes les issues](https://github.com/stefm78/livre01-science-culinaire/issues) : Suivi projet

---

## 👥 Support

**Questions ou problèmes** :  
1. Consulter ce README  
2. Lire TEMPLATE_PROMPT_IA.md (guide intégré)  
3. Vérifier documentation projet (START_HERE.md, PERSONAS_IA.md)  
4. Créer issue GitHub avec label `template` + `question`  
5. Mentionner @Chef-Projet-IA

---

**Créé le** : 2025-11-18  
**Maintenu par** : Chef Projet IA  
**Version** : 1.0  
**Statut** : ✅ Opérationnel