# 🛠️ Phase 3 : Finalisation PAO

**Objectif** : Relecture complète, export final, QA collaborative et livraison.

**Durée** : Semaine 9-13 décembre 2025 (5 jours)

**Responsable** : Reviewer-Qualité IA + Designer-PAO IA

---

## 🎯 Objectifs Phase 3

✅ Relecture orthographe et typographie
✅ Contrôle qualité sur toutes les pages
✅ Application checklist `../CHECKLIST_PAO.md` phase 3
✅ Corrections veuves/orphelines
✅ Vérification références croisées
✅ Export final PDF print (300dpi CMJN)
✅ Export PDF web (150dpi RGB, hyperliens actifs)
✅ Tests impression papier
✅ Livrables archivés / exports complets

---

## 📝 Étapes détaillées

### 1. Relecture et Contrôle Qualité
- Orthographe (outil Scribus)
- Typographie : voir `../CONVENTIONS_TYPO.md`
- Veuves/orphelines/coupures mots (réglages styles)
- Justification / césure (paramètres paragraphe)
- Cohérence pagination
- Cohérence table des matières
- Vérification images (résolution, cadrage, légendes)

### 2. Application Checklist QA
- Suivre section Phase 3 de `../CHECKLIST_PAO.md`
- Cocher chaque critère avant export
- Noter tous warnings/corrections nécessaires

### 3. Correctifs et Export Finaux
- Appliquer corrections orthographe/typo
- Corriger images si floues ou basse résolution
- Ajuster pagination/cadrage au besoin
- Export PDF Print : voir `../01-preparation/specifications.md` (CMJN, PDF/X-1a, fonds perdus 3mm)
- Export PDF Web : RGB, 150dpi, hyperliens actifs si possible

### 4. Tests Impression / Validation
- Impression test 3-5 pages représentatives
- Vérification couleur texte/image (CMJN fidelity)
- Archivage preuves : screenshots/tests

### 5. QA Automatisée / Archivage
- Script `../../scripts/validate-pdf.py` lancé sur PDF print
- 0 erreurs bloquantes, tous warnings justifiés dans rapport
- Rapport archivé dans `exports/qa-report.txt`
- Sauvegarde fichier .sla + polices/images dans `exports/source/`

---

## ✅ Livrables Phase 3

- PDF print-ready 300dpi CMJN
- PDF web optimisé 150dpi RGB
- Fichier source Scribus (.sla)
- Rapport QA
- README livraison finales

---

**Créé** : 18 novembre 2025
**Responsable** : Reviewer-Qualité IA + Designer-PAO IA

*Phase 3 PAO - Finalisation et Export*