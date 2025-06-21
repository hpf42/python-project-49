clean:
	rm -rf dist/ build/ *.egg-info


install:
	uv sync


build:
	uv build


force-install:
	uv tool install --force dist/*.whl


packege-install:
	uv tool install dist/*.whl


brain-games:
	uv run brain-games


brain-even:
	uv run brain-even


brain-calc:
	uv run brain-calc


brain-gdc:
	uv run brain-gdc


lint:
	uv run ruff check brain_games


lint-fix:
	uv run ruff check --fix