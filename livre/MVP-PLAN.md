# 🎯 Plan MVP - Livre Version 1.0

**Version** : MVP 1.0  
**Pages** : 100-120  
**Recettes** : 16  
**Chapitres** : 4  
**Deadline** : 27 décembre 2025  

---

## 📅 Planning Global

| Semaine | Dates | Phase | Livrable |
|---------|-------|-------|----------|
| **S1** | 18-22 nov | Complétion Ch.1 | 4 recettes Bases |
| **S2** | 25-29 nov | Sprint 4 - Ch.4 | 4 recettes Légumes |
| **S3** | 2-6 déc | Contenu Éditorial | Introduction + Annexes |
| **S4** | 9-13 déc | Mise en Page PAO | PDF final |
| **S5** | 16-20 déc | Buffer & Tests | Validation finale |

**Marge sécurité** : 1 semaine buffer pour imprévus

---

## 📚 Structure Livre MVP

### Table des Matières (estimation pages)

```
COUVERTURE                                    [1 page]

INTRODUCTION                                  [10 pages]
  - Philosophie science culinaire             2 pages
  - Comment utiliser ce livre                 2 pages
  - Équipement essentiel                      2 pages
  - Fondamentaux scientifiques                2 pages
  - Conseils généraux                          2 pages

CHAPITRE 1 : BASES & TECHNIQUES               [11 pages]
  - Page intercalaire                         1 page
  - Mayonnaise Stable                         2 pages
  - Vinaigrette Équilibrée                     2 pages
  - Bouillon Volaille Umami                   2 pages
  - Beurre Blanc                              2 pages

CHAPITRE 2 : VIANDES & VOLAILLES              [11 pages]
  - Page intercalaire                         1 page
  - Steak Maillard                            2 pages
  - Poulet Rôti 65°C                          2 pages
  - Bœuf Bourguignon                          2 pages
  - Magret Canard Laqué                       2 pages

CHAPITRE 3 : POISSONS & FRUITS DE MER         [11 pages]
  - Page intercalaire                         1 page
  - Saumon Mi-Cuit 55°C                       2 pages
  - Ceviche                                   2 pages
  - Moules Marinières                         2 pages
  - Lotte Rôtie                               2 pages

CHAPITRE 4 : LÉGUMES & TECHNIQUES             [11 pages]
  - Page intercalaire                         1 page
  - Légume Rôti (Caramélisation)              2 pages
  - Légume Fermenté (Lacto-Fermentation)      2 pages
  - Légume Confit (Osmose)                    2 pages
  - Légume Grillé (Maillard Végétal)          2 pages

ANNEXES                                       [20 pages]
  - Glossaire scientifique                    6 pages
  - 8 Schémas scientifiques                   8 pages
  - Index recettes                            2 pages
  - Bibliographie                             2 pages
  - Crédits & Mentions légales                2 pages

COUVERTURE DOS                                [1 page]

---
TOTAL ESTIMÉ                                  ~75 pages
```

**Note** : Estimation conservatrice. Avec marges, espaces, mise en page aérée, le livre atteindra 100-120 pages.

---

## 📄 Contenu éditorial à Créer

### Introduction (10 pages)

**📝 Fichier** : `livre/content/00-introduction/introduction.md`

**Structure** :

#### 1. Philosophie Science Culinaire (2 pages)
```markdown
# Pourquoi la Science en Cuisine ?

## La Cuisine comme Laboratoire
- Chaque recette = expérience scientifique
- Comprendre le "pourquoi" pour maîtriser le "comment"
- Répétabilité et précision

## Notre Approche
- Pédagogique et accessible
- Sources académiques vérifiables
- Techniques testables immédiatement
```

#### 2. Comment Utiliser ce Livre (2 pages)
```markdown
# Lecture des Recettes

## Structure 2 Pages
- Page 1 : Présentation + Science
- Page 2 : Recette + Variantes

## Section Science
- Concept principal expliqué
- Associations moléculaires
- Mécanismes chimiques

## Difficultés
- ●○○ Facile (accessible débutants)
- ●●○ Intermédiaire (matériel spécialisé)
- ●●● Difficile (technique avancée)
```

#### 3. Équipement Essentiel (2 pages)
```markdown
# Matériel de Base
- Thermomètre sonde (indispensable)
- Balance précision 0.1g
- Poêles fonte
- Cocotte émaillée

# Nice-to-Have
- Thermoplongeur sous-vide
- Batteur électrique
- Mixeur plongeant
```

#### 4. Fondamentaux Scientifiques (2 pages)
```markdown
# 8 Concepts Clés
(Référence aux 8 schémas)

1. Dénaturation protéique
2. Réaction de Maillard
3. Émulsion
4. Osmose
5. Fermentation
6. Extraction aromatique
7. Caramélisation
8. Gélification
```

#### 5. Conseils Généraux (2 pages)
```markdown
# Sourcing Ingrédients
# Organisation Cuisine
# Sécurité Alimentaire
```

