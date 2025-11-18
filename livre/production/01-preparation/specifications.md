# 📋 Spécifications Techniques Impression - Livre Science Culinaire MVP

**Document de référence pour export PDF print-ready.**

**Deadline** : 13 décembre 2025

---

## 📑 Format Document

### Dimensions

**Format final** : A4 portrait
- Largeur : 210 mm
- Hauteur : 297 mm

**Fonds perdus** : 3 mm sur tous les côtés
- Document total : 216 × 303 mm (avec fonds perdus)

**Zone de sécurité** : 5 mm à l'intérieur des marges
- Éviter éléments critiques (texte, logos) dans cette zone

---

## 🎨 Couleurs

### Espace Colorimétrique

**Obligatoire** : CMJN (Cyan, Magenta, Jaune, Noir)

**À éviter** : RVB (Rouge, Vert, Bleu) - réservé à version web

### Profil ICC

**Recommandé** : ISO Coated v2 (ECI)
- Standard européen papier couché
- Compatible majorité imprimeurs

**Alternatif** : Fogra39 (identique ISO Coated v2)

### Noir Riche

**Pour grandes zones noires** :
- Cyan : 60%
- Magenta : 40%
- Jaune : 40%
- Noir : 100%

**Pour texte** :
- Noir : 100%
- Autres : 0%

### Encrage Total

**Limite maximale** : 300% (somme CMJN)
- Exemple acceptable : C:100% + M:80% + Y:60% + K:60% = 300%
- Dépassement risque : bavures, séchage lent

---

## 🖼️ Images

### Résolution

**Minimum obligatoire** : 300 dpi (dots per inch)

**Recommandé** : 300-400 dpi

**À éviter** : < 250 dpi (qualité visible compromise)

### Format Fichiers

**Préféré** :
- PNG (sans perte, transparence)
- TIFF (sans compression, haute qualité)

**Acceptable** :
- JPEG qualité maximale (90%+)

**À éviter** :
- GIF (palette limitée)
- JPEG basse qualité (< 80%)

### Espace Colorimétrique Images

**Obligatoire** : CMJN

**Conversion** : Utiliser script `optimize-images.py` fourni

### Incorporation Images

**Scribus** : Lier images (ne pas incorporer dans .sla)

**Raison** : Permet mises à jour sans ré-import

**Vérification** : Fichier > Préférences d'impression > Images > Vérifier liens

---

## ✏️ Typographie

### Polices

**Incorporation obligatoire** : 100% des polices embarquées dans PDF

**Polices utilisées** :
- Playfair Display (Regular, Bold, Italic)
- Inter (Regular, Medium, SemiBold)
- Crimson Text (Regular, Italic, SemiBold)

**Vérification** : Fichier > Export PDF > Polices > Sélectionner toutes

### Tailles Minimales

**Lisibilité impression** :
- Corps de texte : 10pt minimum (11pt recommandé)
- Légendes : 9pt minimum
- Notes de bas de page : 8pt minimum absolu

### Anti-Aliasing

**Désactiver** pour export print
- Texte net sans lissage gris
- Scribus gère automatiquement à l'export PDF

---

## 📊 Marges et Reliure

### Marges Standard

**Pages intérieures** :
- Haut : 15-20 mm
- Bas : 15-20 mm
- Intérieur (pli) : 20-25 mm
- Extérieur : 15-20 mm

**Rationale** : Marge intérieure plus large pour reliure

### Type de Reliure

**Recommandé** : Dos carré collé (perfect binding)
- Adapté 65-75 pages
- Aspect professionnel
- Coût modéré

**Alternatif** : Brochure piquée à cheval (saddle stitch)
- Maximum 80 pages
- Coût réduit
- Pages multiples de 4 obligatoires

### Gouttière

**Espace entre colonnes** : 5 mm minimum

**Espace entre éléments** : 3 mm minimum (texte/image)

---

## 📝 Export PDF

### Version PDF

**Standard impression** : PDF/X-1a:2001

**Caractéristiques** :
- CMJN obligatoire (pas RVB)
- Polices incorporées
- Transparences aplaties
- Compatible tous imprimeurs

**Alternatif** : PDF/X-3:2002 (si profils ICC spécifiques)

### Paramètres Export Scribus

**Fichier > Exporter > Enregistrer au format PDF** :

#### Onglet "Général"
- Compatibilité : PDF/X-1a
- Inclure fonds perdus : Oui (3 mm)
- Pages : Toutes

#### Onglet "Polices"
- Incorporer toutes les polices : Oui
- Sous-ensemble polices : Oui (réduit taille)

