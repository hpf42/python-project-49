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


brain-gcd:
	uv run brain-gcd


brain-progression:
	uv run brain-progression


brain-prime:
	uv run brain-prime


lint:
	uv run ruff check brain_games


lint-fix:
	uv run ruff check --fix