---

### Pages Intercalaires (4 pages)

**📝 Fichiers** :
- `livre/content/01-bases/intercalaire.md`
- `livre/content/02-viandes/intercalaire.md`
- `livre/content/03-poissons/intercalaire.md`
- `livre/content/04-legumes/intercalaire.md`

**Structure type** :
```markdown
# CHAPITRE [N] : [TITRE]

## Concept Scientifique
Texte 150-200 mots expliquant le fil rouge du chapitre.

## Dans ce Chapitre
- **Recette 1** : [Nom] - [Concept]
- **Recette 2** : [Nom] - [Concept]
- **Recette 3** : [Nom] - [Concept]
- **Recette 4** : [Nom] - [Concept]
```

---

### Annexes (20 pages)

#### Glossaire (6 pages)
**📝 Fichier** : `livre/content/99-annexes/glossaire.md`

50-60 termes scientifiques définis, format :
```markdown
## A

**Acide citrique** : Acide organique présent naturellement dans les agrumes. Abaisse le pH, denature protéines.

**Allicine** : Composé soufré de l'ail libéré lors du broyage. Responsable arôme piquant.

## B
...
```

#### Index Recettes (2 pages)
**📝 Fichier** : `livre/content/99-annexes/index-recettes.md`

```markdown
# Index Alphabétique
# Index par Chapitre
# Index par Difficulté
# Index par Temps
```

#### Bibliographie (2 pages)
**📝 Fichier** : `livre/content/99-annexes/bibliographie.md`

#### Crédits (2 pages)
**📝 Fichier** : `livre/content/99-annexes/credits.md`

---

## 🔧 Outils PAO

### Logiciel Recommandé

**Option 1** : **Affinity Publisher** (★ RECOMMANDÉ)
- Coût : 75€ one-time
- Avantages : Professionnel, stable, pas d'abonnement
- Courbe apprentissage : Moyenne

**Option 2** : **Adobe InDesign**
- Coût : 33€/mois
- Avantages : Standard industrie
- Inconvénient : Abonnement obligatoire

**Option 3** : **Scribus** (Gratuit)
- Coût : Gratuit
- Inconvénient : Interface complexe, bugs

### Polices Requises

🔗 Télécharger depuis Google Fonts (gratuit) :
- **Playfair Display** : Titres chapitres/recettes
- **Inter** : Corps de texte
- **Crimson Text** : Citations/notes

---

## ✅ Checklist Production MVP

### 📝 Contenu (Semaine 1-3)

**Recettes** :
- [ ] Ch.1 : Mayonnaise Stable
- [ ] Ch.1 : Vinaigrette Équilibrée
- [ ] Ch.1 : Bouillon Volaille
- [ ] Ch.1 : Beurre Blanc
- [ ] Ch.4 : Légume Rôti
- [ ] Ch.4 : Légume Fermenté
- [ ] Ch.4 : Légume Confit
- [ ] Ch.4 : Légume Grillé

**Éditorial** :
- [ ] Introduction (10 pages)
- [ ] Intercalaire Ch.1
- [ ] Intercalaire Ch.2
- [ ] Intercalaire Ch.3
- [ ] Intercalaire Ch.4
- [ ] Glossaire (6 pages)
- [ ] Index recettes
- [ ] Bibliographie
- [ ] Crédits

### 📸 Images (Semaine 3)

- [ ] Optimiser images recettes (300dpi, CMJN)
- [ ] Optimiser schémas scientifiques
- [ ] Créer/sourcer 2-3 photos ambiance intro
- [ ] Vérifier qualité impression (test)

### 🎨 Mise en Page (Semaine 4)

**Setup** :
- [ ] Installer logiciel PAO
- [ ] Télécharger polices
- [ ] Créer projet (A4, marges, fonds perdus)

**Templates** :
- [ ] Master pages (intro, recette, annexe)
- [ ] Styles texte (H1, H2, H3, corps, légende)
- [ ] Styles images (cadres, bordures)

**Import** :
- [ ] Introduction
- [ ] 4 Intercalaires
- [ ] 16 Recettes (2 pages chacune)
- [ ] Annexes
- [ ] Toutes images

**Finitions** :
- [ ] Table des matières automatique
- [ ] Numérotation pages
- [ ] En-têtes/pieds de page
- [ ] Vérifier veuves/orphelines
- [ ] Relecture orthographe

**Export** :
- [ ] PDF print (CMJN, 300dpi, fonds perdus)
- [ ] PDF web (RGB, 150dpi, optimisé)
- [ ] Archiver sources

### 🧪 Tests (Semaine 5)

- [ ] Test impression 2-3 pages
- [ ] Vérification qualité couleurs
- [ ] Relecture complète
- [ ] Corrections finales
- [ ] Validation finale

---

## 📈 Suivi Progression

| Phase | Avancem