#### Onglet "Couleur"
- Profil sortie : ISO Coated v2 (ECI)
- Convertir tout en CMJN : Oui
- Utiliser profils incorporés images : Oui

#### Onglet "Images"
- Qualité JPEG : 90% minimum (recommandé 100%)
- Résolution images : 300 dpi
- Compression : JPEG ou ZIP (sans perte)

#### Onglet "Avant-Impression"
- Traits de coupe : Oui (si demandé par imprimeur)
- Repères de montage : Oui (optionnel)
- Informations page : Oui (nom fichier, date)

### Validation PDF

**Outils** :
- Adobe Acrobat Pro : Pré-vol (Preflight)
- Script fourni : `scripts/validate-pdf.py`

**Vérifications critiques** :
- ✅ Version PDF/X-1a confirmée
- ✅ Toutes polices incorporées (100%)
- ✅ Toutes images CMJN 300dpi
- ✅ Fonds perdus 3mm présents
- ✅ Aucune transparence non aplatie
- ✅ Taille fichier raisonnable (< 100 MB)

---

## 🖨️ Papier

### Type Papier Recommandé

**Corps du livre** :
- Papier offset blanc 90-115 g/m²
- Finition : Mat ou satin

**Couverture** :
- Papier couché 250-300 g/m²
- Finition : Brillant, mat, ou pelliculage

### Grammage

**Formule épaisseur** :
- 80 g/m² : ~0,10 mm par feuille
- 90 g/m² : ~0,11 mm par feuille
- 115 g/m² : ~0,14 mm par feuille

**Exemple 70 pages en 90 g/m²** :
- Épaisseur corps : 35 feuilles × 0,11 mm = 3,85 mm
- Épaisseur totale (avec couverture) : ~4,5 mm

---

## 💾 Nomenclature Fichiers

### PDF Print-Ready

**Format** : `[projet]-[version]-print-[date].pdf`

**Exemple** : `livre-science-culinaire-mvp-print-v1.0-20251213.pdf`

**Contenu nom** :
- Projet identifiable
- Version (v1.0, v1.1, etc.)
- Indication "print" (vs "web")
- Date AAAAMMJJ

### PDF Web (optionnel)

**Format** : `[projet]-[version]-web-[date].pdf`

**Exemple** : `livre-science-culinaire-mvp-web-v1.0-20251213.pdf`

**Différences vs print** :
- RVB (pas CMJN)
- 150 dpi (pas 300)
- Hyperliens actifs
- Taille fichier réduite (< 20 MB)

---

## 🧑‍💻 Checklist Pré-Envoi Imprimeur

**Avant d'envoyer PDF à l'imprimeur** :

- [ ] **PDF/X-1a:2001** validé
- [ ] **CMJN** partout (0% RVB)
- [ ] **300 dpi** toutes images
- [ ] **Polices incorporées** 100%
- [ ] **Fonds perdus 3mm** présents
- [ ] **Marges respectées** (intérieur 20mm+)
- [ ] **Pages totales** multiples de 4 (si brochure piquée)
- [ ] **Numérotation** cohérente
- [ ] **Test impression** 2-3 pages validé
- [ ] **Validation QA** script exécuté (0 erreurs)
- [ ] **Taille fichier** < 100 MB
- [ ] **Nomenclature** conforme
- [ ] **Documentation** export archivée

---

## 📞 Contact Imprimeur

**Questions à poser avant production** :

1. **Profil ICC préféré** ? (ISO Coated v2 OK ?)
2. **Fonds perdus requis** ? (3mm standard ?)
3. **Traits de coupe nécessaires** ?
4. **Livraison fichier** : Email, FTP, ou plateforme ?
5. **Délai production** : Combien de jours ?
6. **BAT (Bon à Tirer)** : Envoi épreuve avant impression ?
7. **Nombre exemplaires** : Tarif dégressif ?
8. **Options finition** : Pelliculage, vernis ?

---

## 📚 Références

**Standards** :
- PDF/X-1a:2001 : ISO 15930-1:2001
- Profil ICC : ISO 12647-2:2004

**Ressources** :
- Guide Scribus PDF/X : https://wiki.scribus.net/canvas/PDF/X
- ECI (European Color Initiative) : https://www.eci.org/

**Outils validation** :
- Adobe Acrobat Pro (Pré-vol)
- Ghostscript (ligne de commande)
- Script projet : `scripts/validate-pdf.py`

---

**Créé** : 18 novembre 2025  
**Version** : 1.0  
**Responsable** : Designer-PAO IA

*Spécifications Techniques Impression - Livre Science Culinaire MVP*
