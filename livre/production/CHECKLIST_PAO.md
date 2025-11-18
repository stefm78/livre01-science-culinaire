# ✅ Checklist PAO - Livre Science Culinaire MVP

**Validation progressive par phases** - Cocher au fur et à mesure de l'avancement.

**Deadline** : 13 décembre 2025  
**Logiciel** : Scribus (open source)

---

## 📋 PHASE 1 : Préparation Technique (Semaine 25-29 nov)

### Setup Environnement

- [ ] **Scribus installé** (version 1.5.8+ recommandée)
- [ ] **Python 3.11+** installé (pour scripts)
- [ ] **Pillow** installé (`pip install Pillow`)
- [ ] Test création document vierge Scribus

### Polices

- [ ] **Playfair Display** téléchargée (Google Fonts)
  - Weights : Regular, Bold, Italic
- [ ] **Inter** téléchargée (Google Fonts)
  - Weights : Regular, Medium, SemiBold
- [ ] **Crimson Text** téléchargée (Google Fonts)
  - Weights : Regular, Italic, SemiBold
- [ ] Polices installées système (ou dans `/fonts/`)
- [ ] Polices testées dans Scribus

### Images

- [ ] Script `optimize-images.py` créé
- [ ] Script testé sur 2-3 images échantillon
- [ ] Dossier `02-assemblage/images-optimized/` créé
- [ ] **16 images hero recettes** optimisées (300dpi, CMJN)
- [ ] **8 schémas scientifiques** optimisés (300dpi, CMJN)
- [ ] **Images processus** optimisées (si disponibles)
- [ ] Total : 24+ images prêtes

### Templates Master Pages

- [ ] **Template Couverture** (.sla ou description conceptuelle)
- [ ] **Template Introduction** (marges, colonnes, styles)
- [ ] **Template Recette** (format 2 pages, layout défini)
- [ ] **Template Intercalaire Chapitre** (page simple)
- [ ] **Template Annexes** (format flexible)
- [ ] Documentation templates dans `01-preparation/templates/README.md`

### Documentation Phase 1

- [ ] `01-preparation/README.md` rédigé
- [ ] `01-preparation/specifications.md` complet
- [ ] Guide installation polices créé
- [ ] Notes spécifiques Scribus documentées

---

## 📋 PHASE 2 : Assemblage (Semaine 2-6 déc)

### Préparatifs Import

- [ ] Fichier Scribus principal créé (`livre-science-culinaire-mvp.sla`)
- [ ] Document configuré (A4, marges, fonds perdus 3mm)
- [ ] Styles de paragraphe créés (voir `02-assemblage/styles.md`)
- [ ] Styles de caractère créés
- [ ] Master pages appliquées

### Import Contenu Éditorial

**Ordre strict selon `02-assemblage/ordre-import.md`** :

- [ ] **Page 1** : Couverture (master page template)
- [ ] **Pages 2-11** : Introduction (10 pages) - `content/00-introduction/introduction.md`
- [ ] **Page 12** : Table des matières (générée après assemblage)

### Import Recettes Chapitre 1

- [ ] **Page 13** : Intercalaire Chapitre 1 - `content/01-bases/intercalaire.md`
- [ ] **Pages 14-15** : Mayonnaise Stable - `recettes/mayonnaise-stable/recette.md`
- [ ] **Pages 16-17** : Vinaigrette Équilibrée - `recettes/vinaigrette-equilibree/recette.md`
- [ ] **Pages 18-19** : Bouillon Volaille Umami - `recettes/bouillon-volaille-umami/recette.md`
- [ ] **Pages 20-21** : Beurre Blanc - `recettes/beurre-blanc/recette.md`

### Import Recettes Chapitre 2

- [ ] **Page 22** : Intercalaire Chapitre 2 - `content/02-viandes/intercalaire.md`
- [ ] **Pages 23-24** : Steak Parfait - `recettes/steak-maillard/recette.md`
- [ ] **Pages 25-26** : Poulet Rôti 65°C - `recettes/poulet-roti-65c/recette.md`
- [ ] **Pages 27-28** : Bœuf Bourguignon - `recettes/boeuf-bourguignon-collagene/recette.md`
- [ ] **Pages 29-30** : Magret Canard Laqué - `recettes/magret-canard-laque/recette.md`

### Import Recettes Chapitre 3

