from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []
        self.fragment_links = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in {"script", "img", "link"}:
            attr = "href" if tag == "link" else "src"
            value = attrs.get(attr, "")
            if value and not value.startswith(("http://", "https://", "data:")):
                self.references.append(value.split("?", 1)[0])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.fragment_links.append(attrs["href"][1:])
        if tag == "img" and "alt" not in attrs:
            self.errors.append("Imagem sem atributo alt")
        if tag == "button" and not (attrs.get("aria-label") or attrs.get("aria-labelledby")):
            self.errors.append("Botão sem nome acessível")

parser = SiteParser()
parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
missing = [ref for ref in parser.references if not (ROOT / ref).exists()]
missing_fragments = [target for target in parser.fragment_links if target not in parser.ids]
if missing:
    parser.errors.append("Referências locais inexistentes: " + ", ".join(missing))
if missing_fragments:
    parser.errors.append("Âncoras sem destino: " + ", ".join(missing_fragments))
if "main-content" not in parser.ids or "slides" not in parser.ids:
    parser.errors.append("Falta o destino de skip link ou o contentor do carrossel")
css = (ROOT / "css/styles.css").read_text(encoding="utf-8")
if "prefers-reduced-motion" not in css:
    parser.errors.append("Falta suporte a prefers-reduced-motion")
js = (ROOT / "js/script.js").read_text(encoding="utf-8")
if "setInterval" in js:
    parser.errors.append("O carrossel não deve avançar automaticamente")
if parser.errors:
    raise SystemExit("\n".join(parser.errors))
print("HTML: referências e IDs válidos; imagens/controlos nomeados; movimento reduzido ativo")
