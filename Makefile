default:
	@echo "Simple Makefile to setup and run checks locally."
check:
	uv run --only-dev ruff check --fix .
format:
	uv run --only-dev ruff format
type: format
	uv run --only-dev ty check
build: type clean
	uv build
	uv export --no-hashes --format requirements.txt > requirements.txt
clean:
	rm -rf dist/
	rm -rf wheels/
