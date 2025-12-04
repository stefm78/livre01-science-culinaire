#!/usr/bin/env python3
"""
Ajustements automatiques fichier Scribus PAO
Usage: python livre/scripts/pao-auto-adjust.py [fichier.sla]
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import shutil
from datetime import datetime
import sys
import argparse


class ScribusAdjuster:
    def __init__(self, sla_path):
        self.sla_path = Path(sla_path)
        self.tree = ET.parse(self.sla_path)
        self.root = self.tree.getroot()
        self.changes = []
    
    def backup(self):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.sla_path.with_suffix(f'.sla.{timestamp}.bak')
        shutil.copy2(self.sla_path, backup_path)
        print(f"💾 Backup : {backup_path.name}")
        return backup_path
    
    def adjust_margins(self, margin_mm=15):
        print(f"\n🔧 Ajustement marges à {margin_mm}mm...")
        margin_pts = margin_mm * 2.83465
        count = 0
        
        for page in self.root.findall('.//PAGE'):
            page.set('BORDERTOP', str(margin_pts))
            page.set('BORDERBOTTOM', str(margin_pts))
            page.set('BORDERLEFT', str(margin_pts))
            page.set('BORDERRIGHT', str(margin_pts))
            count += 1
        
        if count:
            self.changes.append(f"Marges ajustées sur {count} pages")
            print(f"  ✅ {count} pages modifiées")
    
    def fix_bleeds(self, bleed_mm=3):
        print(f"\n🔧 Fonds perdus {bleed_mm}mm...")
        bleed_pts = bleed_mm * 2.83465
        
        document = self.root.find('.//DOCUMENT')
        if document is not None:
            document.set('BleedTop', str(bleed_pts))
            document.set('BleedBottom', str(bleed_pts))
            document.set('BleedLeft', str(bleed_pts))
            document.set('BleedRight', str(bleed_pts))
            self.changes.append(f"Fonds perdus : {bleed_mm}mm")
            print(f"  ✅ Configurés")
    
    def save(self):
        ET.indent(self.tree, space="  ")
        self.tree.write(self.sla_path, encoding='utf-8', xml_declaration=True)
        print(f"\n💾 Sauvegardé : {self.sla_path.name}")
    
    def run(self):
        print("🤖 Ajustements automatiques Scribus")
        print("="*60)
        
        backup_file = self.backup()
        self.adjust_margins(15)
        self.fix_bleeds(3)
        self.save()
        
        print("\n" + "="*60)
        print(f"✅ Terminé - {len(self.changes)} modifications")
        if self.changes:
            print("\nChangements :")
            for c in self.changes:
                print(f"  - {c}")
        print("="*60)


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
        adjuster = ScribusAdjuster(sla_file)
        adjuster.run()
    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
