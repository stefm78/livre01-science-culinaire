# 🔨 Phase 2 : Assemblage PAO

**Objectif** : Assembler tout le contenu (recettes + éditorial + images) dans Scribus.

**Durée** : Semaine 2-6 décembre 2025 (5 jours)

**Responsable** : Designer-PAO IA

---

## 🎯 Objectifs Phase 2

✅ Importer TOUT le contenu markdown dans Scribus
✅ Placer 16 recettes (format 2 pages chacune)
✅ Intégrer 32+ images optimisées
✅ Appliquer styles typographiques uniformes
✅ Générer table des matières automatique
✅ Produire PDF assemblage quasi-final (150dpi RGB test)

---

## 📋 Ordre d'Import STRICT

**⚠️ IMPORTANT** : Suivre `ordre-import.md` à la lettre pour cohérence pagination.

**Progression** :
1. Couverture (page 1)
2. Introduction 10 pages (pages 2-11)
3. Table des matières (page 12) - à générer après assemblage
4. Chapitre 1 : Intercalaire + 4 recettes (pages 13-21)
5. Chapitre 2 : Intercalaire + 4 recettes (pages 22-30)
6. Chapitre 3 : Intercalaire + 4 recettes (pages 31-39)
7. Chapitre 4 : Intercalaire + 4 recettes (pages 40-48)
8. Annexes : Glossaire + Schémas + Index + Biblio + Crédits (pages 49-67)

**Total estimé** : 65-70 pages minimum

---

## 🔨 Workflow Assemblage

### Étape 1 : Création Document Scribus

**Fichier > Nouveau document** :

**Paramètres** :
- Format : A4 (210×297 mm)
- Orientation : Portrait
- Nombre pages : 70 (ajustable)
- Pages en regard : Oui (double-page spread)
- Première page : Droite
- Unités : Millimètres

**Marges par défaut** :
- Haut : 15 mm
- Bas : 15 mm
- Intérieur : 20 mm
- Extérieur : 15 mm

**Fonds perdus** : 3 mm tous côtés

**Enregistrer sous** : `livre-science-culinaire-mvp.sla`

---

### Étape 2 : Appliquer Master Pages

**Page > Gérer les gabarits** :

1. Importer gabarits créés Phase 1 (depuis `../01-preparation/templates/`)
2. Appliquer gabarits selon `ordre-import.md` :
   - Page 1 : "Couverture"
   - Pages 2-11 : "Introduction"
   - Page 13, 22, 31, 40 : "Intercalaire"
   - Pages 14-21, 23-30, 32-39, 41-48 : "Recette"
   - Pages 49-67 : "Annexes"

---

### Étape 3 : Créer Styles de Paragraphe

**Édition > Styles > Paragraphe** :

**Importer définitions depuis** : `styles.md`

**Styles à créer** :
- H1 (Playfair Display Bold 24pt)
- H2 (Playfair Display SemiBold 18pt)
- H3 (Inter SemiBold 14pt)
- Corps Texte (Inter Regular 11pt, interligne 14pt)
- Citation (Crimson Text Italic 10pt)
- Liste (Inter Regular 10pt)
- Légende (Inter Regular 9pt, gris 60%)

**Raccourcis clavier** : Assigner F1-F7 pour application rapide

---

### Étape 4 : Import Contenu Éditorial

**Ordre strict selon `ordre-import.md`** :

#### Introduction (Pages 2-11)

**Fichier source** : `../../content/00-introduction/introduction.md`

**Méthode** :
1. Sélectionner cadre texte page 2
2. Fichier > Importer > Obtenir le texte
3. Sélectionner `introduction.md`
4. Chaîner cadres texte sur pages 2-11 (clic icône chaînage)
5. Appliquer styles (H1, H2, Corps Texte)

#### Intercalaires Chapitres (Pages 13, 22, 31, 40)

**Fichiers sources** :
- `../../content/01-bases/intercalaire.md`
- `../../content/02-viandes/intercalaire.md`
- `../../content/03-poissons/intercalaire.md`
- `../../content/04-legumes/intercalaire.md`

**Méthode** : Importer texte dans gabarit "Intercalaire" pré-défini

#### Annexes (Pages 49-67)

**Fichiers sources** :
- Glossaire : `../../content/99-annexes/glossaire.md`
- Index : `../../content/99-annexes/index-recettes.md`
- Bibliographie : `../../content/99-annexes/bibliographie.md`
- Crédits : `../../content/99-annexes/credits.md`

**Méthode** : Importer séquentiellement avec chaînage cadres

---

### Étape 5 : Import Recettes (16 totales)

**Ordre strict selon `ordre-import.md`** :

