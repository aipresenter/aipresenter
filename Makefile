all: verify

lint:
	ruff --format=github --select=E9,F63,F7,F82 --target-version=py37 .
	ruff --format=github --target-version=py37 .
	flake8 sample tests

tests:
	python3 -m unittest discover

verify: lint tests

.PHONY: lint tests verify
