# BATCH sprint5-oeuf-laitages - GÉNÉRATION IMAGES IA
# Instructions pour ChatGPT - Sprint 5 : Chapitre 5 - Œufs & Laitages

**Date de création** : 18 novembre 2025  
**Sprint** : Sprint 5 - Chapitre 5 : Œufs & Laitages  
**Nombre d'images** : 8 images (2 par recette)  
**Charte visuelle** : Minimaliste scientifique, lumière naturelle

---

## 🎯 TA MISSION

Génère les **8 images ci-dessous UNE PAR UNE** avec DALL-E 3, puis crée le manifest JSON et le ZIP structuré.

**IMPORTANT** : Génère EXACTEMENT ces 8 images, ni plus ni moins. Respecte précisément les noms de fichiers et les prompts.

---

## 📸 IMAGES À GÉNÉRER

### Image 1 : oeuf-mollet-parfait-hero.png

**Prompt DALL-E 3** :
```
Minimalist food photography, soft boiled egg (6min30 cooking), cut in half on white ceramic plate, creamy flowing yolk visible, firm white, natural daylight from side, top-down view, clean white background, professional kitchen styling, high resolution 2048x2048px
```

**Description** : Œuf mollet coupé en deux, jaune coulant crémeux bien visible, blanc ferme  
**Attends confirmation puis passe à Image 2**

---

### Image 2 : oeuf-mollet-parfait-final.png

**Prompt DALL-E 3** :
```
Minimalist food photography, soft boiled egg on green salad leaves, cut in half showing creamy yolk, white ceramic plate, natural lighting from window, 45-degree angle, clean white background, professional styling, high resolution 2048x2048px
```

**Description** : Œuf mollet dressé sur salade verte, coupé, jaune coulant, présentation finale  
**Attends confirmation puis passe à Image 3**

---

### Image 3 : mousse-chocolat-aerienne-hero.png

**Prompt DALL-E 3** :
```
Minimalist food photography, airy chocolate mousse in clear glass jar, light and fluffy texture visible, dark chocolate peaks and bubbles, natural daylight from side, 45-degree angle, white marble background, professional dessert styling, high resolution 2048x2048px
```

**Description** : Mousse au chocolat aérienne dans verrine transparente, texture légère volumineuse  
**Attends confirmation puis passe à Image 4**

---

### Image 4 : mousse-chocolat-aerienne-final.png

**Prompt DALL-E 3** :
```
Minimalist food photography, chocolate mousse in elegant glass cup, topped with chocolate shavings and cocoa powder, natural lighting from window, white background, professional dessert presentation, top-down view, high resolution 2048x2048px
```

**Description** : Mousse au chocolat dans coupelle élégante, décor copeaux chocolat  
**Attends confirmation puis passe à Image 5**

---

### Image 5 : panna-cotta-gelification-hero.png

**Prompt DALL-E 3** :
```
Minimalist food photography, panna cotta in white ceramic ramekin, smooth silky texture, vanilla bean pod visible on top, natural daylight from side, 45-degree angle, clean white background, professional styling, high resolution 2048x2048px
```

**Description** : Panna cotta dans ramequin blanc, texture lisse soyeuse, gousse vanille  
**Attends confirmation puis passe à Image 6**

---

### Image 6 : panna-cotta-gelification-final.png

**Prompt DALL-E 3** :
```
Minimalist food photography, panna cotta unmolded on white plate with red berry coulis drizzle, wobbly jelly texture visible, top-down view, natural lighting from window, clean white background, professional dessert presentation, high resolution 2048x2048px
```

**Description** : Panna cotta démoulée sur assiette avec coulis fruits rouges  
**Attends confirmation puis passe à Image 7**

---

### Image 7 : creme-brulee-caramelisee-hero.png

**Prompt DALL-E 3** :
```
Minimalist food photography, creme brulee with caramelized sugar crust being cracked with silver spoon, golden brown caramel layer, creamy custard visible underneath, white ceramic ramekin, natural daylight from side, 45-degree angle, high resolution 2048x2048px
```

**Description** : Crème brûlée avec croûte caramel cassée à la cuillère, crème visible dessous  
**Attends confirmation puis passe à Image 8**

---

### Image 8 : creme-brulee-caramelisee-final.png

**Prompt DALL-E 3** :
```
Minimalist food photography, creme brulee with perfect caramelized sugar top, glossy golden surface, kitchen torch visible in soft focus background, white ramekin on marble surface, natural lighting, top-down view, professional styling, high resolution 2048x2048px
```