#### Chapitre 1 (Pages 14-21)

1. **Mayonnaise Stable** (pages 14-15) : `../../../recettes/mayonnaise-stable/recette.md`
2. **Vinaigrette Équilibrée** (pages 16-17) : `../../../recettes/vinaigrette-equilibree/recette.md`
3. **Bouillon Volaille** (pages 18-19) : `../../../recettes/bouillon-volaille-umami/recette.md`
4. **Beurre Blanc** (pages 20-21) : `../../../recettes/beurre-blanc/recette.md`

#### Chapitre 2 (Pages 23-30)

5. **Steak Parfait** (pages 23-24) : `../../../recettes/steak-maillard/recette.md`
6. **Poulet Rôti 65°C** (pages 25-26) : `../../../recettes/poulet-roti-65c/recette.md`
7. **Bœuf Bourguignon** (pages 27-28) : `../../../recettes/boeuf-bourguignon-collagene/recette.md`
8. **Magret Canard** (pages 29-30) : `../../../recettes/magret-canard-laque/recette.md`

#### Chapitre 3 (Pages 32-39)

9. **Saumon Mi-Cuit** (pages 32-33) : `../../../recettes/saumon-mi-cuit-55c/recette.md`
10. **Ceviche** (pages 34-35) : `../../../recettes/ceviche-marinade-acide/recette.md`
11. **Moules Marinières** (pages 36-37) : `../../../recettes/moules-marinieres-extraction/recette.md`
12. **Lotte Rôtie** (pages 38-39) : `../../../recettes/lotte-rotie-texture-ferme/recette.md`

#### Chapitre 4 (Pages 41-48)

13. **Carottes Rôties** (pages 41-42) : `../../../recettes/carottes-roties-caramelisees/recette.md`
14. **Chou-Fleur Texturé** (pages 43-44) : `../../../recettes/chou-fleur-texture/recette.md`
15. **Kimchi Express** (pages 45-46) : `../../../recettes/kimchi-express/recette.md`
16. **Champignons Umami** (pages 47-48) : `../../../recettes/champignons-umami-shiitake/recette.md`

**Méthode par recette** :
1. Ouvrir gabarit "Recette" (double-page)
2. Importer markdown dans cadres pré-définis
3. Appliquer styles (H2 titre, Corps Texte, Liste)
4. Ajuster chaînage si débordement

---

### Étape 6 : Intégration Images

**Images optimisées dans** : `images-optimized/`

#### Images Hero Recettes (16)

**Emplacement** : Page gauche, 1/3 supérieur

**Méthode** :
1. Sélectionner cadre image gabarit "Recette"
2. Clic droit > Obtenir l'image
3. Sélectionner `images-optimized/recettes/[nom-recette]-hero.png`
4. Ajuster cadrage (clic droit > Ajuster l'image au cadre)
5. Vérifier résolution (Propriétés > Image > DPI effectif ≥ 300)

#### Schémas Scientifiques (8)

**Emplacement** : Annexes, 1 schéma par page (pages 55-62)

**Méthode** : Importer dans cadres images centrés

**Schémas** :
1. Émulsion
2. Maillard
3. Caramélisation
4. Collagène
5. Dénaturation Protéines
6. Fermentation
7. Umami
8. Osmose

---

### Étape 7 : Génération Table des Matières

**Scribus** : Fichier > Table des matières

**Configuration** :
- Inclure : Tous titres H1, H2
- Format : Titre ..... Numéro page
- Police : Inter Regular 11pt
- Position : Page 12

**Vérification** : Tous chapitres et recettes listés avec pagination correcte

---

### Étape 8 : Numérotation Pages

**Insérer > Caractère > Numéro de page** :

**Pages préliminaires (2-12)** : Romaine (i, ii, iii...)

**Corps du livre (13+)** : Arabe (1, 2, 3...)

**Position** : Pied de page, centré ou extérieur selon gabarit

---

## ✅ Checklist Phase 2

Copier depuis `../CHECKLIST_PAO.md` section Phase 2.

---

## 📝 Livrables Phase 2

**À la fin de cette phase** :

✅ Fichier Scribus complet (`livre-science-culinaire-mvp.sla`)
✅ 65-70 pages assemblées
✅ 16 recettes placées (32 pages)
✅ 32+ images intégrées
✅ Table des matières générée
✅ Styles appliqués uniformes
✅ PDF test exporté (RGB 150dpi)

**Transition Phase 3** : Relecture, corrections, export final ! → Issue #56

---

**Créé** : 18 novembre 2025  
**Responsable** : Designer-PAO IA

*Phase 2 PAO - Assemblage*
