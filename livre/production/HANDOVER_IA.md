# 🤝 HANDOVER IA - Production PAO Livre Science Culinaire

**Document de passation pour IA contributrice prenant la suite du projet PAO.**

**Date de création** : 19 novembre 2025  
**Phase active** : Phase 1 - Préparation Technique PAO  
**Deadline MVP** : 13 décembre 2025

---

## 🎯 Contexte Projet

### Projet
**Livre Science Culinaire MVP** - 16 recettes scientifiquement documentées + contenu éditorial

### État d'Avancement Global
- ✅ **Contenu MVP : 100% COMPLET** (16 recettes, 30 pages éditorial, 32+ images)
- ✅ **Infrastructure PAO : 100% CRÉÉE** (documentation, templates, scripts)
- 🟢 **Phase Active : Phase 1 PAO - Préparation Technique** (0% - démarrage immédiat)

### Objectif
Transformer le contenu markdown en **livre imprimable professionnel PDF** (100-120 pages A4)

---

## 📍 Où en Sommes-Nous ?

### ✅ Réalisé (18-19 novembre 2025)

**Infrastructure PAO complète créée** :

1. **CHECKLIST_PAO.md** : Checklist 97 tâches (3 phases)
2. **CONVENTIONS_TYPO.md** : Règles typographiques françaises
3. **01-preparation/README.md** : Guide Phase 1 (installation, setup)
4. **01-preparation/templates/README.md** : Descriptifs 5 master pages
5. **01-preparation/specifications.md** : Specs techniques impression (PDF/X-1a, CMJN, 300dpi)
6. **02-assemblage/README.md** : Workflow Phase 2 (assemblage Scribus)
7. **02-assemblage/ordre-import.md** : Séquence stricte import 67 pages
8. **02-assemblage/styles.md** : Styles typographiques Scribus
9. **03-finalisation/README.md** : Workflow Phase 3 (QA, export final)
10. **scripts/optimize-images.py** : Script conversion images 300dpi CMJN

**Issues GitHub actives** :
- **#54** : Phase 1 - Préparation Technique (0 commentaires)
- **#55** : Phase 2 - Assemblage (0 commentaires)
- **#56** : Phase 3 - Finalisation (0 commentaires)

### 🎯 À Faire Immédiatement (Phase 1)

**Cette semaine (25-29 novembre)** :

1. **Installer Scribus 1.6.4** :
   - Téléchargement : https://www.scribus.net/downloads/
   - Version recommandée : 1.6.4 (stable)
   - Configuration : Langue français, césure automatique

2. **Installer Python 3.11+ et Pillow** :
   ```bash
   python3 --version  # Vérifier version
   pip install Pillow
   ```

3. **Installer 3 polices Google Fonts** :
   - Playfair Display (Regular, Bold, Italic)
   - Inter (Regular, Medium, SemiBold)
   - Crimson Text (Regular, Italic, SemiBold)
   - Sources : https://fonts.google.com/

4. **Exécuter script optimisation images** :
   ```bash
   cd livre/production/scripts/
   python3 optimize-images.py
   ```
   - Génère : `../02-assemblage/images-optimized/` (24+ images 300dpi CMJN)

5. **Créer templates master pages dans Scribus** :
   - 5 gabarits : Couverture, Introduction, Recette, Intercalaire, Annexes
   - Voir descriptifs : `01-preparation/templates/README.md`

6. **Valider checklist Phase 1** :
   - Cocher items dans `CHECKLIST_PAO.md`
   - Commenter progression dans issue #54

---

## 📚 Documentation Essentielle

### Fichiers à Lire en Priorité (ordre recommandé)

1. **`CHECKLIST_PAO.md`** (10 min) :
   - Vision globale 3 phases
   - 97 tâches détaillées
   - Critères de validation

2. **`01-preparation/README.md`** (5 min) :
   - Installation Scribus
   - Setup polices
   - Optimisation images
   - Création templates

3. **`01-preparation/specifications.md`** (5 min) :
   - Format A4, marges, fonds perdus 3mm
   - CMJN obligatoire, 300dpi
   - PDF/X-1a:2001 export

4. **`CONVENTIONS_TYPO.md`** (3 min) :
   - Espaces insécables avant : ; ! ?
   - Guillemets français « »
   - Majuscules accentuées

5. **`02-assemblage/ordre-import.md`** (3 min) :
   - Séquence stricte 67 pages
   - Chemins fichiers sources
   - Mapping images

### Fichiers de Référence (consulter au besoin)

- **`02-assemblage/styles.md`** : Styles paragraphe Scribus
- **`01-preparation/templates/README.md`** : Gabarits master pages
- **`03-finalisation/README.md`** : Workflow export final

---

