# scripts/atualizar_index.py
from pathlib import Path

DATA_DIR = Path("data")
INDEX_FILE = Path("index.html")

arquivos = sorted(DATA_DIR.glob("terceirizados_*.csv"))

lista_html = "\n".join(
    f'<li><a href="data/{f.name}" download>{f.name}</a></li>'
    for f in arquivos
)

html = INDEX_FILE.read_text(encoding="utf-8")

inicio = "<!-- INICIO LISTA CSV -->"
fim = "<!-- FIM LISTA CSV -->"

novo = f"{inicio}\n<ul>\n{lista_html}\n</ul>\n{fim}"

html = html.split(inicio)[0] + novo + html.split(fim)[1]

INDEX_FILE.write_text(html, encoding="utf-8")
