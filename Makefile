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


lint:
	uv run ruff check brain-games