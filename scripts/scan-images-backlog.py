#!/usr/bin/env python3
"""
Scan du backlog images IA - Détection robuste des images manquantes/invalides
Livre01 - Science Culinaire
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from PIL import Image
import hashlib

class ImageBacklogScanner:
    """Scanner robuste du backlog images avec validation stricte"""
    
    MIN_FILE_SIZE = 50_000  # 50 KB
    MAX_FILE_SIZE = 3_145_728  # 3 MB
    MIN_RESOLUTION = 1500
    
    def __init__(self, recipes_path="recettes"):
        self.recipes_path = Path(recipes_path)
        self.results = {
            "scan_date": datetime.now().isoformat(),
            "recipes": [],
            "summary": {},
            "issues": []
        }
    
    def validate_image_file(self, image_path):
        """Validation stricte d'un fichier image"""
        issues = []
        
        # 1. Vérifier existence
        if not image_path.exists():
            return False, ["Fichier absent"]
        
        # 2. Vérifier taille fichier
        file_size = image_path.stat().st_size
        
        if file_size < self.MIN_FILE_SIZE:
            issues.append(f"⚠️ PLACEHOLDER DÉTECTÉ: {file_size} bytes (min: {self.MIN_FILE_SIZE})")
            return False, issues
        
        if file_size > self.MAX_FILE_SIZE:
            issues.append(f"❌ TROP LOURD: {file_size} bytes (max: {self.MAX_FILE_SIZE})")
            return False, issues
        
        # 3. Vérifier format et intégrité
        try:
            with Image.open(image_path) as img:
                # Vérifier dimensions
                width, height = img.size
                if width < self.MIN_RESOLUTION or height < self.MIN_RESOLUTION:
                    issues.append(f"❌ RÉSOLUTION INSUFFISANTE: {width}x{height} (min: {self.MIN_RESOLUTION})")
                    return False, issues
                
                # Vérifier format
                if img.format != 'PNG':
                    issues.append(f"❌ FORMAT INVALIDE: {img.format} (requis: PNG)")
                    return False, issues
                
        except Exception as e:
            issues.append(f"❌ FICHIER CORROMPU: {str(e)}")
            return False, issues
        
        return True, []
    
    def parse_checklist(self, readme_path):
        """Parse la checklist du README.md images"""
        if not readme_path.exists():
            return []
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraire section checklist
        checklist_match = re.search(
            r'## ✅ Checklist.*?(?=\n##|\Z)', 
            content, 
            re.DOTALL
        )
        
        if not checklist_match:
            return []
        
        checklist_section = checklist_match.group(0)
        
        # Parser les items
        items = []
        for line in checklist_section.split('\n'):
            # Détection items checklist: - [ ] ou - [x]
            match = re.match(r'- \[([ x])\] (.+)', line)
            if match:
                checked = match.group(1) == 'x'
                description = match.group(2)
                
                # Extraire nom fichier si présent
                filename_match = re.search(r'(\w+\.png)', description)
                filename = filename_match.group(1) if filename_match else None
                
                # Détecter priorité
                priority = "CRITIQUE" if "critique" in description.lower() or "obligatoire" in description.lower() else "OPTIONNEL"
                
                items.append({
                    "checked": checked,
                    "description": description,
                    "filename": filename,
                    "priority": priority
                })
        
        return items
    
    def scan_recipe(self, recipe_dir):
        """Scan complet d'une recette"""
        recipe_name = recipe_dir.name
        images_dir = recipe_dir / "images"
        readme_path = images_dir / "README.md"
        
        result = {
            "name": recipe_name,
            "images_dir_exists": images_dir.exists(),
            "readme_exists": readme_path.exists(),
            "images": [],
            "stats": {
                "total_expected": 0,
                "valid": 0,
                "missing": 0,
                "invalid": 0,
                "placeholder": 0
            }
        }
        
        if not result["readme_exists"]:
            self.results["issues"].append({
                "recipe": recipe_name,
                "type": "NO_README",
                "message": "README.md images manquant"
            })
            return result
        
        # Parser checklist
        checklist = self.parse_checklist(readme_path)
        result["stats"]["total_expected"] = len([i for i in checklist if i["filename"]])
        
        # Valider chaque image
        for item in checklist:
            if not item["filename"]:
                continue
            
            image_path = images_dir / item["filename"]
            is_valid, issues = self.validate_image_file(image_path)
            
            image_info = {
                "filename": item["filename"],
                "priority": item["priority"],
                "checked_in_readme": item["checked"],
                "file_exists": image_path.exists(),
                "is_valid": is_valid,
                "issues": issues,
                "file_size": image_path.stat().st_size if image_path.exists() else 0
            }
            
            result["images"].append(image_info)
            
            # Compteurs
            if is_valid:
                result["stats"]["valid"] += 1
            elif not image_path.exists():
                result["stats"]["missing"] += 1
            elif "PLACEHOLDER" in str(issues):
                result["stats"]["placeholder"] += 1
            else:
                result["stats"]["invalid"] += 1
            
            # Détection incohérences
            if item["checked"] and not is_valid:
                self.results["issues"].append({
                    "recipe": recipe_name,
                    "type": "INCONSISTENCY",
                    "file": item["filename"],
                    "message": f"Checklist cochée mais image invalide: {issues}"
                })
        
        return result
    
    def scan_all(self):
        """Scan complet du repo"""
        print("🔍 Scan du backlog images IA...")
        
        # Scanner toutes les recettes
        for recipe_dir in sorted(self.recipes_path.iterdir()):
            if recipe_dir.is_dir() and not recipe_dir.name.startswith('_'):
                result = self.scan_recipe(recipe_dir)
                self.results["recipes"].append(result)
                print(f"  ✓ {recipe_dir.name}: {result['stats']['valid']}/{result['stats']['total_expected']} valides")
        
        # Calculer stats globales
        self.results["summary"] = {
            "total_recipes": len(self.results["recipes"]),
            "total_images_expected": sum(r["stats"]["total_expected"] for r in self.results["recipes"]),
            "total_valid": sum(r["stats"]["valid"] for r in self.results["recipes"]),
            "total_missing": sum(r["stats"]["missing"] for r in self.results["recipes"]),
            "total_placeholder": sum(r["stats"]["placeholder"] for r in self.results["recipes"]),
            "total_invalid": sum(r["stats"]["invalid"] for r in self.results["recipes"]),
            "completion_rate": 0
        }
        
        total_expected = self.results["summary"]["total_images_expected"]
        if total_expected > 0:
            self.results["summary"]["completion_rate"] = round(
                (self.results["summary"]["total_valid"] / total_expected) * 100, 1
            )
        
        return self.results
    
    def generate_markdown_report(self):
        """Génère rapport Markdown pour issue GitHub"""
        report = f"""# 📊 Rapport Backlog Images IA - {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 📈 Vue d'ensemble

- **Recettes scannées** : {self.results['summary']['total_recipes']}
- **Images attendues** : {self.results['summary']['total_images_expected']}
- **Images valides** : {self.results['summary']['total_valid']} ✅
- **Images manquantes** : {self.results['summary']['total_missing']} ⬜
- **Placeholders détectés** : {self.results['summary']['total_placeholder']} ⚠️
- **Images invalides** : {self.results['summary']['total_invalid']} ❌
- **Taux complétion** : {self.results['summary']['completion_rate']}%

---

## 🎯 Détail par recette

"""
        for recipe in self.results["recipes"]:
            report += f"\n### {recipe['name']}\n\n"
            report += f"**Stats** : {recipe['stats']['valid']}/{recipe['stats']['total_expected']} valides"
            report += f" | Manquantes: {recipe['stats']['missing']}"
            report += f" | Placeholders: {recipe['stats']['placeholder']}"
            report += f" | Invalides: {recipe['stats']['invalid']}\n\n"
            
            # Lister images problématiques
            problematic = [img for img in recipe["images"] if not img["is_valid"]]
            if problematic:
                report += "**À générer/corriger** :\n"
                for img in problematic:
                    status = "⬜ MANQUANTE" if not img["file_exists"] else f"⚠️ {img['issues'][0]}"
                    report += f"- `{img['filename']}` ({img['priority']}) - {status}\n"
                report += "\n"
        
        # Problèmes critiques
        if self.results["issues"]:
            report += "\n---\n\n## ⚠️ Problèmes détectés\n\n"
            for issue in self.results["issues"]:
                report += f"- **{issue['recipe']}** : {issue['message']}\n"
        
        return report
    
    def save_reports(self, json_path="_inbox/images/backlog-scan.json", md_path="_inbox/images/BACKLOG-REPORT.md"):
        """Sauvegarde les rapports"""
        # JSON
        Path(json_path).parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        # Markdown
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(self.generate_markdown_report())
        
        print(f"\n✅ Rapports générés:")
        print(f"   📄 JSON: {json_path}")
        print(f"   📝 Markdown: {md_path}")


if __name__ == "__main__":
    scanner = ImageBacklogScanner()
    results = scanner.scan_all()
    scanner.save_reports()
    
    print(f"\n🎯 Résumé: {results['summary']['completion_rate']}% complété")
    print(f"   ✅ {results['summary']['total_valid']} images valides")
    print(f"   ⚠️ {results['summary']['total_placeholder']} placeholders à remplacer")
    print(f"   ⬜ {results['summary']['total_missing']} images à générer")