# VENV: virtual environment path (default: .venv)
VENV ?= .venv
# PYTHON: Python interpreter used by setup (default: $(VENV)/bin/python)
PYTHON ?= $(VENV)/bin/python
# MASPY: MASPY requirement to install. Defaults to the published package.
#   Integration: MASPY="git+https://github.com/geovanaSouza/MASPY.git@integration"
#   Local:       MASPY="-e ../MASPY"
MASPY ?= maspy-ml
MASPY_INTEGRATION ?= git+https://github.com/geovanaSouza/MASPY.git@integration

.PHONY: setup install-maspy install-integration run clean help

setup: ## Create the virtual environment and install project dependencies
	uv venv $(VENV) --python 3.12
	uv pip install --python $(PYTHON) -e .

install-maspy: ## Install/replace MASPY (default: published; override with MASPY=...)
	uv pip install --python $(PYTHON) --reinstall-package maspy-ml $(MASPY)

install-integration: ## Create/update the venv and install MASPY from the integration branch
	$(MAKE) setup
	$(MAKE) install-maspy MASPY="$(MASPY_INTEGRATION)"

run: ## Run the shelf robot simulation
	$(PYTHON) -m shelf

clean: ## Remove the virtual environment
	rm -rf $(VENV)

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
