# 📝 Conventions Typographiques - Livre Science Culinaire

**Règles typographiques françaises à respecter strictement dans la mise en page.**

**Références** : Lexique des règles typographiques en usage à l'Imprimerie nationale, Code typographique.

---

## ✏️ Ponctuation

### Espaces Insécables

**Règle** : Espace insécable **avant** les signes de ponctuation double.

| Signe | Espace avant | Espace après | Exemple |
|-------|--------------|---------------|----------|
| `:` (deux-points) | Insécable | Sécable | `Titre : sous-titre` |
| `;` (point-virgule) | Insécable | Sécable | `Ingrédient ; quantité` |
| `!` (exclamation) | Insécable | Sécable | `Délicieux !` |
| `?` (interrogation) | Insécable | Sécable | `Pourquoi ?` |
| `«` (guillemet ouvrant) | Sécable | Insécable | `« science` |
| `»` (guillemet fermant) | Insécable | Sécable | `culinaire »` |

**Ponctuation simple** (aucun espace avant) :
- `.` (point)
- `,` (virgule)
- `…` (points de suspension)

**Scribus** : Utiliser `Ctrl+Espace` (Windows/Linux) ou `Cmd+Espace` (Mac) pour insérer espace insécable.

### Guillemets

**Guillemets français** (standard) :
- Ouvrant : `« ` (chevron + espace insécable)
- Fermant : ` »` (espace insécable + chevron)

**Exemple** : `« La science en cuisine »`

**Guillemets anglais** (à éviter) :
- Ouvrant : `“`
- Fermant : `”`

**Citation dans citation** :
- Guillemets externes : `« … »`
- Guillemets internes : `« … “…” … »`

---

## 🔢 Nombres et Unités

### Espace Insécable entre Nombre et Unité

**Règle** : Toujours un espace insécable entre valeur numérique et unité.

**Exemples corrects** :
- `180 °C` (température)
- `500 g` (grammes)
- `2 L` (litres)
- `30 min` (minutes)
- `15 cm` (centimètres)
- `10 %` (pourcentage)

