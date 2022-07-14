.PHONY: help
help:  ## Show this help.
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.PHONY: install-build
install-build:  ## Install build dependencies.
	python -m pip install build

.PHONY: build
build:  ## Build package.
	python -m build

.PHONY: install-publish
install-publish:  ## Install publish dependencies.
	python -m pip install twine

.PHONY: check
check:  ## Check long description regarding PyPi.
	python -m twine check dist/*

.PHONY: publish-test
publish-test:  ## Publish to TestPyPI.
	python -m twine upload --repository testpypi dist/*

.PHONY: publish
publish:  ## Publish to PyPI.
	python -m twine upload dist/*
