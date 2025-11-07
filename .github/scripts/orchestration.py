#!/usr/bin/env python3
"""
Script d'orchestration pour la gestion automatique des phases projet
Extrait de issue-orchestration.yml pour robustesse et testabilité
Conforme à l'ADN: frugal, émergent, lisible, traçable
"""

import yaml
import os
import sys
from datetime import datetime

def parse_workflow_state():
    """Parse WORKFLOW_STATE.yml pour identifier phases et dépendances"""
    if not os.path.exists('WORKFLOW_STATE.yml'):
        print("workflow-exists=false")
        return None
        
    try:
        with open('WORKFLOW_STATE.yml', 'r', encoding='utf-8') as f:
            content = f.read()
            # Remplacer les placeholders pour la lecture
            content = content.replace('{{', '').replace('}}', '')
            workflow = yaml.safe_load(content)
        
        phases = workflow.get('phases', [])
        current_issue = os.getenv('GITHUB_ISSUE_NUMBER', '')
        
        # Identifier la phase de cette issue
        issue_labels = os.getenv('GITHUB_ISSUE_LABELS', '')
        phase_type = None
        
        if 'phase-recherche' in issue_labels:
            phase_type = 'phase_02_recherche'
        elif 'phase-conception' in issue_labels:
            phase_type = 'phase_03_conception'
        elif 'phase-production' in issue_labels:
            phase_type = 'phase_04_production'
        elif 'phase-validation' in issue_labels:
            phase_type = 'phase_05_validation'
        elif 'phase-finalisation' in issue_labels:
            phase_type = 'phase_06_finalisation'
            
        print(f"phase-type={phase_type}")
        
        # Trouver la phase suivante
        if phase_type:
            phase_index = next((i for i, p in enumerate(phases) if p.get('id') == phase_type), -1)
            if 0 <= phase_index < len(phases) - 1:
                next_phase = phases[phase_index + 1]
                print(f"next-phase-id={next_phase.get('id')}")
                print(f"next-phase-name={next_phase.get('name')}")
                
        print("workflow-exists=true")
        return workflow
        
    except Exception as e:
        print(f"Error: {e}")
        print("workflow-exists=false")
        return None

def update_workflow_completion(issue_labels):
    """Met à jour WORKFLOW_STATE.yml avec l'état de complétion"""
    if not os.path.exists('WORKFLOW_STATE.yml'):
        print("WORKFLOW_STATE.yml non trouvé")
        return
        
    try:
        with open('WORKFLOW_STATE.yml', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Identifier la phase complétée
        replacements = []
        
        if 'phase-recherche' in issue_labels:
            replacements.extend([
                ('{{PHASE_02_STATUS}}', 'completed'),
                ('{{PHASE_02_COMPLETION}}', datetime.now().strftime('%Y-%m-%d'))
            ])
        elif 'phase-conception' in issue_labels:
            replacements.extend([
                ('{{PHASE_03_STATUS}}', 'completed'),
                ('{{PHASE_03_COMPLETION}}', datetime.now().strftime('%Y-%m-%d'))
            ])
        elif 'phase-production' in issue_labels:
            replacements.extend([
                ('{{PHASE_04_STATUS}}', 'completed'),
                ('{{PHASE_04_COMPLETION}}', datetime.now().strftime('%Y-%m-%d'))
            ])
        elif 'phase-validation' in issue_labels:
            replacements.extend([
                ('{{PHASE_05_STATUS}}', 'completed'),
                ('{{PHASE_05_COMPLETION}}', datetime.now().strftime('%Y-%m-%d'))
            ])
        elif 'phase-finalisation' in issue_labels:
            replacements.extend([
                ('{{PHASE_06_STATUS}}', 'completed'),
                ('{{PHASE_06_COMPLETION}}', datetime.now().strftime('%Y-%m-%d'))
            ])
            
        # Mettre à jour les métadonnées
        replacements.extend([
            ('{{LAST_UPDATE}}', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            ('{{UPDATED_BY}}', 'github-actions'),
            ('{{LAST_ACTION}}', f"Phase completed: Issue #{os.getenv('GITHUB_ISSUE_NUMBER', '?')}")
        ])
        
        # Appliquer les remplacements
        for old, new in replacements:
            content = content.replace(old, new)
            
        # Écrire le fichier mis à jour
        with open('WORKFLOW_STATE.yml', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("WORKFLOW_STATE.yml mis à jour")
        
    except Exception as e:
        print(f"Erreur mise à jour: {e}")

def main():
    """Point d'entrée principal"""
    action = sys.argv[1] if len(sys.argv) > 1 else 'parse'
    
    if action == 'parse':
        parse_workflow_state()
    elif action == 'update':
        issue_labels = os.getenv('GITHUB_ISSUE_LABELS', '')
        update_workflow_completion(issue_labels)
    else:
        print(f"Action inconnue: {action}")
        sys.exit(1)

if __name__ == '__main__':
    main()