**Exceptions** (pas d'espace) :
- Degrés d'angle : `45°` (sans unité explicite)
- Degrés d'alcool : `40°` (contexte clair)

### Séparateurs Milliers

**Règle** : Espace insécable fine comme séparateur (norme française ISO).

**Exemples** :
- `1 000` (mille)
- `10 000` (dix mille)
- `1 000 000` (un million)

**Scribus** : Espace insécable fine = caractère Unicode U+202F.

**Exceptions** :
- Moins de 4 chiffres : pas d'espace (`1000` ou `1 000` acceptable)
- Années : jamais d'espace (`2025`, pas `2 025`)

### Décimales

**Règle française** : Virgule comme séparateur décimal.

**Exemples** :
- `3,14` (pi)
- `0,5` (un demi)
- `12,75 €` (prix)

**À éviter** : Point décimal anglo-saxon (`3.14`).

---

## 🅰️ Majuscules et Capitales

### Majuscules Accentuées

**Règle** : Les majuscules françaises doivent **toujours** porter leurs accents.

**Exemples corrects** :
- `Émile` (pas `Emile`)
- `À propos` (pas `A propos`)
- `ÉMISSION` (pas `EMISSION`)
- `ÉVÉNEMENT` (pas `EVENEMENT`)

**Scribus** : Vérifier que la police supporte les majuscules accentuées (Playfair, Inter, Crimson = OK).

### Titres et En-Têtes

**Capitalisation titres** (style français) :
- Première lettre du premier mot en majuscule
- Reste en minuscules (sauf noms propres)

**Exemples** :
- `La science de la mayonnaise` (correct)
- `La Science De La Mayonnaise` (incorrect, style anglais)

**Exceptions** :
- Acronymes : toujours en capitales (`ADN`, `RNA`, `INRAE`)
- Noms propres : capitale initiale (`Harold McGee`, `Hervé This`)

---

## 💬 Citations et Références

### Format Citations Courtes

**Dans le texte** :
```
Selon Harold McGee, « la réaction de Maillard crée des centaines 
de molécules aromatiques ».
```

**Style** :
- Police : Crimson Text Italic 10pt
- Retrait : Aucun (citation courte intégrée)
- Guillemets : `« … »`

### Format Citations Longues (> 3 lignes)

**Bloc de citation** :
```
    La réaction de Maillard est un ensemble complexe de 
    réactions chimiques entre acides aminés et sucres 
    réducteurs sous l'effet de la chaleur.
    
    (McGee, On Food and Cooking, 2004)
```

**Style** :
- Police : Crimson Text Regular 10pt
- Retrait gauche : 1 cm
- Espacement : 0,5 ligne avant/après
- Guillemets : Aucun (retrait suffit)

---

## 🔤 Listes et Énumérations

### Listes à Puces

**Style** :
- Puce : `•` (bullet Unicode U+2022)
- Retrait puce : 0,5 cm
- Retrait texte : 1 cm
- Espacement entre items : 0,3 ligne

**Ponctuation** :
- Items courts (< 1 ligne) : Pas de ponctuation finale
- Items longs (> 1 ligne) : Point-virgule `;` sauf dernier (point `.`)

**Exemple** :
```
• Huile neutre (tournesol, pépins de raisin) ;
• Jaune d'œuf à température ambiante ;
• Moutarde de Dijon (optionnel, stabilise l'émulsion).
```

### Listes Numérotées

**Format** : `1.` `2.` `3.` (chiffre + point + espace)

**Style** :
- Numéro : Inter SemiBold 11pt
- Texte : Inter Regular 11pt
- Retrait : Aligné sur texte corps

**Exemple** :
```
1. Sortir les œufs du réfrigérateur 30 min avant.
2. Séparer jaune et blanc avec précaution.
3. Fouetter le jaune avec 1 c.à c. de moutarde.
```

---

## 📊 Tableaux

### Titres Colonnes

**Style** :
- Police : Inter SemiBold 10pt
- Alignement : Centré (sauf colonnes texte = gauche)
- Fond : Gris clair (10% noir)
- Bordure : Filet 0,5pt noir

### Cellules Corps

**Style** :
- Police : Inter Regular 10pt
- Alignement :
  - Texte : Gauche
  - Nombres : Droite
  - Symboles : Centré
- Bordures : Filet 0,25pt gris (50% noir)

### Exemple Visuel

```
+------------------+------------+-------------+
| Ingrédient      | Quantité  | Temp.       |
+==================+============+=============+
| Huile tournesol  |    250 mL  |   20 °C    |
| Jaune d'œuf     |      1 pc  |   20 °C    |
| Moutarde Dijon   |      5 g   |   20 °C    |
+------------------+------------+-------------+
```

---

## 🎭 Césures et Justification

### Césure Automatique

**Scribus** : Activer césure automatique française.

**Paramètres** :
- Langue : Français (fr_FR)
- Césure après : Minimum 2 caractères
- Césure avant : Minimum 3 caractères
- Césures consécutives : Maximum 2 lignes

**Éviter césures** :
- Noms propres (McGee, Maillard)
- Acronymes (ADN, INRAE)
- Nombres (1 000, 180 °C)
- URLs ou emails

### Veuves et Orphelines

**Définitions** :
- **Veuve** : Première ligne d'un paragraphe isolée en bas de page
- **Orpheline** : Dernière ligne d'un paragraphe isolée en haut de page

**Scribus** : Paramètres anti-veuves/orphelines dans styles de paragraphe.

**Règle** : Minimum 2 lignes en bas/haut de page.

### Justification

**Espacement mots** (corps de texte justifié) :
- Minimum : 80% espace normal
- Optimal : 100% espace normal
- Maximum : 120% espace normal

**Glyphes** : Utiliser espaces insécables fines pour éviter espacement excessif.

---

## 🖌 Styles de Caractères Spéciaux

### Italique

**Usages** :
- Mots étrangers non francissés : *food pairing*, *umami*
- Titres d'œuvres : *On Food and Cooking*
- Noms scientifiques : *Lactobacillus*, *Saccharomyces cerevisiae*
- Emphase légère : *très* important

**À éviter** : Italique pour citations (utiliser guillemets `« … »`).

### Gras

**Usages** :
- Titres et sous-titres (selon hiérarchie)
- Termes techniques à première occurrence : **émulsion**
- Encadrés "Astuce" ou "Science"

**À éviter** : Gras excessif (dilue l'impact).

### Petites Capitales

**Usages** :
- Siècles : <span style="font-variant:small-caps">xxi</span>ᵉ siècle
- Acronymes dans corps de texte : <span style="font-variant:small-caps">adn</span>

**Scribus** : Appliquer variante police "Small Caps" si disponible.

---

## 📍Footnotes et Références

### Appels de Notes

**Format** : Chiffre exposant sans parenthèses.

**Exemple** : `La réaction de Maillard¹ transforme les protéines.`

**Scribus** : Utiliser style "Exposant" (ou Format > Caractère > Position > Exposant).

### Notes de Bas de Page

**Style** :
- Police : Inter Regular 9pt
- Retrait : Numéro + 0,3 cm
- Séparateur : Filet 3 cm, 0,5pt, à gauche

**Exemple** :
```
___________
¹ McGee, Harold. On Food and Cooking, 2004, p. 778.
```

---

## 🎨 Styles Typographiques Globaux

### Hiérarchie Titres

| Niveau | Police | Taille | Graisse | Espacement |
|--------|--------|--------|---------|------------|
| H1 | Playfair Display | 24pt | Bold | 2 lignes avant, 1 après |
| H2 | Playfair Display | 18pt | SemiBold | 1,5 lignes avant, 0,5 après |
| H3 | Inter | 14pt | SemiBold | 1 ligne avant, 0,3 après |
| H4 | Inter | 12pt | Medium | 0,5 ligne avant, 0,2 après |

### Corps de Texte

**Standard** :
- Police : Inter Regular
- Taille : 11pt
- Interligne : 14pt (127% de la taille)
- Justification : Justifié (avec césure)
- Espacement paragraphes : 0,5 ligne

**Citations** :
- Police : Crimson Text Italic
- Taille : 10pt
- Interligne : 13pt
- Justification : Justifié

**Légendes Images** :
- Police : Inter Regular
- Taille : 9pt
- Couleur : Gris 60%
- Alignement : Centré sous image

---

## ✅ Checklist Typographique Finale

**Avant export PDF** :

- [ ] Espaces insécables avant `:` `;` `!` `?`
- [ ] Guillemets français `« … »` partout
- [ ] Majuscules accentuées (É, À, È, etc.)
- [ ] Espace insécable entre nombres et unités (`180 °C`)
- [ ] Virgule décimale (pas point anglo-saxon)
- [ ] 0 veuves/orphelines
- [ ] Césures cohérentes (max 2 consécutives)
- [ ] Justification harmonieuse (pas de "rivières" blanches)
- [ ] Italique pour mots étrangers et noms scientifiques
- [ ] Cohérence styles titres (H1, H2, H3)

---

**Créé** : 18 novembre 2025  
**Référence** : Lexique Imprimerie Nationale, Code Typographique  
**Responsable** : Designer-PAO IA

*Conventions Typographiques v1.0 - Production Livre Science Culinaire*