**Description** : Crème brûlée avec surface parfaitement caramélisée brillante  
**Attends confirmation - TOUTES LES IMAGES GÉNÉRÉES**

---

## 📋 ÉTAPE FINALE A : CRÉER manifest-sprint5-oeuf-laitages.json

Crée un fichier texte nommé **manifest-sprint5-oeuf-laitages.json** avec ce contenu EXACT :

```json
{
  "batch_id": "sprint5-oeuf-laitages-20251118",
  "created_at": "2025-11-18T18:45:00+01:00",
  "sprint": "Sprint 5",
  "chapter": "Chapitre 5 - Œufs & Laitages",
  "images": [
    {
      "source_file": "oeuf-mollet-parfait-hero.png",
      "target_path": "recettes/oeuf-mollet-parfait/images/hero.png",
      "recipe": "oeuf-mollet-parfait",
      "type": "hero",
      "description": "Œuf mollet coupé en deux, jaune coulant visible"
    },
    {
      "source_file": "oeuf-mollet-parfait-final.png",
      "target_path": "recettes/oeuf-mollet-parfait/images/final.png",
      "recipe": "oeuf-mollet-parfait",
      "type": "final",
      "description": "Œuf mollet dressé sur salade verte"
    },
    {
      "source_file": "mousse-chocolat-aerienne-hero.png",
      "target_path": "recettes/mousse-chocolat-aerienne/images/hero.png",
      "recipe": "mousse-chocolat-aerienne",
      "type": "hero",
      "description": "Mousse au chocolat aérienne dans verrine"
    },
    {
      "source_file": "mousse-chocolat-aerienne-final.png",
      "target_path": "recettes/mousse-chocolat-aerienne/images/final.png",
      "recipe": "mousse-chocolat-aerienne",
      "type": "final",
      "description": "Mousse au chocolat avec copeaux chocolat"
    },
    {
      "source_file": "panna-cotta-gelification-hero.png",
      "target_path": "recettes/panna-cotta-gelification/images/hero.png",
      "recipe": "panna-cotta-gelification",
      "type": "hero",
      "description": "Panna cotta dans ramequin blanc, texture lisse"
    },
    {
      "source_file": "panna-cotta-gelification-final.png",
      "target_path": "recettes/panna-cotta-gelification/images/final.png",
      "recipe": "panna-cotta-gelification",
      "type": "final",
      "description": "Panna cotta démoulée avec coulis fruits rouges"
    },
    {
      "source_file": "creme-brulee-caramelisee-hero.png",
      "target_path": "recettes/creme-brulee-caramelisee/images/hero.png",
      "recipe": "creme-brulee-caramelisee",
      "type": "hero",
      "description": "Crème brûlée avec croûte caramel cassée"
    },
    {
      "source_file": "creme-brulee-caramelisee-final.png",
      "target_path": "recettes/creme-brulee-caramelisee/images/final.png",
      "recipe": "creme-brulee-caramelisee",
      "type": "final",
      "description": "Crème brûlée surface parfaitement caramélisée"
    }
  ],
  "status": "pending",
  "total_images": 8,
  "style": "Minimaliste scientifique, lumière naturelle douce, fond neutre",
  "resolution": "2048x2048px minimum",
  "format": "PNG"
}
```

---

## 📦 ÉTAPE FINALE B : CRÉER LE ZIP

### ⚠️ RÈGLE ABSOLUE : TOUS LES FICHIERS À LA RACINE DU ZIP

**Le ZIP doit contenir UNIQUEMENT les fichiers, SANS aucun dossier ou hiérarchie.**

**Le ZIP final doit contenir le fichier manifest ET TOUTES LES 8 IMAGES générées. Vérifie que chaque fichier est bien présent dans le ZIP.**

### Code Python à exécuter

```python
import zipfile

# Liste des 9 fichiers à zipper (1 manifest + 8 images)
files_to_zip = [
    'manifest-sprint5-oeuf-laitages.json',
    'oeuf-mollet-parfait-hero.png',
    'oeuf-mollet-parfait-final.png',
    'mousse-chocolat-aerienne-hero.png',
    'mousse-chocolat-aerienne-final.png',
    'panna-cotta-gelification-hero.png',
    'panna-cotta-gelification-final.png',
    'creme-brulee-caramelisee-hero.png',
    'creme-brulee-caramelisee-final.png'
]

# Création du ZIP avec fichiers à plat (pas de dossier)
with zipfile.ZipFile('images-sprint5-oeuf-laitages.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        # arcname=file garantit : fichier directement à la racine, pas de chemin parent
        zipf.write(file, arcname=file)

print("✅ ZIP créé : images-sprint5-oeuf-laitages.zip")
print(f"📊 Contient {len(files_to_zip)} fichiers (1 manifest + 8 images PNG)")
```

