#!/usr/bin/env python3
"""
Script universel pour committer des images dans le repository
Utilisable par toute IA avec accès GitHub API
Conserve les URLs sources pour traçabilité
"""

import requests
import json
import sys
from pathlib import Path

def load_image_manifest():
    """Charge le manifeste des images à committer"""
    try:
        with open('tools/images-to-commit.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Fichier images-to-commit.json introuvable")
        sys.exit(1)

def download_image(url):
    """Télécharge une image et retourne son contenu"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"❌ Erreur téléchargement: {e}")
        return None

def main():
    print("🚀 Commit Images Script - Version 1.0")
    print("=" * 50)
    
    # Charge le manifeste
    manifest = load_image_manifest()
    
    if not manifest.get('images'):
        print("⚠️ Aucune image à committer")
        return
    
    print(f"📋 {len(manifest['images'])} image(s) à traiter")
    print()
    
    results = []
    
    for img in manifest['images']:
        filename = img['filename']
        url = img['url']
        destination = img.get('destination', 'sources/images')
        issue_ref = img.get('issue', 'N/A')
        
        print(f"⏳ Traitement: {filename}")
        print(f"   Source: {url[:60]}...")
        print(f"   Issue: #{issue_ref}")
        
        # Téléchargement
        content = download_image(url)
        if not content:
            print(f"❌ Échec téléchargement {filename}")
            print()
            continue
        
        # Sauvegarde locale
        local_path = Path(destination) / filename
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(content)
        
        print(f"✅ {filename} téléchargé ({len(content)} bytes)")
        
        results.append({
            'filename': filename,
            'path': f"{destination}/{filename}",
            'size': len(content),
            'source_url': url,
            'issue': issue_ref,
            'status': 'ready'
        })
        print()
    
    # Génère rapport
    print("=" * 50)
    print("📊 RÉSUMÉ")
    print(f"✅ {len(results)} image(s) prête(s) pour commit Git")
    print()
    print("📝 Commandes Git:")
    print("   git add sources/images/")
    print(f"   git commit -m '🎨 Ajout {len(results)} maquettes (Issue #{manifest.get('issue_number', 'N/A')})'")
    print("   git push")
    print()
    
    # Traçabilité
    trace_file = Path('tools/images-committed.json')
    trace_data = {
        'commit_date': manifest.get('date'),
        'issue': manifest.get('issue_number'),
        'persona': manifest.get('persona'),
        'images': results
    }
    
    trace_file.write_text(json.dumps(trace_data, indent=2))
    print(f"📋 Traçabilité: {trace_file}")

if __name__ == "__main__":
    main()
