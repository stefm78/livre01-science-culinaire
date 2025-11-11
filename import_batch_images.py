#!/usr/bin/env python3
"""
Script d'import automatique des batchs d'images IA depuis _inbox/images/
Lit les manifests, déplace les images vers les dossiers recettes, archive les manifests
"""

import os
import json
import glob
import shutil
from datetime import datetime

BATCH_DIR = "_inbox/images"

def process_batch():
    """Traite tous les manifests en attente dans _inbox/images/"""
    
    # Trouver tous les fichiers manifest-*.json (non processed)
    manifest_files = glob.glob(os.path.join(BATCH_DIR, "manifest-*.json"))
    
    if not manifest_files:
        print("ℹ️  Aucun manifest en attente de traitement")
        return
    
    for manifest_path in manifest_files:
        # Skip si déjà processed
        if "-processed.json" in manifest_path:
            continue
            
        print(f"\n{'='*60}")
        print(f"📦 Traitement : {os.path.basename(manifest_path)}")
        print(f"{'='*60}")
        
        # Lire le manifest
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        
        batch_id = manifest.get("batch_id", "unknown")
        images = manifest.get("images", [])
        
        print(f"🆔 Batch ID: {batch_id}")
        print(f"📸 Nombre d'images: {len(images)}\n")
        
        # Traiter chaque image
        success_count = 0
        for img in images:
            source_file = img["source_file"]
            target_path = img["target_path"]
            recipe = img.get("recipe", "unknown")
            img_type = img.get("type", "unknown")
            
            src = os.path.join(BATCH_DIR, source_file)
            
            # Vérifier que le fichier source existe
            if not os.path.exists(src):
                print(f"⚠️  {source_file} introuvable, skip")
                continue
            
            # Créer le dossier cible si nécessaire
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Supprimer l'ancien fichier si existe
            if os.path.exists(target_path):
                os.remove(target_path)
                print(f"🗑️  Ancien {target_path} supprimé")
            
            # Déplacer la nouvelle image
            shutil.move(src, target_path)
            print(f"✅ {source_file} → {target_path}")
            success_count += 1
        
        # Mettre à jour et archiver le manifest
        manifest["status"] = "processed"
        manifest["processed_at"] = datetime.now().isoformat()
        manifest["processed_count"] = success_count
        
        # Créer le nom d'archive
        archive_name = f"manifest-{batch_id}-processed.json"
        archive_path = os.path.join(BATCH_DIR, archive_name)
        
        # Sauvegarder le manifest archivé
        with open(archive_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        # Supprimer le manifest original
        os.remove(manifest_path)
        
        print(f"\n✔️  Batch {batch_id} traité avec succès")
        print(f"📋 Manifest archivé : {archive_name}")
        print(f"📊 Images traitées : {success_count}/{len(images)}")

if __name__ == "__main__":
    print("\n🚀 IMPORT BATCH IMAGES IA\n")
    process_batch()
    print("\n✅ Traitement terminé\n")
