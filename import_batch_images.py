#!/usr/bin/env python3
"""
Script d'import automatique des batchs d'images IA depuis _inbox/images/
Lit le premier manifest JSON trouvé (nom arbitraire), déplace les images, archive le manifest
"""
import os
import json
import glob
import shutil
from datetime import datetime

BATCH_DIR = "_inbox/images"

def process_batch():
    """Traite le premier manifest JSON présent dans _inbox/images/ (nom libre)"""
    manifest_files = [f for f in glob.glob(os.path.join(BATCH_DIR, "*.json")) if not f.endswith("-processed.json")]
    if not manifest_files:
        print("ℹ️  Aucun manifest en attente de traitement")
        return
    # Prend le premier (seul manifest standard par batch)
    manifest_path = manifest_files[0]
    print(f"\n{'='*60}")
    print(f"📦 Traitement : {os.path.basename(manifest_path)}")
    print(f"{'='*60}")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    batch_id = manifest.get("batch_id", "unknown")
    images = manifest.get("images", [])
    print(f"🆔 Batch ID: {batch_id}")
    print(f"📸 Nombre d'images: {len(images)}\n")
    success_count = 0
    for img in images:
        source_file = img["source_file"]
        target_path = img["target_path"]
        recipe = img.get("recipe", "unknown")
        img_type = img.get("type", "unknown")
        src = os.path.join(BATCH_DIR, source_file)
        if not os.path.exists(src):
            print(f"⚠️  {source_file} introuvable, skip")
            continue
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        if os.path.exists(target_path):
            os.remove(target_path)
            print(f"🗑️  Ancien {target_path} supprimé")
        shutil.move(src, target_path)
        print(f"✅ {source_file} → {target_path}")
        success_count += 1
    manifest["status"] = "processed"
    manifest["processed_at"] = datetime.now().isoformat()
    manifest["processed_count"] = success_count
    archive_name = f"manifest-{batch_id}-processed.json"
    archive_path = os.path.join(BATCH_DIR, archive_name)
    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    os.remove(manifest_path)
    print(f"\n✔️  Batch {batch_id} traité avec succès")
    print(f"📋 Manifest archivé : {archive_name}")
    print(f"📊 Images traitées : {success_count}/{len(images)}")

if __name__ == "__main__":
    print("\n🚀 IMPORT BATCH IMAGES IA\n")
    process_batch()
    print("\n✅ Traitement terminé\n")