## 🗂️ Contenu Source Disponible

### Recettes (16 totales)

**Chapitre 1 - Bases & Techniques** :
- `recettes/mayonnaise-stable/recette.md`
- `recettes/vinaigrette-equilibree/recette.md`
- `recettes/bouillon-volaille-umami/recette.md`
- `recettes/beurre-blanc/recette.md`

**Chapitre 2 - Viandes & Volailles** :
- `recettes/steak-maillard/recette.md`
- `recettes/poulet-roti-65c/recette.md`
- `recettes/boeuf-bourguignon-collagene/recette.md`
- `recettes/magret-canard-laque/recette.md`

**Chapitre 3 - Poissons & Fruits de Mer** :
- `recettes/saumon-mi-cuit-55c/recette.md`
- `recettes/ceviche-marinade-acide/recette.md`
- `recettes/moules-marinieres-extraction/recette.md`
- `recettes/lotte-rotie-texture-ferme/recette.md`

**Chapitre 4 - Légumes Révélés** :
- `recettes/carottes-roties-caramelisees/recette.md`
- `recettes/chou-fleur-texture/recette.md`
- `recettes/kimchi-express/recette.md`
- `recettes/champignons-umami-shiitake/recette.md`

### Contenu Éditorial (30 pages)

- `livre/content/00-introduction/introduction.md` (10 pages)
- `livre/content/01-bases/intercalaire.md`
- `livre/content/02-viandes/intercalaire.md`
- `livre/content/03-poissons/intercalaire.md`
- `livre/content/04-legumes/intercalaire.md`
- `livre/content/99-annexes/glossaire.md` (6-7 pages)
- `livre/content/99-annexes/index-recettes.md` (2 pages)
- `livre/content/99-annexes/bibliographie.md` (2 pages)
- `livre/content/99-annexes/credits.md` (2 pages)

### Images (32+)

- 16 images hero recettes : `recettes/*/images/hero.png`
- 8 schémas scientifiques : `sources/schemas/*.png`
- Images processus (optionnel) : `recettes/*/images/process-*.png`

---

## 🎯 Workflow Recommandé

### Semaine 1 (25-29 nov) : Phase 1 Préparation

**Jours 1-2** :
- Installation Scribus + Python + Polices
- Configuration Scribus (langue, césure)
- Tests création document vierge

**Jours 3-4** :
- Exécution script `optimize-images.py`
- Vérification images générées (24+ dans `images-optimized/`)
- Création 5 templates master pages dans Scribus

**Jour 5** :
- Validation checklist Phase 1 complète
- Commit progression dans issue #54
- Préparation Phase 2

### Semaine 2 (2-6 déc) : Phase 2 Assemblage

**Création document Scribus** :
- 70 pages A4, pages en regard, marges définies
- Application master pages selon `ordre-import.md`
- Création styles paragraphe selon `styles.md`

**Import contenu séquentiel** :
- Introduction (pages 2-11)
- 4 chapitres avec recettes (pages 13-48)
- Annexes (pages 49-67)
- Intégration 32+ images

**Génération éléments** :
- Table des matières automatique (page 12)
- Numérotation pages
- Export PDF test (150dpi RGB)

### Semaine 3 (9-13 déc) : Phase 3 Finalisation

**Relecture et QA** :
- Orthographe/typographie
- Veuves/orphelines
- Cohérence pagination

**Export final** :
- PDF print (CMJN, 300dpi, PDF/X-1a)
- PDF web (RGB, 150dpi, hyperliens)
- Validation script `validate-pdf.py`

**Tests impression** :
- 3-5 pages représentatives
- Archivage preuves

**Livraison** :
- 2 PDF finaux
- Fichier source .sla
- Rapport QA

---

## ⚠️ Points d'Attention Critiques

### Erreurs à Éviter Absolument

1. **Ne PAS utiliser RGB** pour export print (CMJN obligatoire)
2. **Ne PAS oublier fonds perdus 3mm** (sinon rejet imprimeur)
3. **Ne PAS négliger résolution images** (300dpi minimum)
4. **Ne PAS sauter l'ordre d'import** (pagination incohérente sinon)
5. **Ne PAS incorporer polices partiellement** (100% obligatoire)

### Validations Obligatoires Avant Export Final

- ✅ Toutes cases checklist Phase 3 cochées
- ✅ Script `validate-pdf.py` : 0 erreurs bloquantes
- ✅ PDF/X-1a:2001 confirmé
- ✅ Toutes polices incorporées (100%)
- ✅ Toutes images CMJN 300dpi
- ✅ Tests impression validés

---

## 🔗 Ressources Externes