- [ ] **Page 31** : Intercalaire Chapitre 3 - `content/03-poissons/intercalaire.md`
- [ ] **Pages 32-33** : Saumon Mi-Cuit 55°C - `recettes/saumon-mi-cuit-55c/recette.md`
- [ ] **Pages 34-35** : Ceviche - `recettes/ceviche-marinade-acide/recette.md`
- [ ] **Pages 36-37** : Moules Marinières - `recettes/moules-marinieres-extraction/recette.md`
- [ ] **Pages 38-39** : Lotte Rôtie - `recettes/lotte-rotie-texture-ferme/recette.md`

### Import Recettes Chapitre 4

- [ ] **Page 40** : Intercalaire Chapitre 4 - `content/04-legumes/intercalaire.md`
- [ ] **Pages 41-42** : Carottes Rôties - `recettes/carottes-roties-caramelisees/recette.md`
- [ ] **Pages 43-44** : Chou-Fleur Texturé - `recettes/chou-fleur-texture/recette.md`
- [ ] **Pages 45-46** : Kimchi Express - `recettes/kimchi-express/recette.md`
- [ ] **Pages 47-48** : Champignons Umami - `recettes/champignons-umami-shiitake/recette.md`

### Import Annexes

- [ ] **Pages 49-54** : Glossaire (6 pages) - `content/99-annexes/glossaire.md`
- [ ] **Pages 55-62** : Schémas scientifiques (8 pages, 1 par page)
- [ ] **Pages 63-64** : Index recettes (2 pages) - `content/99-annexes/index-recettes.md`
- [ ] **Pages 65-66** : Bibliographie (2 pages) - `content/99-annexes/bibliographie.md`
- [ ] **Page 67** : Crédits (1-2 pages) - `content/99-annexes/credits.md`

### Intégration Images

- [ ] **Images hero placées** (16 totales, 1 par recette)
- [ ] **Images processus placées** (si disponibles)
- [ ] **Schémas placés** (8 totaux, 1 par page annexes)
- [ ] Légendes images vérifiées
- [ ] Résolution validée (300dpi minimum)

### Application Styles

- [ ] Tous titres H1 stylés (Playfair Display Bold 24pt)
- [ ] Tous titres H2 stylés (Playfair Display SemiBold 18pt)
- [ ] Tous titres H3 stylés (Inter SemiBold 14pt)
- [ ] Corps de texte uniforme (Inter Regular 11pt)
- [ ] Citations stylées (Crimson Text Italic 10pt)
- [ ] Légendes images stylées (Inter Regular 9pt, gris)

### Éléments Structurels

- [ ] **Table des matières générée** (après page 12)
- [ ] **Numérotation pages préliminaire** (pied de page)
- [ ] Cohérence master pages vérifiée
- [ ] Espacement paragraphes uniforme

### Validation Phase 2

- [ ] Total pages : 65-70 minimum
- [ ] Toutes images présentes et visibles
- [ ] Aucun débordement texte non géré
- [ ] Export PDF test réussi (RGB, 150dpi)

---

## 📋 PHASE 3 : Finalisation (Semaine 9-13 déc)

### Relecture Complète

- [ ] **Orthographe** : Relecture automatique Scribus
- [ ] **Typographie** : Vérification conventions (voir `CONVENTIONS_TYPO.md`)
  - Espaces insécables avant : ; ! ?
  - Guillemets français « »
  - Majuscules accentuées (É, À, È)
  - Nombres : espace insécable entre nombre et unité (ex: 180 °C)
- [ ] **Cohérence terminologique** : Vérification glossaire
- [ ] **Références croisées** : Validation liens internes

### Corrections Micro-Typographie

- [ ] **Veuves** éliminées (ligne isolée début de page)
- [ ] **Orphelines** éliminées (ligne isolée fin de page)
- [ ] **Coupures mots** vérifiées (césures intelligentes)
- [ ] **Justification** : Espacement mots harmonieux
- [ ] **Lignes creuses** corrigées (espacement excessif)

### Validation Images

- [ ] Toutes images nettes à 100% zoom
- [ ] Résolution minimum 300dpi confirmée
- [ ] Conversion CMJN vérifiée (script ou Scribus)
- [ ] Fonds perdus images respectés (3mm extension)
- [ ] Cadrage images cohérent

### Numérotation Finale

- [ ] **Pages préliminaires** : Numérotation romaine (i, ii, iii...)
- [ ] **Corps du livre** : Numérotation arabe (1, 2, 3...)
- [ ] **Position numéros** : Centré pied de page ou extérieur
- [ ] Cohérence numérotation table des matières

### Table des Matières

