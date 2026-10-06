# CV — single source

The CV is maintained from **one content file**:

```text
data/cv.yaml
```

The generator uses that source to create both English and Russian:

- LaTeX source → PDF
- HTML resume page

The PDF layout/style remains in `src/common.tex`.

## Structure

```text
cv-github-pages-single-source/
├── .github/workflows/build.yml
├── data/cv.yaml                 # single source of CV content
├── scripts/generate_cv.py       # generator
├── templates/
│   ├── cv.tex.j2                # PDF template
│   ├── cv.html.j2               # website template
│   └── cv.css                   # website styles
├── src/
│   ├── common.tex               # PDF layout/style
│   ├── cv_en.tex                # generated source preview
│   └── cv_ru.tex                # generated source preview
├── docs/                        # generated Pages output / local preview
│   ├── index.html
│   ├── cv.css
│   ├── en/cv.pdf
│   └── ru/
│       ├── index.html
│       └── cv.pdf
├── requirements.txt
└── .gitignore
```

`docs/` is included in this ZIP so the project is immediately usable after extraction. It is generated output and remains ignored by Git; GitHub Actions recreates it on every build.

## Local build

```bash
python -m pip install -r requirements.txt
python scripts/generate_cv.py
cd src
latexmk -xelatex cv_en.tex
latexmk -xelatex cv_ru.tex
cp cv_en.pdf ../docs/en/cv.pdf
cp cv_ru.pdf ../docs/ru/cv.pdf
```

## GitHub Actions

Every push to `main`:

1. reads `data/cv.yaml`;
2. generates English and Russian LaTeX + HTML;
3. builds both PDFs with XeLaTeX;
4. puts the PDFs into `docs/en/` and `docs/ru/`;
5. deploys `docs/` to GitHub Pages.

Generated files are intentionally **not committed**. This avoids the generated-PDF commit/push loop.

For the root user site `harhaly.github.io`:

- `/` — English
- `/ru/` — Russian
- `/en/cv.pdf` — English PDF
- `/ru/cv.pdf` — Russian PDF
