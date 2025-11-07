# Base documentaire minimale

Objectif: éviter la perte d'information dans les issues en consolidant une trace diffable, légère et réutilisable.

Règles :
- Consolidation en fin d'étape de recherche validée (pas de suivi continu)
- Deux fichiers Markdown dans `sources/` (noms et structure génériques):
  - `base-documentaire.md` (références factuelles)
  - `synthese.md` (synthèses/enseignements clés, associations/liens utiles)
- Les issues restent le lieu de discussion; le repository est la source de vérité consolidée.
- Aucune automatisation lourde, pas d’exports par défaut (JSON/CSV) tant que non nécessaire.

Processus:
1) Publier les résultats dans l’issue
2) Consolider dans `sources/` (création/mise à jour)
3) Commenter l’issue avec les chemins consolidés, puis fermer/archiver si objectif atteint
