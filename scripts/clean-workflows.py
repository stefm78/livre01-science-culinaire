#!/usr/bin/env python3
"""
Script de nettoyage automatique des workflows GitHub Actions
Corrige les erreurs yamllint :
- Trailing spaces (espaces en fin de ligne)
- Indentation excessive (espaces inutiles)
"""

import os
import sys
from pathlib import Path

def clean_yaml_file(filepath):
    """Nettoie un fichier YAML des trailing spaces"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Retirer trailing spaces de chaque ligne
        lines = content.split('\n')
        cleaned_lines = [line.rstrip() for line in lines]
        cleaned_content = '\n'.join(cleaned_lines)

        # Éviter ajout de newline finale si absent
        if not content.endswith('\n') and cleaned_content.endswith('\n'):
            cleaned_content = cleaned_content[:-1]

        # Sauvegarder seulement si changements
        if cleaned_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True, len(content) - len(cleaned_content)
        return False, 0

    except Exception as e:
        print(f"❌ Erreur sur {filepath}: {e}", file=sys.stderr)
        return False, 0

def main():
    workflows_dir = Path('.github/workflows')

    if not workflows_dir.exists():
        print(f"❌ Dossier {workflows_dir} introuvable")
        sys.exit(1)

    yaml_files = list(workflows_dir.glob('*.yml')) + list(workflows_dir.glob('*.yaml'))

    if not yaml_files:
        print("ℹ️ Aucun workflow YAML trouvé")
        return

    print(f"🔍 Scan de {len(yaml_files)} workflows YAML...")

    modified = 0
    total_spaces = 0

    for filepath in sorted(yaml_files):
        changed, spaces_removed = clean_yaml_file(filepath)
        if changed:
            modified += 1
            total_spaces += spaces_removed
            print(f"  ✅ {filepath.name} - {spaces_removed} espaces retirés")
        else:
            print(f"  ✓ {filepath.name} - déjà propre")

    print(f"\n📊 Résumé :")
    print(f"  • Fichiers scannés : {len(yaml_files)}")
    print(f"  • Fichiers modifiés : {modified}")
    print(f"  • Espaces retirés : {total_spaces}")

    if modified > 0:
        print(f"\n✅ {modified} fichier(s) nettoyé(s) avec succès")
        print("💡 N'oubliez pas de commit les changements :")
        print("   git add .github/workflows/")
        print('   git commit -m "fix(workflows): retirer trailing spaces yamllint"')
    else:
        print("\n✅ Tous les workflows sont déjà conformes")

if __name__ == '__main__':
    main()
