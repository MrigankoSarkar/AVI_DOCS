# Makefile for Sphinx documentation

SPHINXBUILD   = ..\.venv\Scripts\sphinx-build.exe
SOURCEDIR     = .
BUILDDIR      = _build

.PHONY: help html clean

help:
	@echo "Makefile for building Sphinx documentation"
	@echo "  make html    - Build the HTML documentation"
	@echo "  make clean   - Remove build artifacts"

html:
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" -q

clean:
	rm -rf $(BUILDDIR)
