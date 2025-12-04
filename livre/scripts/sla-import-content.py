#!/usr/bin/env python3
"""
Extraction contenu Markdown pour import Scribus
Usage: python livre/scripts/sla-import-content.py recettes/steak-maillard/recette.md
"""

import re
from pathlib import Path
import sys
import argparse


class MarkdownParser:
    def __init__(self, md_path):
        self.md_path = Path(md_path)
        self.content = self.md_path.read_text(encoding='utf-8')
        self.sections = {}
    
    def parse(self):
        # Titre
        title_match = re.search(r'^#\s+(.+)$', self.content, re.MULTILINE)
        if title_match:
            self.sections['title'] = title_match.group(1)
        
        # Science
        science_match = re.search(
            r'##\s+🔬\s+La Science\s+(.+?)(?=\n##|\Z)',
            self.content, re.DOTALL
        )
        if science_match:
            self.sections['science'] = science_match.group(1).strip()
        
        # Ingrédients
        ing_match = re.search(
            r'##\s+📝\s+Ingrédients\s+(.+?)(?=\n##|\Z)',
            self.content, re.DOTALL
        )
        if ing_match:
            self.sections['ingredients'] = re.findall(
                r'^\s*[-*]\s+(.+)$', ing_match.group(1), re.MULTILINE
            )
        
        # Étapes
        steps_match = re.search(
            r'##\s+👨‍🍳\s+Préparation\s+(.+?)(?=\n##|\Z)',
            self.content, re.DOTALL
        )
        if steps_match:
            self.sections['steps'] = re.findall(
                r'^\s*\d+\.\s+(.+)$', steps_match.group(1), re.MULTILINE
            )
        
        return self.sections
    
    def display(self):
        print("\n" + "="*60)
        print("📝 CONTENU EXTRAIT")
        print("="*60)
        print(f"📁 {self.md_path.name}")
        print()
        
        if 'title' in self.sections:
            print(f"🎯 TITRE : {self.sections['title']}")
            print()
        
        if 'science' in self.sections:
            print("🔬 SCIENCE :")
            preview = self.sections['science'][:150]
            print(f"  {preview}...")
            print()
        
        if 'ingredients' in self.sections:
            print(f"📝 INGRÉDIENTS ({len(self.sections['ingredients'])}) :")
            for i, ing in enumerate(self.sections['ingredients'][:3], 1):
                print(f"  {i}. {ing}")
            if len(self.sections['ingredients']) > 3:
                print(f"  ... +{len(self.sections['ingredients']) - 3}")
            print()
        
        if 'steps' in self.sections:
            print(f"👨‍🍳 ÉTAPES ({len(self.sections['steps'])}) :")
            for i, step in enumerate(self.sections['steps'][:2], 1):
                preview = step[:70]
                print(f"  {i}. {preview}...")
            if len(self.sections['steps']) > 2:
                print(f"  ... +{len(self.sections['steps']) - 2}")
        
        print("\n" + "="*60)
        print("💡 Copier-coller dans Scribus")
        print("="*60)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('md_file', help='Fichier recette.md')
    args = parser.parse_args()
    
    md_file = Path(args.md_file)
    if not md_file.exists():
        print(f"❌ Fichier introuvable : {md_file}")
        sys.exit(1)
    
    try:
        parser = MarkdownParser(md_file)
        parser.parse()
        parser.display()
    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
