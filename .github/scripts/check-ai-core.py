#!/usr/bin/env python3
# check-ai-core.py: validate AI_CORE.yml YAML syntax
import sys
try:
    import yaml  # type: ignore
except Exception as e:
    print(f"❌ PyYAML non disponible: {e}")
    sys.exit(1)

try:
    with open('AI_CORE.yml','r',encoding='utf-8') as f:
        yaml.safe_load(f)
    print('✅ AI_CORE.yml syntaxe YAML valide')
except Exception as e:
    print(f"❌ AI_CORE.yml invalide: {e}")
    sys.exit(1)
