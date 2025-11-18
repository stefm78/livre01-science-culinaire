# 📚 Ordre d'Import Contenu - Assemblage PAO

**Document de référence pour import séquentiel strict.**

**⚠️ RESPECTER CET ORDRE** pour pagination cohérente.

---

## 📍 Structure Globale (65-70 pages)

```
Page 1      : Couverture
Pages 2-11  : Introduction (10 pages)
Page 12     : Table des matières
Pages 13-21 : Chapitre 1 (1 intercalaire + 4 recettes × 2 pages)
Pages 22-30 : Chapitre 2 (1 intercalaire + 4 recettes × 2 pages)
Pages 31-39 : Chapitre 3 (1 intercalaire + 4 recettes × 2 pages)
Pages 40-48 : Chapitre 4 (1 intercalaire + 4 recettes × 2 pages)
Pages 49-67 : Annexes (glossaire, schémas, index, biblio, crédits)
```

---

## 📝 Séquence d'Import Détaillée

### 1. Couverture (Page 1)

**Gabarit** : `master-cover`

**Éléments** :
- Titre principal (manuel) : "La Science en Cuisine"
- Sous-titre (manuel) : "16 recettes expliquées scientifiquement"
- Image fond (optionnel)

**Action** : Création manuelle dans gabarit

---

### 2. Introduction (Pages 2-11)

**Gabarit** : `master-intro`

**Fichier source** : `../../content/00-introduction/introduction.md`

**Import** :
1. Sélectionner cadre texte page 2
2. Fichier > Importer > Obtenir le texte
3. Chaîner cadres sur pages 2-11

**Styles à appliquer** :
- H1 : Titres principaux
- H2 : Sous-titres
- Corps Texte : Paragraphes

**Durée estimée** : 10 pages

---

### 3. Table des Matières (Page 12)

**Gabarit** : `master-intro` (ou `master-annexes`)

**Génération** : À faire **après** assemblage complet

**Méthode** : Scribus > Fichier > Table des matières

**Contenu** :
- Chapitres 1-4 avec pagination
- 16 recettes avec pagination
- Annexes avec pagination

---

### 4. Chapitre 1 : Bases & Techniques (Pages 13-21)

#### Page 13 : Intercalaire Chapitre 1

**Gabarit** : `master-intercalaire`

**Fichier source** : `../../content/01-bases/intercalaire.md`

**Éléments** :
- Numéro : "01"
- Titre : "Bases & Techniques"
- Sous-titre : "Les fondamentaux de la cuisine scientifique"

#### Pages 14-15 : Recette 1.1 - Mayonnaise Stable

**Gabarit** : `master-recipe`

**Fichier source** : `../../../recettes/mayonnaise-stable/recette.md`

**Image hero** : `images-optimized/recettes/mayonnaise-stable-hero.png`

#### Pages 16-17 : Recette 1.2 - Vinaigrette Équilibrée

**Fichier source** : `../../../recettes/vinaigrette-equilibree/recette.md`

**Image hero** : `images-optimized/recettes/vinaigrette-equilibree-hero.png`

#### Pages 18-19 : Recette 1.3 - Bouillon Volaille Umami

**Fichier source** : `../../../recettes/bouillon-volaille-umami/recette.md`

**Image hero** : `images-optimized/recettes/bouillon-volaille-umami-hero.png`

#### Pages 20-21 : Recette 1.4 - Beurre Blanc

**Fichier source** : `../../../recettes/beurre-blanc/recette.md`

**Image hero** : `images-optimized/recettes/beurre-blanc-hero.png`

---

### 5. Chapitre 2 : Viandes & Volailles (Pages 22-30)

#### Page 22 : Intercalaire Chapitre 2

**Fichier source** : `../../content/02-viandes/intercalaire.md`

**Éléments** :
- Numéro : "02"
- Titre : "Viandes & Volailles"
- Sous-titre : "Maîtrise de la cuisson et des réactions de Maillard"

#### Pages 23-24 : Recette 2.1 - Steak Parfait (Maillard)

**Fichier source** : `../../../recettes/steak-maillard/recette.md`

**Image hero** : `images-optimized/recettes/steak-maillard-hero.png`

#### Pages 25-26 : Recette 2.2 - Poulet Rôti 65°C

**Fichier source** : `../../../recettes/poulet-roti-65c/recette.md`

**Image hero** : `images-optimized/recettes/poulet-roti-65c-hero.png`

#### Pages 27-28 : Recette 2.3 - Bœuf Bourguignon (Collagène)

**Fichier source** : `../../../recettes/boeuf-bourguignon-collagene/recette.md`

**Image hero** : `images-optimized/recettes/boeuf-bourguignon-collagene-hero.png`

#### Pages 29-30 : Recette 2.4 - Magret Canard Laqué

**Fichier source** : `../../../recettes/magret-canard-laque/recette.md`

**Image hero** : `images-optimized/recettes/magret-canard-laque-hero.png`

---

### 6. Chapitre 3 : Poissons & Fruits de Mer (Pages 31-39)

#### Page 31 : Intercalaire Chapitre 3

**Fichier source** : `../../content/03-poissons/intercalaire.md`

**Éléments** :
- Numéro : "03"
- Titre : "Poissons & Fruits de Mer"
- Sous-titre : "Précision de la cuisson et dénaturation protéique"

#### Pages 32-33 : Recette 3.1 - Saumon Mi-Cuit 55°C

