#!/usr/bin/env python3
"""
Script de validation d'une recette

Usage:
    python scripts/validate-recipe.py recettes/nom-recette

Vérifie:
- Présence fichiers obligatoires (recette.md, metadata.json)
- Validité JSON metadata.json
- Présence images référencées
- Champs obligatoires metadata
- Conformité format recette.md
"""

import json
import sys
from pathlib import Path


class Colors:
    """Couleurs ANSI pour terminal"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.RESET}")


def print_error(msg):
    print(f"{Colors.RED}✗ {msg}{Colors.RESET}")


def print_warning(msg):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.RESET}")


def print_info(msg):
    print(f"{Colors.BLUE}ℹ {msg}{Colors.RESET}")


def validate_recipe(recipe_dir):
    """
    Valide une recette complète
    
    Args:
        recipe_dir: Path vers le dossier recette
    
    Returns:
        bool: True si valide, False sinon
    """
    recipe_path = Path(recipe_dir)
    
    if not recipe_path.exists():
        print_error(f"Le dossier {recipe_dir} n'existe pas")
        return False
    
    if not recipe_path.is_dir():
        print_error(f"{recipe_dir} n'est pas un dossier")
        return False
    
    print_info(f"Validation de la recette : {recipe_path.name}")
    print()
    
    errors = []
    warnings = []
    
    # Vérification fichiers obligatoires
    print("1. Vérification fichiers obligatoires...")
    
    recette_md = recipe_path / "recette.md"
    metadata_json = recipe_path / "metadata.json"
    images_dir = recipe_path / "images"
    
    if not recette_md.exists():
        errors.append("recette.md manquant")
        print_error("  recette.md manquant")
    else:
        print_success("  recette.md présent")
    
    if not metadata_json.exists():
        errors.append("metadata.json manquant")
        print_error("  metadata.json manquant")
    else:
        print_success("  metadata.json présent")
    
    if not images_dir.exists():
        warnings.append("Dossier images/ manquant")
        print_warning("  images/ manquant")
    else:
        print_success("  images/ présent")
    
    print()
    
    # Validation JSON
    if metadata_json.exists():
        print("2. Validation metadata.json...")
        
        try:
            with open(metadata_json, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            print_success("  JSON valide")
            
            # Vérification champs obligatoires
            required_fields = {
                'recette': ['id', 'titre', 'chapitre'],
                'science': ['concept_principal'],
                'images': ['hero'],
            }
            
            for section, fields in required_fields.items():
                if section not in metadata:
                    errors.append(f"Section '{section}' manquante dans metadata.json")
                    print_error(f"  Section '{section}' manquante")
                else:
                    for field in fields:
                        if field not in metadata[section]:
                            errors.append(f"Champ '{section}.{field}' manquant")
                            print_error(f"  Champ '{section}.{field}' manquant")
                        else:
                            print_success(f"  Champ '{section}.{field}' présent")
            
            # Vérification images référencées
            if 'images' in metadata and images_dir.exists():
                print()
                print("3. Vérification images référencées...")
                
                images_metadata = metadata['images']
                
                # Hero image (obligatoire)
                if 'hero' in images_metadata:
                    hero_path = recipe_path / images_metadata['hero']['fichier']
                    if not hero_path.exists():
                        errors.append(f"Image hero manquante : {hero_path}")
                        print_error(f"  {hero_path.name} manquante")
                    else:
                        print_success(f"  {hero_path.name} présente")
                
                # Process images (optionnel)
                if 'process' in images_metadata:
                    for idx, process_img in enumerate(images_metadata['process']):
                        process_path = recipe_path / process_img['fichier']
                        if not process_path.exists():
                            warnings.append(f"Image process-{idx+1:02d} manquante : {process_path}")
                            print_warning(f"  {process_path.name} manquante")
                        else:
                            print_success(f"  {process_path.name} présente")
                
                # Final image (obligatoire)
                if 'final' in images_metadata:
                    final_path = recipe_path / images_metadata['final']['fichier']
                    if not final_path.exists():
                        errors.append(f"Image final manquante : {final_path}")
                        print_error(f"  {final_path.name} manquante")
                    else:
                        print_success(f"  {final_path.name} présente")
            
        except json.JSONDecodeError as e:
            errors.append(f"JSON invalide : {e}")
            print_error(f"  Erreur JSON : {e}")
    
    print()
    
    # Validation contenu recette.md
    if recette_md.exists():
        print("4. Validation structure recette.md...")
        
        with open(recette_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifications basiques
        required_sections = [
            '## Page 1 : Présentation + Science',
            '## Page 2 : Recette + Variantes',
            '🔬 **LA SCIENCE**',
            '🌿 **ASSOCIATIONS CLÉS**',
            '🧑‍🍳 **INGRÉDIENTS**',
            '🔥 **PRÉPARATION**',
            '🔄 **VARIANTES**',
            '💡 **ASTUCE SCIENCE**'
        ]
        
        for section in required_sections:
            if section in content:
                print_success(f"  Section '{section}' présente")
            else:
                warnings.append(f"Section '{section}' manquante ou mal formatée")
                print_warning(f"  Section '{section}' manquante")
    
    print()
    print("="*60)
    
    # Résumé
    if errors:
        print_error(f"\n✗ VALIDATION ÉCHOUÉE : {len(errors)} erreur(s)")
        for error in errors:
            print(f"  - {error}")
        success = False
    else:
        print_success("\n✓ VALIDATION RÉUSSIE")
        success = True
    
    if warnings:
        print_warning(f"\n⚠ {len(warnings)} avertissement(s) :")
        for warning in warnings:
            print(f"  - {warning}")
    
    print()
    return success


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate-recipe.py recettes/nom-recette")
        sys.exit(1)
    
    recipe_dir = sys.argv[1]
    success = validate_recipe(recipe_dir)
    
    sys.exit(0 if success else 1)