### Scribus
- Site officiel : https://www.scribus.net/
- Téléchargement : https://www.scribus.net/downloads/ (version 1.6.4)
- Wiki : https://wiki.scribus.net/
- Forum : https://forums.scribus.net/

### Polices (Google Fonts)
- Playfair Display : https://fonts.google.com/specimen/Playfair+Display
- Inter : https://fonts.google.com/specimen/Inter
- Crimson Text : https://fonts.google.com/specimen/Crimson+Text

### Standards Impression
- PDF/X-1a : https://www.iso.org/standard/29061.html
- Profil ICC ISO Coated v2 : https://www.eci.org/

---

## 💬 Communication et Suivi

### Issues GitHub Actives

**Issue #54** : Phase 1 - Préparation Technique
- Commentez progression quotidienne
- Signalez blocages éventuels
- Cochez items checklist

**Issue #55** : Phase 2 - Assemblage
- À activer après Phase 1 validée
- Documentation assemblage

**Issue #56** : Phase 3 - Finalisation
- À activer après Phase 2 validée
- QA collaborative et export

### Escalade Problèmes

**Si blocage technique** :
1. Vérifier documentation (`README.md`, `specifications.md`)
2. Consulter Wiki Scribus
3. Commenter dans issue GitHub concernée
4. Escalade @stefm78 si critique

### Commits Git

**Convention messages** :
- `feat(pao): [description]` : Nouvelle fonctionnalité
- `docs(pao): [description]` : Documentation
- `fix(pao): [description]` : Correction bug
- `chore(pao): [description]` : Maintenance

**Exemple** :
```bash
git add livre/production/02-assemblage/images-optimized/
git commit -m "feat(pao): optimisation 24 images 300dpi CMJN"
git push origin main
```

---

## 📊 Métriques Succès

### Indicateurs Phase 1 (cette semaine)

- ✅ Scribus installé et configuré
- ✅ Python + Pillow installés
- ✅ 3 polices installées et testées
- ✅ Script optimize-images.py exécuté (24+ images)
- ✅ 5 templates master pages créés
- ✅ Checklist Phase 1 100% cochée

### Indicateurs Phase 2 (semaine prochaine)

- ✅ Document Scribus 67+ pages créé
- ✅ 16 recettes importées (32 pages)
- ✅ 32+ images placées
- ✅ Table des matières générée
- ✅ PDF test exporté (RGB 150dpi)

### Indicateurs Phase 3 (dans 3 semaines)

- ✅ PDF print-ready (CMJN 300dpi)
- ✅ PDF web (RGB 150dpi)
- ✅ Validation QA : 0 erreurs
- ✅ Tests impression réussis
- ✅ Livraison complète 13 décembre

---

## 🎯 Résumé pour Démarrage Immédiat

**Tu es IA prenant la suite de la production PAO du livre Science Culinaire MVP.**

**Ton objectif** : Assembler 16 recettes + contenu éditorial en PDF imprimable professionnel (100-120 pages).

**Ton rôle** : Designer-PAO IA (autonomie totale, décisions techniques, respect spécifications).

**Ta deadline** : 13 décembre 2025 (3 semaines).

**Ton action immédiate** :
1. Lire `CHECKLIST_PAO.md` (10 min)
2. Lire `01-preparation/README.md` (5 min)
3. Installer Scribus 1.6.4
4. Commenter dans issue #54 : "Démarrage Phase 1 PAO - Installation en cours"
5. Suivre workflow Phase 1 (5 jours)

**Ton support** :
- Documentation complète dans `livre/production/`
- Issues GitHub pour suivi
- Contact humain : smagnand@gmail.com

**Ton succès** :
- Respect CHECKLIST_PAO.md (97 tâches)
- PDF print-ready PDF/X-1a livré 13 décembre
- 0 erreurs QA validation

---

## ✅ Checklist Handover

**Avant de démarrer, vérifie** :

- [ ] J'ai lu `CHECKLIST_PAO.md` (vision globale)
- [ ] J'ai lu `01-preparation/README.md` (Phase 1 détaillée)
- [ ] J'ai compris l'objectif : PDF print-ready 13 décembre
- [ ] J'ai identifié mon rôle : Designer-PAO IA
- [ ] J'ai accès au repo GitHub
- [ ] Je peux commenter dans issue #54
- [ ] Je sais où trouver contenu source (recettes, éditorial, images)
- [ ] Je comprends workflow 3 phases (Préparation → Assemblage → Finalisation)

**Si toutes cases cochées : GO ! Démarre Phase 1 immédiatement ! 🚀**

---

**Créé** : 19 novembre 2025  
**Auteur** : IA Contributrice (Handover)  
**Contact** : smagnand@gmail.com  
**Version** : 1.0

*Handover IA - Production PAO Livre Science Culinaire MVP*
