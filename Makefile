.PHONY: help
help: # Display help for all Makefile commands
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: setup
setup: # Setup this project's pipenv environment
	pipenv install --deploy --dev

.PHONY: main-docs
main-docs: # Copy README.md to doc/index.md and build the docs in "doc/"
	rm -rf docs/
	cp README.md doc/index.md
	pipenv run sphinx-build -b dirhtml doc/ docs/

# Download each project's docs.tar.gz from its LATEST release and extract
# it into docs/<repo>/. A failed download warns with gh's error message and
# is skipped so one lagging project does not fail the whole build.
.PHONY: pull-docs
pull-docs: # Pull the latest docs.tar.gz from each project and extract into "docs/<repo>/"
	@while read -r url; do \
		[ -z "$$url" ] && continue; \
		repo=$$(basename "$$url"); \
		owner_repo=$${url#https://github.com/}; \
		echo "Pulling docs for $$owner_repo"; \
		mkdir -p "docs/$$repo"; \
		if err=$$(gh release download --repo "$$owner_repo" \
		     --pattern 'docs.tar.gz' \
		     --output "$$repo.tar.gz" \
		     --clobber 2>&1); then \
			tar -xzf "$$repo.tar.gz" -C "docs/$$repo"; \
			rm -f "$$repo.tar.gz"; \
		else \
			err=$$(printf '%s' "$$err" | tr -s '\n' ' '); \
			echo "::warning::Could not pull docs.tar.gz for $$owner_repo: $${err:-unknown error}; skipping"; \
			rmdir "docs/$$repo" 2>/dev/null || true; \
		fi; \
	done < projects.txt

.PHONY: docs
docs: # Combine the main docs with the pulled docs from other projects into "docs/"
	$(MAKE) main-docs
	$(MAKE) pull-docs
	echo "Generated and combined docs written to docs/"

.PHONY: read-docs
read-docs: # Open the current version of the blog in "docs/" locally
	open docs/index.html
