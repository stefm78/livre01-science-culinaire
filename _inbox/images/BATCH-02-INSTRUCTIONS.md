# BATCH 2 - GÉNÉRATION IMAGES IA
# Instructions complètes pour ChatGPT

Tu vas générer 4 images pour un livre de cuisine scientifique, puis créer un manifest JSON et un ZIP automatisé.

## 🎯 TA MISSION

Génère les 4 images ci-dessous **UNE PAR UNE**, puis crée le manifest.json et le ZIP final.

---

## 📸 IMAGE 1 : bouillon-final.png

**Prompt** :
```
45-degree angle presentation of a chicken broth served in an elegant white bowl, with a sprig of parsley, fine droplets of fat glistening, side focus, bright table, rustic bread slices in background, professional chef plating, natural lighting, photorealistic, 4K
```

**Attends confirmation puis passe à Image 2**

---

## 📸 IMAGE 2 : steak-final.png

**Prompt** :
```
Professional plating of sliced beef steak showing perfect medium-rare interior with pink center and golden Maillard crust, natural resting juices visible on pristine white plate, 45-degree angle, soft natural lighting, shallow depth of field focusing on meat texture, minimalist elegant presentation, high-end restaurant quality, photorealistic, 4K
```

**Attends confirmation puis passe à Image 3**

---

## 📸 IMAGE 3 : steak-process-01.png

**Prompt** :
```
Close-up action shot of beef steak searing in hot cast iron pan, golden Maillard crust visibly forming on surface, light steam rising, 45-degree angle, dramatic warm lighting from above, professional kitchen photography, photorealistic texture, high contrast, sharp focus on crust formation
```

**Attends confirmation puis passe à Image 4**

---

## 📸 IMAGE 4 : steak-process-02.png

**Prompt** :
```
Action shot of chef's hand basting beef steak with foaming golden butter using a spoon, fresh thyme and garlic clove visible in pan, butter bubbles catching light, 45-degree angle, warm dramatic lighting, professional culinary photography, motion blur on butter stream, photorealistic, shallow depth of field
```

---

## 📋 ÉTAPE 5 : CRÉER MANIFEST.JSON

Crée un fichier texte nommé **manifest.json** avec ce contenu EXACT (copie-colle) :

```json
{
  "batch_id": "batch2-20251111",
  "created_at": "2025-11-11T19:55:00Z",
  "images": [
    {
      "source_file": "bouillon-final.png",
      "target_path": "recettes/bouillon-volaille-umami/images/final.png",
      "recipe": "bouillon-volaille-umami",
      "type": "final"
    },
    {
      "source_file": "steak-final.png",
      "target_path": "recettes/steak-maillard/images/final.png",
      "recipe": "steak-maillard",
      "type": "final"
    },
    {
      "source_file": "steak-process-01.png",
      "target_path": "recettes/steak-maillard/images/process-01.png",
      "recipe": "steak-maillard",
      "type": "process"
    },
    {
      "source_file": "steak-process-02.png",
      "target_path": "recettes/steak-maillard/images/process-02.png",
      "recipe": "steak-maillard",
      "type": "process"
    }
  ],
  "status": "pending",
  "total_images": 4
}
```

---

## 📦 ÉTAPE 6 : CRÉER LE ZIP

Crée un fichier ZIP nommé **images-batch2.zip** contenant exactement ces 5 fichiers (à plat, pas de sous-dossier) :

1. manifest.json
2. bouillon-final.png
3. steak-final.png
4. steak-process-01.png
5. steak-process-02.png

**Structure du ZIP** :
```
images-batch2.zip/
├── manifest.json
├── bouillon-final.png
├── steak-final.png
├── steak-process-01.png
└── steak-process-02.png
```

---

## ✅ LIVRABLE FINAL

Fournis-moi le fichier **images-batch2.zip** à télécharger.

---

## 📝 CHECKLIST

- [ ] 4 images générées avec les prompts exacts
- [ ] Noms de fichiers respectés (bouillon-final.png, steak-final.png, etc.)
- [ ] manifest.json créé avec le contenu exact ci-dessus
- [ ] ZIP créé avec les 5 fichiers à plat (pas de sous-dossier)
- [ ] ZIP nommé images-batch2.zip

**Confirme-moi quand le ZIP est prêt à télécharger !**
