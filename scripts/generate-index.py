#!/usr/bin/env python3
"""
Générateur d'index automatique des recettes

Usage:
    python scripts/generate-index.py

Génère:
- recettes/index.json : Index complet JSON
- recettes/INDEX.md : Index lisible Markdown
"""

import json
from pathlib import Path
from datetime import datetime


def generate_index():
    """
    Génère l'index de toutes les recettes
    """
    recettes_dir = Path("recettes")
    
    if not recettes_dir.exists():
        print("❌ Dossier recettes/ inexistant")
        return
    
    recettes = []
    recettes_by_chapter = {}
    
    # Scanner tous les dossiers de recettes
    for recipe_dir in sorted(recettes_dir.iterdir()):
        if not recipe_dir.is_dir():
            continue
        
        # Ignorer les dossiers spéciaux
        if recipe_dir.name.startswith(('_', '.')):
            continue
        
        metadata_path = recipe_dir / "metadata.json"
        
        if not metadata_path.exists():
            print(f"⚠️ {recipe_dir.name} : metadata.json manquant")
            continue
        
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # Extraire infos principales
            recette_data = {
                "id": metadata["recette"]["id"],
                "titre": metadata["recette"]["titre"],
                "slug": metadata["recette"]["slug"],
                "chapitre": metadata["recette"]["chapitre"],
                "numero_chapitre": metadata["recette"].get("numero_chapitre", 0),
                "numero_recette": metadata["recette"].get("numero_recette", 0),
                "difficulte": metadata["recette"]["difficulte"],
                "temps_total": (
                    metadata["recette"].get("temps_preparation", 0) +
                    metadata["recette"].get("temps_cuisson", 0) +
                    metadata["recette"].get("temps_repos", 0)
                ),
                "portions": metadata["recette"]["portions"],
                "concept_scientifique": metadata["science"]["concept_principal"],
                "tags": metadata["recette"]["tags"],
                "hero_image": f"{recipe_dir.name}/{metadata['images']['hero']['fichier']}",
                "statut": metadata.get("statut", "brouillon")
            }
            
            recettes.append(recette_data)
            
            # Grouper par chapitre
            chapitre = recette_data["chapitre"]
            if chapitre not in recettes_by_chapter:
                recettes_by_chapter[chapitre] = []
            recettes_by_chapter[chapitre].append(recette_data)
            
            print(f"✓ {recette_data['titre']}")
            
        except (json.JSONDecodeError, KeyError) as e:
            print(f"❌ {recipe_dir.name} : erreur parsing - {e}")
            continue
    
    # Trier les recettes
    recettes.sort(key=lambda r: (r["numero_chapitre"], r["numero_recette"]))
    
    # Générer index.json
    index_data = {
        "meta": {
            "total_recettes": len(recettes),
            "total_chapitres": len(recettes_by_chapter),
            "date_generation": datetime.now().isoformat(),
            "version": "1.0"
        },
        "recettes": recettes,
        "par_chapitre": recettes_by_chapter
    }
    
    index_json_path = recettes_dir / "index.json"
    with open(index_json_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ index.json généré : {len(recettes)} recettes")
    
    # Générer INDEX.md
    markdown_content = generate_markdown_index(index_data)
    
    index_md_path = recettes_dir / "INDEX.md"
    with open(index_md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✓ INDEX.md généré\n")
    
    # Statistiques
    print("="*60)
    print(f"\n📊 STATISTIQUES\n")
    print(f"Total recettes : {len(recettes)}")
    print(f"Total chapitres : {len(recettes_by_chapter)}")
    print(f"\nPar chapitre :")
    for chapitre, recettes_list in sorted(recettes_by_chapter.items()):
        print(f"  - {chapitre} : {len(recettes_list)} recettes")
    
    # Par difficulté
    by_diff = {1: 0, 2: 0, 3: 0}
    for r in recettes:
        by_diff[r["difficulte"]] += 1
    
    print(f"\nPar difficulté :")
    print(f"  - Facile (●○○) : {by_diff[1]} recettes")
    print(f"  - Intermédiaire (●●○) : {by_diff[2]} recettes")
    print(f"  - Difficile (●●●) : {by_diff[3]} recettes")
    
    print()


def generate_markdown_index(index_data):
    """
    Génère un index Markdown lisible
    """
    md = []
    md.append("# 📖 Index des Recettes\n")
    md.append(f"**Généré le** : {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n")
    md.append(f"**Total** : {index_data['meta']['total_recettes']} recettes en {index_data['meta']['total_chapitres']} chapitres\n")
    md.append("---\n\n")
    
    # Par chapitre
    for chapitre, recettes in sorted(index_data['par_chapitre'].items()):
        md.append(f"## {chapitre}\n\n")
        
        for recette in sorted(recettes, key=lambda r: r['numero_recette']):
            # Difficulté
            diff_icons = {
                1: "●○○",
                2: "●●○",
                3: "●●●"
            }
            diff = diff_icons.get(recette['difficulte'], "○○○")
            
            md.append(f"### {recette['titre']}\n\n")
            md.append(f"- **Concept** : {recette['concept_scientifique']}\n")
            md.append(f"- **Difficulté** : {diff}\n")
            md.append(f"- **Temps total** : {recette['temps_total']} min\n")
            md.append(f"- **Portions** : {recette['portions']} personnes\n")
            md.append(f"- **Tags** : {', '.join(recette['tags'])}\n")
            md.append(f"- **Fichier** : [`{recette['slug']}/`]({recette['slug']}/recette.md)\n")
            md.append(f"- **Statut** : {recette['statut']}\n\n")
    
    md.append("---\n\n")
    md.append("*Index généré automatiquement par `scripts/generate-index.py`*\n")
    
    return "".join(md)


if __name__ == "__main__":
    generate_index()
