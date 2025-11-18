# 🎨 Templates Master Pages - Livre Science Culinaire

**Templates Scribus pour cohérence mise en page.**

**Création** : Phase 1 Préparation

**Utilisation** : Phase 2 Assemblage

---

## 📚 5 Templates à Créer

### 1. Template Couverture (`master-cover`)

**Usage** : Page 1 uniquement (couverture livre)

**Format** :
- Taille : A4 portrait (210×297 mm)
- Marges : 0 mm (plein bord)
- Fonds perdus : 3 mm tous côtés
- Couleur fond : Blanc ou image pleine page

**Éléments** :

#### Titre Principal
- Texte : "La Science en Cuisine" (exemple)
- Police : Playfair Display Bold
- Taille : 36pt
- Couleur : Noir (ou contrasté)
- Position : Centré, 1/3 supérieur
- Alignement : Centré

#### Sous-Titre
- Texte : "16 recettes expliquées scientifiquement" (exemple)
- Police : Inter Regular
- Taille : 18pt
- Couleur : Gris 40%
- Position : Sous titre principal, espacement 10mm
- Alignement : Centré

#### Image Fond (optionnel)
- Cadre image pleine page avec fonds perdus
- Opacité : 30% si utilisée en arrière-plan
- Placement : Derrière textes

**Notes Scribus** :
- Créer dans : Page > Gérer les gabarits > Nouveau
- Nom gabarit : "Couverture"
- Appliquer à : Page 1

---

### 2. Template Introduction (`master-intro`)

**Usage** : Pages 2-11 (introduction 10 pages)

**Format** :
- Taille : A4 portrait (210×297 mm)
- Marges :
  - Haut : 20 mm
  - Bas : 20 mm
  - Gauche : 25 mm
  - Droite : 25 mm
- Fonds perdus : 3 mm
- Colonnes : 1 colonne

**Éléments** :

#### Zone Texte Principale
- Largeur : 160 mm (210 - 25 - 25)
- Hauteur : 257 mm (297 - 20 - 20)
- Colonnes : 1
- Justification : Justifié
- Style : "Corps Texte" (Inter Regular 11pt, interligne 14pt)

