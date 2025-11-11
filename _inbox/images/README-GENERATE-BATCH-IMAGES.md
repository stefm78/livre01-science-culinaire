# 🖼️ Comment générer un batch d'images IA pour ce projet

## Instructions IA universelle

Quand une IA reçoit la consigne "Donne-moi les batchs de création d'images", elle doit :

1. Parcourir le dossier `recettes/` et lire chaque `images/README.md` pour lister toutes les images attendues (nom + prompt associé)
2. Regrouper les images par batch de 12 maximum
3. Pour chaque batch, générer un fichier `.md` structuré ainsi :

---

## Exemple : BATCH-01-IMAGES.md

```
# Batch 01 - Création images IA

## Recettes concernées :
- bouillon-volaille-umami
- steak-maillard

## Images à générer :
1. Recette : bouillon-volaille-umami  
   Nom fichier : bouillon-hero.png  
   Prompt : [copier prompt section HERO du README.md de la recette]
2. Recette : bouillon-volaille-umami  
   Nom fichier : final.png  
   Prompt : [copier prompt section FINAL]
3. Recette : steak-maillard  
   Nom fichier : steak-hero.png  
   Prompt : [copier prompt section HERO]
4. Recette : steak-maillard  
   Nom fichier : final.png  
   Prompt : [copier prompt section FINAL]
...

---

## À fournir après génération d'un batch (commit humain ou IA) :
- Les .png
- 1 fichier manifest.json (voir modèle ci-dessous)

```
{
  "batch_id": "batch01-20251112",
  "created_at": "2025-11-12T09:30:00Z",
  "images": [
    {
      "source_file": "bouillon-hero.png",
      "target_path": "recettes/bouillon-volaille-umami/images/bouillon-hero.png",
      "recipe": "bouillon-volaille-umami",
      "type": "hero"
    },
    // ...
  ],
  "status": "pending",
  "total_images": 8
}
```

- Zipper le tout et uploader dans `_inbox/images/`

---

## Checklist batch
- [ ] Maximum 12 images par batch
- [ ] Prompts DALL-E exacts copiés
- [ ] manifest.json bien structuré
- [ ] Noms de fichiers respectés
- [ ] PNG vérifiés (non vides)

---

Quand tout est prêt, tu peux demander : 
> Donne-moi pour chaque batch le fichier markdown détaillé pour la génération images IA avec prompts et checklist.

Et l'IA doit suivre ce format à la lettre.

---

*(Fichier à placer à la racine du projet ou dans _inbox/images/ : `README-GENERATE-BATCH-IMAGES.md`)*
