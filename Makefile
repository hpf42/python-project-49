install:
	uv sync


build:
	uv build


packege-install:
	uv tool install dist/*.whl