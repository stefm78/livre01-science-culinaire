#!/usr/bin/env python3
"""
Analyse qualité fichier Scribus PAO
Usage: python livre/scripts/pao-analyze.py [fichier.sla]
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import sys
import argparse


class ScribusAnalyzer:
    def __init__(self, sla_path):
        self.sla_path = Path(sla_path)
        self.tree = ET.parse(self.sla_path)
        self.root = self.tree.getroot()
        self.issues = []
        
    def check_margins(self, expected_mm=15):
        print("🔍 Vérification marges...")
        expected_pts = expected_mm * 2.83465
        tolerance = 0.5 * 2.83465
        pages_checked = 0
        issues_found = 0
        
        for i, page in enumerate(self.root.findall('.//PAGE'), 1):
            pages_checked += 1
            margins = {
                'top': float(page.get('BORDERTOP', 0)),
                'bottom': float(page.get('BORDERBOTTOM', 0)),
                'left': float(page.get('BORDERLEFT', 0)),
                'right': float(page.get('BORDERRIGHT', 0))
            }
            
            for side, value in margins.items():
                actual_mm = round(value / 2.83465, 1)
                if abs(value - expected_pts) > tolerance:
                    issues_found += 1
                    self.issues.append({
                        'type': 'margin',
                        'page': i,
                        'side': side,
                        'expected': expected_mm,
                        'actual': actual_mm
                    })
        
        if issues_found == 0:
            print(f"  ✅ Marges conformes (15mm) sur {pages_checked} pages")
        else:
            print(f"  ⚠️  {issues_found} marges non conformes")
    
    def check_document_info(self):
        print("\n📄 Informations document...")
        document = self.root.find('.//DOCUMENT')
        if document is None:
            return
        
        width_pts = float(document.get('PAGEWIDTH', 0))
        height_pts = float(document.get('PAGEHEIGHT', 0))
        width_mm = round(width_pts / 2.83465, 1)
        height_mm = round(height_pts / 2.83465, 1)
        pages = len(self.root.findall('.//PAGE'))
        title = document.get('TITLE', 'N/A')
        
        print(f"  📏 Format : {width_mm} x {height_mm} mm")
        print(f"  📖 Pages : {pages}")
        print(f"  📝 Titre : {title}")
    
    def generate_report(self):
        print("\n" + "="*60)
        print("📊 RAPPORT QUALITÉ PAO - Scribus")
        print("="*60)
        print(f"📁 Fichier : {self.sla_path.name}")
        print()
        
        self.check_document_info()
        self.check_margins()
        
        print("\n" + "="*60)
        if not self.issues:
            print("✅ Aucun problème détecté")
        else:
            print(f"⚠️  {len(self.issues)} problème(s) détecté(s)")
            for issue in self.issues:
                if issue['type'] == 'margin':
                    print(f"  • Page {issue['page']} : marge {issue['side']} "
                          f"= {issue['actual']}mm (attendu {issue['expected']}mm)")
        print("="*60)
        return len(self.issues) == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sla_file', nargs='?', 
                        default='livre/production/exports/livre-mvp.sla')
    args = parser.parse_args()
    sla_file = Path(args.sla_file)
    
    if not sla_file.exists():
        print(f"❌ Fichier introuvable : {sla_file}")
        sys.exit(1)
    
    try:
        analyzer = ScribusAnalyzer(sla_file)
        success = analyzer.generate_report()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
