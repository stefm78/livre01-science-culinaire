# Backlog Production Images - Mayonnaise Stable

## 📋 Statut Général

**Recette** : Mayonnaise Stable  
**Chapitre** : 1 - Bases Fondamentales  
**Priorité** : P1 (Sprint 1)  
**Date création backlog** : 2025-11-11  
**Issue GitHub** : #13

---

## 📦 Inventaire Images

### Images Obligatoires (P1)

| Fichier | Type | Statut | Priorité | Date génération | Outil | Notes |
|---------|------|--------|----------|-------------------|-------|-------|
| `hero.png` | Hero | ☐ À générer | P1 | - | - | Mayonnaise crémeuse texture veloutée |
| `final.png` | Final | ☐ À générer | P1 | - | - | Présentation avec ingrédients frais |

### Images Optionnelles (P2 - Enrichissement)

| Fichier | Type | Statut | Priorité | Date génération | Outil | Notes |
|---------|------|--------|----------|-------------------|-------|-------|
| `process-01.png` | Process | ☐ À générer | P2 | - | - | Début émulsion (transformation liquide → crémeux) |
| `detail-texture.png` | Détail | ☐ À générer | P2 | - | - | Test ruban mayonnaise (gros plan macro) |

**Légende Statuts** :  
- ☐ À générer  
- 🛠️ En production  
- ✅ Validée  
- 🔄 À retravailler  
- ❌ Rejetée

---

## ✅ Checklist Qualité

### Conformité Charte Visuelle
- [ ] Éclairage naturel doux latéral (45°)
- [ ] Arrière-plan neutre minimaliste (blanc/gris perle/bois clair)
- [ ] Tonalités chaudes et naturelles
- [ ] Pas de décors excessifs ou distrayants
- [ ] Focus net sur sujet principal, arrière-plan légèrement flou

### Spécificités Recette Mayonnaise
- [ ] Texture **crémeuse épaisse** clairement visible (pas liquide)
- [ ] Couleur **jaune pâle ivoire** naturelle (pas blanc pur, pas jaune vif)
- [ ] Brillance **naturelle** sans excès huileux
- [ ] Si test ruban : mayonnaise forme **rubans épais** retombant du fouet
- [ ] Émulsion **stable homogène** sans séparation visible
- [ ] Contraste visuel avec vinaigrette (même schéma, textures différentes)

### Technique
- [ ] Résolution minimum 1200px côté court
- [ ] Format adapté (16:9 hero/process, 4:3 ou carré final/détail)
- [ ] Balance des blancs précise (tons naturels)
- [ ] Compression optimisée sans perte qualité visible (<500 KB idéalement)
- [ ] Nom fichier conforme (hero.png, final.png, process-01.png, detail-texture.png)

---

## 📝 Notes Production

### Challenges Spécifiques
1. **Texture crémeuse** : Difficile de rendre appétissante une sauce blanche/ivoire (moins visuellement "sexy" que plats colorés)
2. **Couleur naturelle** : Éviter jaune trop vif (industriel) ou blanc pur (pas réaliste pour mayo maison)
3. **Test du ruban** : Capture mouvement figé difficile (IA facilite)
4. **Différenciation** : Montrer différence visuelle avec vinaigrette (duo pédagogique)
5. **Brillance** : Équilibre entre brillance appétissante et excès huileux

### Recommandations IA
- **Midjourney v6** (Recommandé) : Excellent rendu texture crémeuse et brillance naturelle. Paramètres : `--style raw --ar 16:9` ou `--ar 1:1`
- **DALL-E 3** : Bon pour compositions épurées et mise en scène lifestyle
- **Stable Diffusion XL** : Contrôle précis réalisme et macro. Checkpoints : RealVisXL, JuggernautXL

### Mots-clés IA Efficaces
- "professional food photography"
- "creamy homemade mayonnaise"
- "soft natural lighting 45 degree"
- "pale yellow ivory color"
- "silky ribbon texture"
- "minimalist white background"
- "shallow depth of field"
- "high-end editorial style"

---

## 🔄 Workflow Production

### Étape 1 : Génération Images P1 (Obligatoires)
1. Générer `hero.png` avec prompt détaillé README.md
2. Générer `final.png` avec prompt détaillé README.md
3. Vérifier conformité checklists ci-dessus
4. Optimiser résolution/compression si nécessaire
5. Renommer fichiers exactement `hero.png` et `final.png`
6. Placer dans dossier `recettes/mayonnaise-stable/images/`

### Étape 2 : Génération Images P2 (Optionnelles)
1. Générer `process-01.png` (début émulsion)
2. Générer `detail-texture.png` (test ruban macro)
3. Mêmes vérifications qualité que P1
4. Ajouter au dossier images/

### Étape 3 : Validation & Intégration
1. Tester affichage images dans `recette.md` (liens relatifs)
2. Vérifier cohérence visuelle avec vinaigrette-equilibree/
3. Comparer rendu avec charte visuelle projet
4. Mettre à jour statuts dans ce BACKLOG.md
5. Commit images sur branche appropriée
6. Marquer issue #13 avec label `images-complétées` si toutes recettes finalisées

---

## 📊 Suivi Avancement

**Progrès global** : 0/4 images (0%)  
**P1 (obligatoires)** : 0/2 (0%)  
**P2 (optionnelles)** : 0/2 (0%)  

**Prochaine action** : Générer hero.png et final.png (P1)  
**Responsable** : À assigner  
**Deadline estimée** : Sprint 1 (coordination avec autres recettes Chapitre 1)

---

## 🔍 Comparaison Duo Pédagogique (Mayo vs Vinaigrette)

### Mayonnaise Stable
- **Texture** : Crémeuse épaisse, rubans 🎂
- **Émulsion** : Stable permanente (3-4 jours)
- **Couleur** : Jaune pâle ivoire 🧈
- **Visuel clé** : Onctuosité, brillance, consistance

### Vinaigrette Équilibrée
- **Texture** : Liquide, gouttelettes 💧
- **Émulsion** : Temporaire (3-5 min)
- **Couleur** : Jaune doré ambré transparent
- **Visuel clé** : Séparation phases, liquidité, transparence

**Objectif images** : Montrer visuellement cette différence scientifique fondamentale (émulsion stable vs temporaire) partageant le même schéma `02-emulsions-mayo-vinaigrette.svg`.

---

## 💬 Commentaires & Ajustements

*Section réservée pour notes durant production :*

- [ ] TODO : Générer hero.png et final.png en priorité
- [ ] TODO : Comparer rendu visuel avec vinaigrette-equilibree pour duo pédagogique
- [ ] TODO : Si difficulté couleur ivoire, tester variation prompts "pale yellow" vs "ivory cream"
- [ ] TODO : Pour test ruban, essayer angle 45° avec éclairage macro latéral

---

**Dernière mise à jour** : 2025-11-11  
**Créé par** : Rédacteur-Scientifique IA  
**Statut backlog** : ✅ Finalisé et à jour