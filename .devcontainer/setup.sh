#!/bin/bash

# Script d'initialisation Codespaces
# Exécuté automatiquement à la création du Codespace

echo "🚀 Configuration Environnement Livre Science Culinaire..."
echo "==============================================================="
echo ""

# Installation dépendances Python
echo "🐍 Installation dépendances Python..."
pip install --quiet --upgrade pip
pip install --quiet requests pillow

echo "✅ Python configuré"
echo ""

# Configuration Git
echo "🔧 Configuration Git..."
git config --global user.name "stefm78"
git config --global user.email "smagnand@gmail.com"
git config --global push.default current
git config --global pull.rebase false

echo "✅ Git configuré"
echo ""

# Rendre les scripts exécutables
echo "🛠️ Configuration scripts projet..."
chmod +x scripts/*.py 2>/dev/null || true

echo "✅ Scripts prêts"
echo ""

# Afficher informations projet
echo "==============================================================="
echo "📚 Livre Science Culinaire - Environnement Prêt"
echo "==============================================================="
echo ""
echo "📁 Structure projet :"
echo "  - sources/          : Documentation cadrage"
echo "  - recettes/         : Production 30 fiches (templates prêts)"
echo "  - images/tests/     : Photos tests validation charte"
echo "  - scripts/          : Outils automatisation"
echo ""
echo "🛠️ Outils disponibles :"
echo "  - python scripts/validate-recipe.py recettes/[nom]"
echo "  - python scripts/generate-index.py"
echo ""
echo "📚 Documentation :"
echo "  - recettes/README.md      : Workflow production"
echo "  - INFRASTRUCTURE.md       : Architecture complète"
echo ""
echo "🚀 Prêt pour production !"
echo ""