#### Pied de Page
- Cadre texte : 160×10 mm
- Position : Centré horizontal, 10mm du bas
- Contenu : Numéro page automatique (#)
- Police : Inter Regular 10pt
- Alignement : Centré

**Notes Scribus** :
- Gabarit : "Introduction"
- Numérotation : Romaine (i, ii, iii...) si souhaité
- Appliquer à : Pages 2-11

---

### 3. Template Recette (`master-recipe`)

**Usage** : Pages recettes (double-page spread, 2 pages par recette)

**Format** :
- Taille : A4 portrait (210×297 mm)
- Marges :
  - Haut : 15 mm
  - Bas : 15 mm
  - Intérieur (pli) : 20 mm
  - Extérieur : 15 mm
- Fonds perdus : 3 mm
- Colonnes : 2 colonnes, espacement 5 mm

**Éléments Page Gauche** :

#### En-Tête
- Cadre texte : 175×15 mm
- Position : Haut page, aligné marges
- Contenu : Titre recette (variable)
- Police : Playfair Display SemiBold 14pt
- Alignement : Gauche
- Couleur : Noir

#### Image Hero
- Cadre image : 175×100 mm (environ 1/3 page)
- Position : Sous en-tête, espacement 5mm
- Proportion : Conserver ratio
- Cadrage : Centré

#### Zone "LA SCIENCE"
- Cadre texte : 175×60 mm
- Position : Sous image hero
- Fond : Gris 10% (#E5E5E5)
- Bordure : 0,5pt gris 50%
- Marge interne : 5mm tous côtés
- Style : "Science" (Inter Regular 10pt, interligne 13pt)

**Éléments Page Droite** :

#### Colonnes 2
- Colonne 1 : Ingrédients (largeur 80 mm)
- Colonne 2 : Préparation (largeur 85 mm)
- Espacement : 5 mm

#### Zone Ingrédients
- Titre : "Ingrédients" (Inter SemiBold 12pt)
- Liste à puces :
  - Puce : • (bullet)
  - Retrait : 5 mm
  - Style : "Liste" (Inter Regular 10pt, interligne 13pt)

#### Zone Préparation
- Titre : "Préparation" (Inter SemiBold 12pt)
- Liste numérotée :
  - Format : 1. 2. 3.
  - Retrait : 5 mm
  - Style : "Liste" (Inter Regular 10pt, interligne 13pt)

#### Pied de Page
- Cadre texte : 175×10 mm
- Position : 10mm du bas
- Contenu : Numéro page automatique (#)
- Police : Inter Regular 10pt
- Alignement : Extérieur (gauche sur page gauche, droite sur page droite)

**Notes Scribus** :
- Gabarit : "Recette"
- Créer variantes : "Recette-Gauche" et "Recette-Droite"
- Appliquer à : Pages recettes (14-49)

---

### 4. Template Intercalaire Chapitre (`master-intercalaire`)

**Usage** : Début de chaque chapitre (pages 13, 22, 31, 40)

**Format** :
- Taille : A4 portrait (210×297 mm)
- Marges : 0 mm (pleine page)
- Fonds perdus : 3 mm
- Couleur fond : Variable par chapitre (option)

**Éléments** :

#### Numéro Chapitre
- Texte : "01" "02" "03" "04" (variable)
- Police : Playfair Display Bold
- Taille : 72pt
- Couleur : Gris clair 20% ou couleur chapitre
- Position : Centré, 1/4 supérieur
- Alignement : Centré
- Opacité : 30% (arrière-plan)

#### Titre Chapitre
- Texte : "Bases & Techniques" (exemple)
- Police : Playfair Display SemiBold
- Taille : 28pt
- Couleur : Noir
- Position : Centré, milieu page
- Alignement : Centré

#### Sous-Titre Descriptif
- Texte : "Les fondamentaux de la cuisine scientifique" (exemple)
- Police : Inter Regular
- Taille : 14pt
- Couleur : Gris 40%
- Position : Sous titre chapitre, espacement 10mm
- Alignement : Centré

**Notes Scribus** :
- Gabarit : "Intercalaire"
- Créer 4 variantes si couleurs différentes par chapitre
- Appliquer à : Pages 13, 22, 31, 40

---

### 5. Template Annexes (`master-annexes`)

**Usage** : Pages annexes (glossaire, index, biblio, crédits)

**Format** :
- Taille : A4 portrait (210×297 mm)
- Marges : 20 mm tous côtés
- Fonds perdus : 3 mm
- Colonnes : 2 colonnes (glossaire, index) ou 1 (biblio, crédits)

**Éléments** :

#### En-Tête
- Cadre texte : 170×10 mm
- Position : Haut page
- Contenu : Titre section ("Glossaire", "Index", etc.)
- Police : Inter SemiBold 12pt
- Alignement : Gauche
- Couleur : Noir
- Bordure inférieure : Filet 0,5pt gris 50%

#### Zone Contenu
- Cadre texte : 170×247 mm
- Position : Sous en-tête
- Colonnes : 2 (espacement 5mm) pour glossaire/index, 1 pour biblio/crédits
- Style : "Corps Texte" (Inter Regular 10pt, interligne 13pt)

#### Pied de Page
- Cadre texte : 170×10 mm
- Position : 10mm du bas
- Contenu : Numéro page automatique (#)
- Police : Inter Regular 10pt
- Alignement : Centré

**Notes Scribus** :
- Gabarit : "Annexes"
- Variantes : "Annexes-2col" et "Annexes-1col"
- Appliquer à : Pages 49-67

---

## 🔧 Création dans Scribus

### Méthode

1. **Ouvrir Scribus** : Fichier > Nouveau document

2. **Créer premier gabarit** :
   - Page > Gérer les gabarits
   - Nouveau > Nommer (ex: "Couverture")
   - Définir marges, colonnes

3. **Ajouter éléments au gabarit** :
   - Insérer cadres texte avec Outil Texte (T)
   - Insérer cadres image avec Outil Image (I)
   - Définir styles de paragraphe (voir `../02-assemblage/styles.md`)
   - Positionner précisément (Propriétés > X, Y, Largeur, Hauteur)

4. **Dupliquer pour variantes** :
   - Gabarit > Dupliquer
   - Modifier légèrement (ex: page gauche vs droite)

5. **Appliquer gabarits aux pages** :
   - Organiser > Pages > Appliquer gabarit
   - Sélectionner plage de pages

---

## 📝 Documentation Supplémentaire

**Fichiers à consulter** :
- `../CONVENTIONS_TYPO.md` : Règles typographiques
- `../02-assemblage/styles.md` : Définitions styles de paragraphe
- `specifications.md` : Spécifications techniques impression

**Aide Scribus** :
- Documentation officielle : https://wiki.scribus.net/
- Tutoriels gabarits : https://wiki.scribus.net/canvas/Master_Pages

---

**Créé** : 18 novembre 2025
**Responsable** : Designer-PAO IA

*Templates Master Pages - Production PAO*