- [ ] Tous chapitres listés avec pagination exacte
- [ ] 16 recettes listées avec pagination exacte
- [ ] Annexes listées (glossaire, index, biblio, crédits)
- [ ] Hiérarchie visuelle claire (titres, sous-titres)
- [ ] Points de suite corrects (.... entre titre et numéro)

### Export PDF Print-Ready

- [ ] **Format** : A4 (210×297 mm)
- [ ] **Résolution** : 300dpi minimum
- [ ] **Espace colorimétrique** : CMJN (obligatoire impression)
- [ ] **Fonds perdus** : 3mm sur tous côtés
- [ ] **PDF/X-1a:2001** : Standard impression respecté
- [ ] **Polices incorporées** : 100% des polices embarquées
- [ ] **Compression images** : Qualité maximale (JPEG 90%+)
- [ ] Nom fichier : `livre-science-culinaire-mvp-print-v1.0.pdf`

### Export PDF Web

- [ ] **Format** : A4 (210×297 mm)
- [ ] **Résolution** : 150dpi (optimisé web)
- [ ] **Espace colorimétrique** : RGB
- [ ] **Hyperliens** : Table des matières cliquable (si possible)
- [ ] **Taille fichier** : < 20 MB (compression intelligente)
- [ ] Nom fichier : `livre-science-culinaire-mvp-web-v1.0.pdf`

### Tests Impression

- [ ] **Impression test** : 3-5 pages représentatives
  - 1 page couverture
  - 1 double-page recette
  - 1 page annexe schéma
- [ ] **Validation couleurs** : CMJN rendu fidèle
- [ ] **Validation texte** : Lisibilité optimale (corps 11pt minimum)
- [ ] **Validation images** : Netteté satisfaisante
- [ ] Photos tests documentées (screenshots ou scans)

### Quality Assurance Automatique

- [ ] Script `validate-pdf.py` exécuté
- [ ] **0 erreurs bloquantes** dans rapport QA
- [ ] Tous warnings documentés et justifiés
- [ ] Rapport QA archivé dans `03-finalisation/qa-report.txt`

### Archivage Sources

- [ ] Fichier Scribus source sauvegardé (`livre-science-culinaire-mvp.sla`)
- [ ] Dossier images sources archivé
- [ ] Polices sources archivées
- [ ] Documentation versions archivée
- [ ] Archive complète dans `03-finalisation/exports/source/`

### Livrables Finaux

- [ ] ✅ `livre-science-culinaire-mvp-print-v1.0.pdf` (version impression)
- [ ] ✅ `livre-science-culinaire-mvp-web-v1.0.pdf` (version web)
- [ ] ✅ `livre-science-culinaire-mvp.sla` (source Scribus)
- [ ] ✅ `qa-report.txt` (rapport validation)
- [ ] ✅ `README-LIVRAISON.md` (documentation livraison)

---

## 🎯 Critères de Validation Globale

### Critères Bloquants (Must-Have)

- ✅ 65-75 pages minimum assemblées
- ✅ 16 recettes complètes présentes (32 pages)
- ✅ Contenu éditorial 100% intégré (30 pages)
- ✅ 24+ images présentes et nettes
- ✅ PDF print-ready 300dpi CMJN exporté
- ✅ 0 erreurs critiques validation QA
- ✅ Tests impression validés

### Critères Qualité (Should-Have)

- ✅ Table des matières automatique générée
- ✅ Numérotation pages complète et cohérente
- ✅ Styles typographiques 100% appliqués
- ✅ 0 veuves/orphelines
- ✅ Hyperliens web fonctionnels (PDF web)
- ✅ Taille fichier web < 20 MB

### Critères Excellence (Nice-to-Have)

- ✅ Micro-typographie parfaite (justification, césures)
- ✅ Cohérence esthétique inter-chapitres
- ✅ Images processus recettes intégrées
- ✅ Enrichissements visuels (encadrés, filets)

---

## 📊 Progression Globale

**Phase 1 - Préparation** : ☐ 0/24 (0%)  
**Phase 2 - Assemblage** : ☐ 0/42 (0%)  
**Phase 3 - Finalisation** : ☐ 0/31 (0%)

**TOTAL** : ☐ 0/97 tâches (0%)

---

## 🚨 Blocages Potentiels

**Si blocage rencontré** :

1. Documenter problème dans issue #54, #55, ou #56
2. Identifier workaround temporaire
3. Escalade @stefm78 si critique
4. Mise à jour checklist avec solution

---

**Créé** : 18 novembre 2025  
**Dernière mise à jour** : 18 novembre 2025  
**Responsable** : Designer-PAO IA

*Checklist PAO v1.0 - Production Collaborative IA*
