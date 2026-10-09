PYTHON = .venv/bin/python
MAIN = a_maze_ing.py
CONFIG = config.txt
VENV = .venv
PIP = $(VENV)/bin/pip

MYPY_FLAGS = --warn-return-any --warn-unused-ignores \
    --ignore-missing-imports --disallow-untyped-defs \
    --check-untyped-defs

.PHONY: install run debug clean lint lint-strict build

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install -r requirements.txt
	$(PIP) install build

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .mypy_cache

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . $(MYPY_FLAGS)

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

build:
	$(PYTHON) -m build