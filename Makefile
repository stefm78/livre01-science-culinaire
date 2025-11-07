.PHONY: lint lint-yaml lint-shell lint-python

lint: lint-yaml lint-shell lint-python
	@echo "✅ All lint checks passed"

lint-yaml:
	@echo "=== YAML LINT ==="
	@yamllint -c .yamllint.yml . || { echo "❌ YAML issues found"; exit 1; }

lint-shell:
	@echo "=== SHELL LINT ==="
	@if ls .github/scripts/*.sh 1> /dev/null 2>&1; then \
		shellcheck .github/scripts/*.sh || { echo "❌ Shell issues found"; exit 1; }; \
	else \
		echo "(no shell scripts)"; \
	fi

lint-python:
	@echo "=== PYTHON LINT ==="
	@if ls .github/scripts/*.py 1> /dev/null 2>&1; then \
		python3 -m py_compile .github/scripts/*.py || { echo "❌ Python syntax errors"; exit 1; }; \
	else \
		echo "(no python scripts)"; \
	fi