**Fichier source** : `../../../recettes/saumon-mi-cuit-55c/recette.md`

**Image hero** : `images-optimized/recettes/saumon-mi-cuit-55c-hero.png`

#### Pages 34-35 : Recette 3.2 - Ceviche (Dénaturation Acide)

**Fichier source** : `../../../recettes/ceviche-marinade-acide/recette.md`

**Image hero** : `images-optimized/recettes/ceviche-marinade-acide-hero.png`

#### Pages 36-37 : Recette 3.3 - Moules Marinières (Extraction)

**Fichier source** : `../../../recettes/moules-marinieres-extraction/recette.md`

**Image hero** : `images-optimized/recettes/moules-marinieres-extraction-hero.png`

#### Pages 38-39 : Recette 3.4 - Lotte Rôtie (Texture Ferme)

**Fichier source** : `../../../recettes/lotte-rotie-texture-ferme/recette.md`

**Image hero** : `images-optimized/recettes/lotte-rotie-texture-ferme-hero.png`

---

### 7. Chapitre 4 : Légumes Révélés (Pages 40-48)

#### Page 40 : Intercalaire Chapitre 4

**Fichier source** : `../../content/04-legumes/intercalaire.md`

**Éléments** :
- Numéro : "04"
- Titre : "Légumes Révélés"
- Sous-titre : "Transformations culinaires et valorisation végétale"

#### Pages 41-42 : Recette 4.1 - Carottes Rôties Caramélisées

**Fichier source** : `../../../recettes/carottes-roties-caramelisees/recette.md`

**Image hero** : `images-optimized/recettes/carottes-roties-caramelisees-hero.png`

#### Pages 43-44 : Recette 4.2 - Chou-Fleur Texturé

**Fichier source** : `../../../recettes/chou-fleur-texture/recette.md`

**Image hero** : `images-optimized/recettes/chou-fleur-texture-hero.png`

#### Pages 45-46 : Recette 4.3 - Kimchi Express (Fermentation)

**Fichier source** : `../../../recettes/kimchi-express/recette.md`

**Image hero** : `images-optimized/recettes/kimchi-express-hero.png`

#### Pages 47-48 : Recette 4.4 - Champignons Umami Shiitake

**Fichier source** : `../../../recettes/champignons-umami-shiitake/recette.md`

**Image hero** : `images-optimized/recettes/champignons-umami-shiitake-hero.png`

---

### 8. Annexes (Pages 49-67)

#### Pages 49-54 : Glossaire Scientifique (6 pages)

**Gabarit** : `master-annexes` (2 colonnes)

**Fichier source** : `../../content/99-annexes/glossaire.md`

**Durée** : 6-7 pages (48 termes)

#### Pages 55-62 : Schémas Scientifiques (8 pages)

**Gabarit** : `master-annexes` (1 colonne)

**Images** : 1 schéma par page

**Sources** :
1. Page 55 : `images-optimized/schemas/emulsion-schema.png`
2. Page 56 : `images-optimized/schemas/maillard-schema.png`
3. Page 57 : `images-optimized/schemas/caramelisation-schema.png`
4. Page 58 : `images-optimized/schemas/collagene-schema.png`
5. Page 59 : `images-optimized/schemas/denaturation-schema.png`
6. Page 60 : `images-optimized/schemas/fermentation-schema.png`
7. Page 61 : `images-optimized/schemas/umami-schema.png`
8. Page 62 : `images-optimized/schemas/osmose-schema.png`

#### Pages 63-64 : Index Recettes (2 pages)

**Fichier source** : `../../content/99-annexes/index-recettes.md`

**Format** : Liste alphabétique avec pagination

#### Pages 65-66 : Bibliographie (2 pages)

**Fichier source** : `../../content/99-annexes/bibliographie.md`

**Format** : Liste auteurs, année, titre, éditeur

#### Page 67 : Crédits (1-2 pages)

**Fichier source** : `../../content/99-annexes/credits.md`

**Contenu** : Mentions légales, crédits images IA, remerciements

---

## ✅ Checklist Import

**Après chaque import** :

- [ ] Contenu entièrement visible (pas de débordement)
- [ ] Styles appliqués correctement
- [ ] Images placées et cadrées
- [ ] Numérotation pages cohérente
- [ ] Sauvegarde fichier Scribus (.sla)

---

## 📊 Récapitulatif Comptage

| Section | Pages | Contenu |
|---------|-------|----------|
| Couverture | 1 | 1 page |
| Introduction | 10 | Pages 2-11 |
| Table matières | 1 | Page 12 |
| Chapitre 1 | 9 | 1 intercalaire + 4 recettes (pages 13-21) |
| Chapitre 2 | 9 | 1 intercalaire + 4 recettes (pages 22-30) |
| Chapitre 3 | 9 | 1 intercalaire + 4 recettes (pages 31-39) |
| Chapitre 4 | 9 | 1 intercalaire + 4 recettes (pages 40-48) |
| Glossaire | 6 | Pages 49-54 |
| Schémas | 8 | Pages 55-62 |
| Index | 2 | Pages 63-64 |
| Bibliographie | 2 | Pages 65-66 |
| Crédits | 1 | Page 67 |
| **TOTAL** | **67** | **Minimum** |

---

**Créé** : 18 novembre 2025  
**Responsable** : Designer-PAO IA

*Ordre d'Import - Assemblage PAO*
