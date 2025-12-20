#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

# ============================
# CONFIGURAÇÕES
# ============================

DATA_DIR = Path("data")
OUTPUT = Path("datapackage/datapackage.json")

DATASET_NAME = "empregados-terceirizados-mg"
OWNER_ORG = "controladoria-geral-do-estado-cge"

# ============================
# COLETA DOS CSVs
# ============================

resources = []

csv_files = sorted(DATA_DIR.glob("terceirizados_*.csv"))

if not csv_files:
    raise RuntimeError("❌ Nenhum arquivo terceirizados_*.csv encontrado na pasta data/")

for csv in csv_files:
    ano = csv.stem.split("_")[-1]

    resources.append({
        "name": f"terceirizados-{ano}",
        "title": f"Empregados Terceirizados – {ano}",
        "path": f"data/{csv.name}",
        "profile": "tabular-data-resource",
        "scheme": "file",
        "format": "csv",
        "encoding": "utf-8",
        "mediatype": "text/csv",
        "description": f"Dados de empregados terceirizados do Governo de Minas Gerais – ano de {ano}",
        "schema": {
            "fields": [
                {"name": "matricula", "type": "string", "title": "Matrícula"},
                {"name": "nome", "type": "string", "title": "Nome"},
                {"name": "orgao", "type": "string", "title": "Órgão"},
                {"name": "cargo", "type": "string", "title": "Cargo"},
                {"name": "empresa", "type": "string", "title": "Empresa"},
                {"name": "cnpj_empresa", "type": "string", "title": "CNPJ da Empresa"},
                {"name": "mes_referencia", "type": "string", "title": "Mês de referência"}
            ],
            "primaryKey": ["matricula", "mes_referencia"]
        }
    })

# ============================
# DATAPACKAGE FINAL
# ============================

datapackage = {
    "profile": "data-package",
    "name": DATASET_NAME,
    "title": "Empregados Terceirizados do Governo de Minas Gerais",
    "description": "Base anual de empregados terceirizados do Governo do Estado de Minas Gerais.",
    "owner_org": OWNER_ORG,
    "resources": resources
}

# ============================
# GRAVAÇÃO
# ============================

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(
    json.dumps(datapackage, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print(f"✔ datapackage.json gerado com sucesso ({len(resources)} recursos)")
