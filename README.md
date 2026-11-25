# project_name

> **Scientific question:** one sentence stating what this project answers.

![Headline result](results/headline.png)

## Background
Three short paragraphs: the biology or neuroscience, why the question matters, what is already known.

## Data
Sources, versions, licences and access dates are listed in [docs/DATA.md](docs/DATA.md).
Raw data is never committed. Download it with `scripts/get_data.sh`.

## Methods
Summary here. Full math, with every variable labelled, in [docs/METHODS.md](docs/METHODS.md).

## Validation
What the results were checked against, the tolerance, and the numbers obtained.

## Quickstart
```bash
mamba env create -f environment.yml
mamba activate project_name
bash scripts/get_data.sh
pytest
```

## Architecture
Diagram and a short description (only if the project has services, a database or jobs).

## API
Endpoints, if any.

## Limitations
See [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Reproducing the figures
One command per figure, or one command for all of them.

## Citation and references
See [CITATION.cff](CITATION.cff) and the references in docs/METHODS.md.

---

### Using this template (delete this section in a real project)
1. On GitHub: **Use this template → Create a new repository**.
2. Rename `project_name` in: `pyproject.toml` (name + packages path), `environment.yml`,
   `src/project_name/` (the folder), the imports in `tests/`, the `--cov` flag in
   `.github/workflows/ci.yml`, and this README.
3. Delete `src/project_name/sequence.py` and `tests/test_sequence.py` once you have real code.
4. Fill in the docs/ files as you go, not at the end.
