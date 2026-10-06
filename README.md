# CV — Nikolai Avtsinov

Bilingual CV (English / Russian) generated with LaTeX and published with GitHub Pages.

## Project structure

- `src/cv_en.tex` — English CV content
- `src/cv_ru.tex` — Russian CV content
- `src/common.tex` — shared LaTeX layout and formatting
- `docs/index.html` — GitHub Pages landing page
- `.github/workflows/build.yml` — automatic PDF build and deployment

## Local build

Requirements:

- XeLaTeX
- latexmk

Build English:

```bash
cd src
latexmk -xelatex -interaction=nonstopmode cv_en.tex
```

Build Russian:

```bash
cd src
latexmk -xelatex -interaction=nonstopmode cv_ru.tex
```

## GitHub Pages

1. Create a GitHub repository, for example `cv`.
2. Push this project to the `main` branch.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **GitHub Actions**.
5. Push a change or run **Actions → Build CV → Run workflow**.
6. GitHub will publish the generated site.

The workflow compiles both PDFs with XeLaTeX and deploys the `docs/` directory as the Pages site.

## Updating the CV

Most text is defined near the top of `src/cv_en.tex` and `src/cv_ru.tex`. The visual layout is shared in `src/common.tex`, so design changes only need to be made once.
