from pathlib import Path

DATA_DIR = Path("data")
INDEX_FILE = Path("index.html")

# Lista os CSVs
arquivos = sorted(DATA_DIR.glob("terceirizados_*.csv"))

# Gera linhas JS
lista_js = ",\n    ".join(
    f"'{f.name}'" for f in arquivos
)

html = INDEX_FILE.read_text(encoding="utf-8")

inicio = "<!-- INICIO LISTA CSV -->"
fim = "<!-- FIM LISTA CSV -->"

novo = f"""{inicio}
const CSV_FILES = [
    {lista_js}
];
{fim}"""

# Substituição segura
html = html.split(inicio)[0] + novo + html.split(fim)[1]

INDEX_FILE.write_text(html, encoding="utf-8")

print("index.html atualizado com sucesso.")
