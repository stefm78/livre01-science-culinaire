# 💡 Aide automatisée IA Sprint 2

- Les fichiers recettes, metadata et prompts images sont installés et validés (voir backlog).
- Les images IA ne peuvent être générées actuellement (quota atteint). Vérification automatique lors du passage du pipeline.
- Script de validation automatique à lancer :

```bash
python scripts/validate-recipe.py recettes/poulet-roti-juteux
python scripts/validate-recipe.py recettes/boeuf-bourguignon
python scripts/validate-recipe.py recettes/magret-canard-laque
```

- Si tout est conforme, préparer le Pull Request vers `main`.
- Intégrer commentaires, feedback, quickfix des reviewers puis merge.

---

Tâches IA restantes à faire :
- [ ] Génération images IA (bloqué)
- [ ] Validation script automatique
- [ ] PR + mise à jour index/metadata global
- [ ] Release Sprint 2 finale

*(Document mis à jour automatiquement par IA contributrice le 18/11/2025, 09:51 CET)*