### Vérification OBLIGATOIRE avant livraison

```python
import zipfile

with zipfile.ZipFile('images-sprint5-oeuf-laitages.zip', 'r') as zipf:
    print("📋 Contenu du ZIP :")
    for name in zipf.namelist():
        print(f"  - {name}")
        # Vérifie qu'il n'y a PAS de "/" dans le nom (= pas de dossier)
        if "/" in name:
            print(f"❌ ERREUR : {name} contient un chemin (dossier détecté) !")
            raise ValueError("Le ZIP ne doit contenir QUE des fichiers à la racine")
    
    print(f"\n✅ VALIDATION OK : {len(zipf.namelist())} fichiers à plat (sans dossier)")
    print(f"📊 Détail : 1 manifest JSON + {len(zipf.namelist())-1} images PNG")
```

**Résultat attendu** :
```
📋 Contenu du ZIP :
  - manifest-sprint5-oeuf-laitages.json
  - oeuf-mollet-parfait-hero.png
  - oeuf-mollet-parfait-final.png
  - mousse-chocolat-aerienne-hero.png
  - mousse-chocolat-aerienne-final.png
  - panna-cotta-gelification-hero.png
  - panna-cotta-gelification-final.png
  - creme-brulee-caramelisee-hero.png
  - creme-brulee-caramelisee-final.png

✅ VALIDATION OK : 9 fichiers à plat (sans dossier)
📊 Détail : 1 manifest JSON + 8 images PNG
```

### ✅ STRUCTURE CORRECTE DU ZIP

```
images-sprint5-oeuf-laitages.zip/
├── manifest-sprint5-oeuf-laitages.json     ← ✅ Directement à la racine
├── oeuf-mollet-parfait-hero.png            ← ✅ Directement à la racine
├── oeuf-mollet-parfait-final.png           ← ✅ Directement à la racine
├── mousse-chocolat-aerienne-hero.png       ← ✅ Directement à la racine
├── mousse-chocolat-aerienne-final.png      ← ✅ Directement à la racine
├── panna-cotta-gelification-hero.png       ← ✅ Directement à la racine
├── panna-cotta-gelification-final.png      ← ✅ Directement à la racine
├── creme-brulee-caramelisee-hero.png       ← ✅ Directement à la racine
└── creme-brulee-caramelisee-final.png      ← ✅ Directement à la racine
```

---

## ✅ LIVRABLE FINAL

Fournis-moi **UN SEUL FICHIER** : **images-sprint5-oeuf-laitages.zip**

Ce ZIP contient :
- Le fichier manifest-sprint5-oeuf-laitages.json
- Les 8 images PNG générées avec DALL-E 3
- **TOUS les 9 fichiers directement à la racine (pas de sous-dossier)**

---

## 📝 CHECKLIST AVANT LIVRAISON

- [ ] Les 8 images générées UNE PAR UNE avec DALL-E 3
- [ ] Noms de fichiers respectés exactement (oeuf-mollet-parfait-hero.png, etc.)
- [ ] Résolution minimum 2048x2048px pour chaque image
- [ ] Style minimaliste scientifique respecté (lumière naturelle, fond neutre)
- [ ] manifest-sprint5-oeuf-laitages.json créé avec le contenu exact ci-dessus
- [ ] ZIP créé avec le code Python fourni ci-dessus
- [ ] Vérification ZIP exécutée : aucun "/" dans les noms de fichiers
- [ ] Structure du ZIP validée : 9 fichiers à plat (1 JSON + 8 PNG)
- [ ] Le ZIP contient TOUTES LES 8 IMAGES + le manifest

**Confirme-moi quand le ZIP est prêt à télécharger avec la sortie de la vérification !**

---

## 📚 Références

- **Charte visuelle complète** : `sources/charte-visuelle.md`
- **Brief images détaillé** : `recettes/Sprint5-briefs-images-IA.md`
- **Issue suivi Sprint 5** : #19
- **Repository** : https://github.com/stefm78/livre01-science-culinaire

---

**Créé le** : 18 novembre 2025  
**Batch ID** : sprint5-oeuf-laitages-20251118  
**Statut** : ⏳ En attente de génération