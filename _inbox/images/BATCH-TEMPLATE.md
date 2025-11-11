# BATCH {{BATCH_ID}} - GÉNÉRATION IMAGES IA
# Template d'instructions pour ChatGPT ou toute IA de génération d'images

⚠️ **AVANT DE COMMENCER** : Remplace `{{BATCH_ID}}` par le numéro de batch (ex: batch3, batch4, etc.)

---

## 🎯 TA MISSION

Génère les images ci-dessous **UNE PAR UNE**, puis crée le manifest JSON.

**IMPORTANT : Limite de 10-12 images par batch maximum** pour garantir qualité et traçabilité.

---

## 📸 IMAGES À GÉNÉRER

### Image 1 : {{recette1}}-{{type1}}.png

**Prompt** :
```
[INSÈRE ICI LE PROMPT DALL-E POUR CETTE IMAGE]
```

**Attends confirmation puis passe à Image 2**

---

### Image 2 : {{recette2}}-{{type2}}.png

**Prompt** :
```
[INSÈRE ICI LE PROMPT DALL-E POUR CETTE IMAGE]
```

**Attends confirmation puis continue...**

---

## 📋 ÉTAPE FINALE : CRÉER manifest-{{BATCH_ID}}.json

Crée un fichier texte nommé **manifest-{{BATCH_ID}}.json** avec ce contenu EXACT :

```json
{
  "batch_id": "{{BATCH_ID}}-{{DATE}}",
  "created_at": "{{DATE_ISO}}",
  "images": [
    {
      "source_file": "{{recette1}}-{{type1}}.png",
      "target_path": "recettes/{{recette1}}/images/{{type1}}.png",
      "recipe": "{{recette1}}",
      "type": "{{type1}}"
    },
    {
      "source_file": "{{recette2}}-{{type2}}.png",
      "target_path": "recettes/{{recette2}}/images/{{type2}}.png",
      "recipe": "{{recette2}}",
      "type": "{{type2}}"
    }
  ],
  "status": "pending",
  "total_images": 2
}
```

---

## ✅ LIVRABLE FINAL

Fournis-moi :
1. Toutes les images générées (fichiers PNG individuels)
2. Le fichier manifest-{{BATCH_ID}}.json

Je me charge ensuite de les uploader dans le repo GitHub.

---

## 📝 CHECKLIST

- [ ] Toutes les images générées avec les prompts exacts
- [ ] Noms de fichiers respectés ({{recette}}-{{type}}.png)
- [ ] manifest-{{BATCH_ID}}.json créé avec le contenu exact
- [ ] Tous les paramètres {{BATCH_ID}}, {{DATE}}, etc. remplacés
- [ ] **Maximum 10-12 images par batch** (sinon diviser en plusieurs batchs)

**Confirme-moi quand tout est prêt à télécharger !**
