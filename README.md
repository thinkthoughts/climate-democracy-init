# Climate Democracy Init

A reusable starter repository for climate-democracy lab reports, local watershed/school-district translation, and actionable public coordination.

This repo is intended to be used as a GitHub template for projects connected to:

- climate democracy work
- local lab reports
- watershed and school-district geography
- reproducible public documentation
- actionable ≠ artificial communication

## Quick start

```bash
git clone https://github.com/YOUR-ORG/climate-democracy-init.git
cd climate-democracy-init
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Repo structure

```text
site/                 Static site for climatedemocracy.app
notebooks/            Colab/Jupyter notebooks
src/                  Python modules
scripts/              Build helpers
results/              Generated JSON/CSV outputs
figures/              Generated figures
docs/                 Published reports/docs
paper/                Optional TeX paper scaffold
data/                 Local or example data
.github/workflows/    Optional automation
```

## First workflow

1. Edit `site/index.html` for the public landing page.
2. Run `notebooks/01_climate_democracy_init.ipynb` or adapt it in Colab.
3. Generate local report artifacts into `results/`, `figures/`, and `docs/reports/`.
4. Deploy `site/` to `climatedemocracy.app`.

## Core framing

Climate democracy becomes practical when local reading and writing are grounded in places people can actually observe:

- watershed geography
- school-district geography
- local public meetings
- public reports
- shared climate actions

Actionable public work is not a replacement for existing organizations. It is a reproducible support layer.
