# BATCH {{BATCH_ID}} - GÉNÉRATION IMAGES IA
# Template d'instructions pour ChatGPT ou toute IA de génération d'images

⚠️ **AVANT DE COMMENCER** : Remplace `{{BATCH_ID}}` par le numéro de batch (ex: batch3, batch4, etc.)

---

## 🎯 TA MISSION

Génère les images ci-dessous **UNE PAR UNE**, puis crée le manifest JSON et le ZIP.

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

## 📋 ÉTAPE FINALE A : CRÉER manifest-{{BATCH_ID}}.json

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

## 📦 ÉTAPE FINALE B : CRÉER LE ZIP

### ⚠️ RÈGLE ABSOLUE : TOUS LES FICHIERS À LA RACINE DU ZIP

**Le ZIP doit contenir UNIQUEMENT les fichiers, SANS aucun dossier ou hiérarchie.**

**Important : Le ZIP final doit contenir non seulement le fichier manifest, mais aussi TOUTES LES IMAGES générées pour le batch. Vérifie que chaque fichier image et le manifest est bien présent dans le ZIP (pas uniquement le manifest).**

### Code Python à exécuter

```python
import zipfile

# Liste des fichiers à zipper (adapte selon ton batch)
files_to_zip = [
    'manifest-{{BATCH_ID}}.json',
    '{{recette1}}-{{type1}}.png',
    '{{recette2}}-{{type2}}.png',
    # Ajoute tous les autres fichiers ici
]

# Création du ZIP avec fichiers à plat (pas de dossier)
with zipfile.ZipFile('images-{{BATCH_ID}}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        # arcname=file garantit : fichier directement à la racine, pas de chemin parent
        zipf.write(file, arcname=file)

print("✅ ZIP créé : images-{{BATCH_ID}}.zip")
```

### Vérification OBLIGATOIRE avant livraison

Exécute ce code pour vérifier la structure du ZIP :

```python
import zipfile

with zipfile.ZipFile('images-{{BATCH_ID}}.zip', 'r') as zipf:
    print("📋 Contenu du ZIP :")
    for name in zipf.namelist():
        print(f"  - {name}")
        # Vérifie qu'il n'y a PAS de "/" dans le nom (= pas de dossier)
        if "/" in name:
            print(f"❌ ERREUR : {name} contient un chemin (dossier détecté) !")
            raise ValueError("Le ZIP ne doit contenir QUE des fichiers à la racine")
    
    print(f"\n✅ VALIDATION OK : {len(zipf.namelist())} fichiers à plat (sans dossier)")
```

**Résultat attendu** :
```
📋 Contenu du ZIP :
  - manifest-{{BATCH_ID}}.json
  - {{recette1}}-{{type1}}.png
  - {{recette2}}-{{type2}}.png

✅ VALIDATION OK : 3 fichiers à plat (sans dossier)
```

### ❌ STRUCTURE INTERDITE

```
images-{{BATCH_ID}}.zip/
└── images/                    ← ❌ PAS DE DOSSIER INTERMÉDIAIRE
    ├── manifest.json
    ├── recette1-type1.png
    └── ...

OU

images-{{BATCH_ID}}.zip/
└── {{BATCH_ID}}/              ← ❌ PAS DE DOSSIER INTERMÉDIAIRE
    ├── manifest.json
    └── ...
```

### ✅ STRUCTURE CORRECTE

```
images-{{BATCH_ID}}.zip/
├── manifest-{{BATCH_ID}}.json     ← ✅ Directement à la racine
├── {{recette1}}-{{type1}}.png     ← ✅ Directement à la racine
├── {{recette2}}-{{type2}}.png     ← ✅ Directement à la racine
└── ...
```

---

## ✅ LIVRABLE FINAL

Fournis-moi **UN SEUL FICHIER** : **images-{{BATCH_ID}}.zip**

Ce ZIP contient :
- Le fichier manifest-{{BATCH_ID}}.json
- Toutes les images PNG
- **TOUS les fichiers directement à la racine (pas de sous-dossier)**

---

## 📝 CHECKLIST AVANT LIVRAISON

- [ ] Toutes les images générées avec les prompts exacts
- [ ] Noms de fichiers respectés ({{recette}}-{{type}}.png)
- [ ] manifest-{{BATCH_ID}}.json créé avec le contenu exact
- [ ] Tous les paramètres {{BATCH_ID}}, {{DATE}}, etc. remplacés
- [ ] **Maximum 10-12 images par batch** (sinon diviser en plusieurs batchs)
- [ ] **ZIP créé avec code Python fourni ci-dessus**
- [ ] **Vérification ZIP exécutée : aucun "/" dans les noms de fichiers**
- [ ] **Structure du ZIP validée : fichiers à plat, pas de dossier**
- [ ] **Le ZIP doit contenir TOUTES LES IMAGES générées ET le manifest, pas uniquement le manifest !**

**Confirme-moi quand le ZIP est prêt à télécharger avec la sortie de la vérification !**
