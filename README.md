# 🧬 Projet Template - Génome Minimal ADN

Template pour créer des projets IA avec un "génome minimal" garantissant efficacité, simplicité et gouvernance distribuée.

## 🎯 Philosophie ADN

**Efficacité par la Simplicité** : Chaque élément a sa raison d'être précise. Aucun "bloatware", aucune bureaucratie paralysante.

**Émergence Guidée** : Les projets évoluent organiquement, guidés par des invariants clairs plutôt que par des spécifications rigides.

**Gouvernance Distribuée** : Les IA prennent des décisions dans leur domaine d'expertise, coordonnées par des workflows transparents.

## 📋 Structure du Génome

### Fichiers Vitaux (Invariants)
- `constitution-projet-ai.md` : Règles fondamentales du projet
- `AI_CORE.yml` : Configuration des personas IA et workflows
- `README.md` : Documentation essentielle
- `PROJECT_DNA.yml` : Patrimoine génétique évolutif du projet

### Outillage ADN Minimal
- `.github/scripts/common.sh` : Fonctions utilitaires robustes (retry, diagnostics, validation)
- `.github/templates/` : Contenus statiques versionnés (seed_header.md, seed_guidelines.md)
- `.github/workflows/lint-guard.yml` : Garde-fou qualité (yamllint, actionlint, shellcheck, vérification fichiers ADN)
- `.github/workflows/evolution.yml` : Gestion du feedback IA et des verrous
- `.github/workflows/issue-orchestration.yml` : Orchestration automatique des phases projet

### Documentation Organisée
- `docs/personas.md` : Documentation des rôles IA
- `templates/` : Modèles de fichiers pour démarrage rapide

## 🔒 Gouvernance des IA

### Système de Verrous
- **ia-locked** : Une IA travaille sur cette issue (timeout: 30min)
- **ia-available** : Issue disponible pour prise en charge IA
- **Relais automatique** : En cas d'inactivité > 30min, nouvelle IA peut prendre la main

### Feedback et Évolution
- `IA_FEEDBACK.yml` : Historique des interactions IA (max 50 entrées)
- **Synthèse automatique** : Issue "meta-synth" créée si feedback > seuil
- **Traçabilité complète** : Chaque action IA documentée et versionnée

## ⚙️ Garde-fous Qualité

**Lint Guard** bloque automatiquement :
- ❌ Erreurs syntaxe YAML/Actions/Shell
- ❌ Fichiers ADN vitaux manquants ou corrompus
- ❌ Templates invalides ou mal encodés
- ❌ Scripts non exécutables ou avec erreurs

**Conformité ADN** garantie :
- ✅ Frugalité : Outillage minimal nécessaire
- ✅ Émergence : Scripts modulaires et évolutifs
- ✅ Lisibilité : Logique externalisée des YAML
- ✅ Traçabilité : Diagnostics explicites, pas d'actions silencieuses

## 🚀 Utilisation

1. **Créer un projet** via [ia-activation](https://github.com/stefm78/ia-activation)
2. **Les IA se connectent** automatiquement via les labels `ia-available`
3. **Évolution organique** guidée par les workflows et la Constitution
4. **Qualité garantie** par les garde-fous automatiques

---

*Génome Minimal v1.1 - Efficacité par la Simplicité*