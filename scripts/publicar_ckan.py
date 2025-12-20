#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import requests
from pathlib import Path
import re

# =============================
# CONFIGURAÇÕES
# =============================
CKAN_URL = "https://www.dados.mg.gov.br"
API_KEY = os.environ.get("CKAN_KEY")

if not API_KEY:
    raise RuntimeError("CKAN_KEY não encontrada como variável de ambiente")

HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

DATASET_NAME = "empregados-terceirizados"
OWNER_ORG = "controladoria-geral-do-estado-cge"

GITHUB_REPO = "transparencia-mg/empregados_terceirizados"
GITHUB_BRANCH = "main"

# =============================
# FUNÇÕES AUXILIARES
# =============================
def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value)
    return value.strip("-")

# =============================
# Carregar datapackage
# =============================
datapackage = json.loads(
    Path("datapackage/datapackage.json").read_text(encoding="utf-8")
)

# =============================
# Criar ou atualizar dataset
# =============================
dataset_payload = {
    "name": DATASET_NAME,
    "title": datapackage.get("title", DATASET_NAME),
    "notes": datapackage.get("description", ""),
    "owner_org": OWNER_ORG,
    "license_id": "cc-by",
    "state": "active"
}

r = requests.post(
    f"{CKAN_URL}/api/3/action/package_show",
    headers=HEADERS,
    json={"id": DATASET_NAME}
)

action = "package_update" if r.ok else "package_create"

r = requests.post(
    f"{CKAN_URL}/api/3/action/{action}",
    headers=HEADERS,
    json=dataset_payload
)

if not r.ok:
    raise RuntimeError(f"Erro ao criar/atualizar dataset: {r.text}")

print("✔ Dataset criado/atualizado com sucesso.")

# =============================
# Criar ou atualizar recursos
# =============================
for res in datapackage["resources"]:
    resource_name = slugify(res["name"])

    resource_url = (
        f"https://raw.githubusercontent.com/"
        f"{GITHUB_REPO}/{GITHUB_BRANCH}/{res['path']}"
    )

    resource_payload = {
        "package_id": DATASET_NAME,
        "name": resource_name,
        "title": res.get("title", resource_name),
        "url": resource_url,
        "url_type": "link",
        "format": "CSV",
        "description": res.get("description", ""),
        "schema": res.get("schema")
    }

    # Verifica se o recurso já existe
    r = requests.post(
        f"{CKAN_URL}/api/3/action/resource_search",
        headers=HEADERS,
        json={
            "query": f'name:"{resource_name}"',
            "package_id": DATASET_NAME
        }
    )

    exists = r.ok and r.json()["result"]["count"] > 0

    if exists:
        resource_payload["id"] = r.json()["result"]["results"][0]["id"]
        action = "resource_update"
    else:
        action = "resource_create"

    r = requests.post(
        f"{CKAN_URL}/api/3/action/{action}",
        headers=HEADERS,
        json=resource_payload
    )

    if r.ok:
        print(f"✔ Recurso publicado: {res['title']}")
    else:
        raise RuntimeError(
            f"Erro ao publicar recurso {res['title']}:\n{r.text}"
        )

print("🏁 Publicação no CKAN finalizada com sucesso.")
