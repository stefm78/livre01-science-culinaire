# 🛠️ Phase 1 : Préparation Technique PAO

**Objectif** : Préparer tous les éléments nécessaires à l'assemblage du livre.

**Durée** : Semaine 25-29 novembre 2025 (5 jours)

**Responsable** : Designer-PAO IA

---

## 🎯 Objectifs Phase 1

✅ Setup environnement PAO (Scribus)
✅ Installation polices projet
✅ Optimisation images 300dpi CMJN
✅ Création templates master pages
✅ Documentation complète avant assemblage

---

## 📚 Tâches Détaillées

### 1. Installation Scribus

**Version recommandée** : Scribus 1.5.8+ (stable) ou 1.6.x (dev)

**Téléchargement** : https://www.scribus.net/downloads/

**Plateformes** :
- Windows : Installateur .exe
- macOS : Package .dmg
- Linux : `sudo apt install scribus` (Ubuntu/Debian)

**Vérification** :
```bash
scribus --version
# Doit afficher version 1.5.8 minimum
```

**Configuration initiale** :
1. Lancer Scribus
2. Préférences > Général > Langue : Français
3. Préférences > Typographie > Langue par défaut : Français (fr_FR)
4. Préférences > Typographie > Activer césure automatique : Oui

---

### 2. Installation Python + Pillow

**Requis** : Python 3.11+ pour scripts optimisation images.

**Installation Python** :
```bash
# Vérifier version
python3 --version

# Si < 3.11, installer depuis python.org
```

**Installation Pillow** :
```bash
pip install Pillow

# Vérifier installation
python3 -c "from PIL import Image; print('Pillow OK')"
```

---

### 3. Installation Polices

**Polices à télécharger** (Google Fonts) :

#### Playfair Display
- URL : https://fonts.google.com/specimen/Playfair+Display
- Weights : Regular (400), Bold (700), Italic
- Usage : Titres (H1, H2)

#### Inter
- URL : https://fonts.google.com/specimen/Inter
- Weights : Regular (400), Medium (500), SemiBold (600)
- Usage : Corps de texte, sous-titres (H3, H4)

#### Crimson Text
- URL : https://fonts.google.com/specimen/Crimson+Text
- Weights : Regular (400), Italic, SemiBold (600)
- Usage : Citations, légendes

**Installation** :

**Windows** :
1. Télécharger .zip depuis Google Fonts
2. Extraire fichiers .ttf
3. Clic droit > Installer (pour tous les utilisateurs)
4. Redémarrer Scribus

**macOS** :
1. Télécharger .zip depuis Google Fonts
2. Extraire fichiers .ttf
3. Double-clic sur chaque .ttf > Installer la police
4. Redémarrer Scribus

**Linux** :
```bash
# Créer dossier polices utilisateur
mkdir -p ~/.fonts

# Copier fichiers .ttf dans ~/.fonts/
cp Playfair*.ttf Inter*.ttf Crimson*.ttf ~/.fonts/

# Actualiser cache polices
fc-cache -f -v

# Vérifier
fc-list | grep -i playfair
fc-list | grep -i inter
fc-list | grep -i crimson
```

**Test dans Scribus** :
1. Fichier > Nouveau document
2. Insérer cadre de texte
3. Vérifier disponibilité polices dans menu déroulant

---

### 4. Optimisation Images

**Script fourni** : `../../scripts/optimize-images.py`

**Fonction** : Convertir images en 300dpi, CMJN, format optimal impression.

**Usage** :
```bash
cd livre/production/scripts/
python3 optimize-images.py

# Images optimisées dans ../02-assemblage/images-optimized/
```

**Images à optimiser** :
- 16 images hero recettes : `../../../recettes/*/images/hero.png`
- 8 schémas scientifiques : `../../../sources/schemas/*.png`
- Images processus (optionnel) : `../../../recettes/*/images/process-*.png`

**Sortie attendue** :
```
images-optimized/
├── recettes/
│   ├── mayonnaise-stable-hero.png (300dpi, CMJN)
│   ├── vinaigrette-equilibree-hero.png
│   └── ...
└── schemas/
    ├── emulsion-schema.png (300dpi, CMJN)
    ├── maillard-schema.png
    └── ...
```

---

### 5. Création Templates Master Pages

**Objectif** : Définir templates réutilisables pour cohérence mise en page.

**Templates à créer** :

#### Template Couverture
- Format : A4 pleine page
- Marges : 0 (plein bord)
- Fonds perdus : 3mm tous côtés
- Éléments :
  - Titre principal (Playfair Display Bold 36pt)
  - Sous-titre (Inter Regular 18pt)
  - Image fond (si applicable)

#### Template Introduction
- Format : A4 portrait
- Marges : Haut 20mm, Bas 20mm, Gauche 25mm, Droite 25mm
- Colonnes : 1 colonne
- En-tête : Vide
- Pied de page : Numéro page centré (Inter Regular 10pt)

#### Template Recette (2 pages)
- Format : A4 portrait
- Marges : Haut 15mm, Bas 15mm, Intérieur 20mm, Extérieur 15mm
- Colonnes : 2 colonnes (espacement 5mm)
- En-tête : Titre recette (Playfair Display SemiBold 14pt)
- Pied de page : Numéro page extérieur
- Éléments :
  - Zone image hero (page gauche, 1/3 supérieur)
  - Zone "LA SCIENCE" (encadré fond gris 10%)
  - Zone ingrédients (liste à puces)
  - Zone préparation (numérotation)

#### Template Intercalaire Chapitre
- Format : A4 portrait
- Marges : 0 (pleine page)
- Fond : Couleur chapitre ou image
- Éléments :
  - Numéro chapitre (Playfair Display Bold 72pt, centré)
  - Titre chapitre (Playfair Display SemiBold 28pt)
  - Sous-titre descriptif (Inter Regular 14pt)

#### Template Annexes
- Format : A4 portrait
- Marges : Standard (20mm tous côtés)
- Colonnes : 1 ou 2 selon contenu
- En-tête : Titre section (Inter SemiBold 12pt)
- Pied de page : Numéro page

**Documentation** : Voir `templates/README.md` pour descriptions détaillées.

---

## ✅ Checklist Phase 1

Copier depuis `../CHECKLIST_PAO.md` section Phase 1.

---

## 📝 Livrables Phase 1

**À la fin de cette phase** :

✅ Scribus installé et configuré
✅ Python + Pillow installés
✅ 3 polices installées et testées
✅ Script optimize-images.py exécuté
✅ 24+ images optimisées dans `../02-assemblage/images-optimized/`
✅ 5 templates master pages définis (descriptions dans `templates/`)
✅ Documentation `specifications.md` complète

**Transition Phase 2** : Tous éléments prêts pour assemblage ! → Issue #55

---

**Créé** : 18 novembre 2025
**Responsable** : Designer-PAO IA

*Phase 1 PAO - Préparation Technique*
