#!/usr/bin/env python3
"""
Script de téléchargement et commit d'images depuis URLs externes
Lit tools/images-to-commit.json et commit dans Git
"""
import json
import os
import sys
import subprocess
import requests
from pathlib import Path
from collections import defaultdict

def main():
    print("🚀 Commit Images Script - Version 1.0")
    print("="*50)
    
    # Charger la config
    config_path = Path('tools/images-to-commit.json')
    if not config_path.exists():
        print("❌ Fichier tools/images-to-commit.json introuvable")
        sys.exit(1)
    
    with open(config_path) as f:
        manifest = json.load(f)
    
    images = manifest.get('images', [])
    print(f"📋 {len(images)} image(s) à traiter\n")
    
    # Grouper par destination
    by_destination = defaultdict(list)
    results = []
    
    for img in images:
        filename = img['filename']
        url = img['url']
        destination = img.get('destination', 'sources/images')
        
        print(f"⏳ Traitement: {filename}")
        print(f"   Source: {url[:60]}...")
        print(f"   Destination: {destination}")
        
        try:
            # Télécharger
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Créer le dossier de destination
            dest_path = Path(destination)
            dest_path.mkdir(parents=True, exist_ok=True)
            
            # Sauvegarder
            file_path = dest_path / filename
            file_path.write_bytes(response.content)
            
            print(f"✅ {filename} téléchargé ({len(response.content)} bytes)")
            
            by_destination[destination].append({
                'filename': filename,
                'size': len(response.content),
                'url': url
            })
            results.append({
                'filename': filename,
                'destination': destination,
                'size': len(response.content)
            })
            
        except Exception as e:
            print(f"❌ Erreur: {e}")
        
        print()
    
    if not results:
        print("⚠️ Aucune image téléchargée")
        sys.exit(1)
    
    # Sauvegarder traçabilité
    trace_path = Path('tools/images-committed.json')
    trace_path.write_text(json.dumps({
        'issue_number': manifest.get('issue_number'),
        'images': results,
        'destinations': list(by_destination.keys())
    }, indent=2))
    
    print("="*50)
    print("📊 RÉSUMÉ")
    print(f"✅ {len(results)} image(s) prête(s) pour commit Git\n")
    
    # Git commit
    issue_num = manifest.get('issue_number', 'N/A')
    commit_and_push(by_destination, len(results), issue_num)

def commit_and_push(by_destination, img_count, issue_num):
    """Commit et push des images téléchargées"""
    
    # Config Git
    subprocess.run(['git', 'config', '--local', 'user.email', 'github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', 'config', '--local', 'user.name', 'github-actions[bot]'], check=True)
    
    # Git add par destination
    for dest in sorted(by_destination.keys()):
        count = len(by_destination[dest])
        print(f"📁 git add {dest}/ ({count} image(s))")
        subprocess.run(['git', 'add', f'{dest}/'], check=False)
    
    # Add traçabilité
    subprocess.run(['git', 'add', 'tools/images-committed.json'], check=False)
    
    # Vérifier s'il y a des changements
    result = subprocess.run(['git', 'diff', '--staged', '--name-only'], capture_output=True, text=True)
    if not result.stdout.strip():
        print("⚠️ Aucun changement à committer")
        return
    
    # Commit
    commit_msg = f"🎨 Ajout {img_count} images (Issue #{issue_num})"
    print(f"\n💾 Commit: {commit_msg}")
    subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
    
    # Pull rebase
    subprocess.run(['git', 'pull', '--rebase', '--autostash', 'origin', 'main'], check=True)
    
    # Push
    subprocess.run(['git', 'push'], check=True)
    
    print(f"✅ {img_count} images commitées avec succès")

if __name__ == '__main__':
    main()
