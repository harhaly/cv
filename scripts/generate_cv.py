from pathlib import Path
import html
import shutil
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cv.yaml"
TEMPLATES = ROOT / "templates"
SRC = ROOT / "src"
DOCS = ROOT / "docs"


def latex_escape(value: object) -> str:
    text = str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def html_filter(value: object) -> str:
    return html.escape(str(value))


def main() -> None:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        autoescape=False,
    )
    env.filters["latex"] = latex_escape
    env.filters["html"] = html_filter

    tex_template = env.get_template("cv.tex.j2")
    html_template = env.get_template("cv.html.j2")
    css = (TEMPLATES / "cv.css").read_text(encoding="utf-8")

    SRC.mkdir(parents=True, exist_ok=True)
    (SRC / "cv_en.tex").write_text(
        tex_template.render(person=data["person"], lang=data["languages"]["en"]),
        encoding="utf-8",
    )
    (SRC / "cv_ru.tex").write_text(
        tex_template.render(person=data["person"], lang=data["languages"]["ru"]),
        encoding="utf-8",
    )

    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "index.html").write_text(
        html_template.render(person=data["person"], lang=data["languages"]["en"], css_path="/cv.css"),
        encoding="utf-8",
    )
    (DOCS / "ru").mkdir(parents=True, exist_ok=True)
    (DOCS / "ru" / "index.html").write_text(
        html_template.render(person=data["person"], lang=data["languages"]["ru"], css_path="/cv.css"),
        encoding="utf-8",
    )
    (DOCS / "cv.css").write_text(css, encoding="utf-8")

    print("Generated:")
    print("  src/cv_en.tex")
    print("  src/cv_ru.tex")
    print("  docs/index.html")
    print("  docs/ru/index.html")
    print("  docs/cv.css")


if __name__ == "__main__":
    main()
