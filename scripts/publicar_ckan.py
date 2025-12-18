import requests
import json
from pathlib import Path

CKAN_URL = "https://www.dados.mg.gov.br"
API_KEY = os.environ.get("CKAN_API_KEY")

DATASET_NAME = "empregados-terceirizados"
OWNER_ORG = "controladoria-geral-do-estado-cge"

datapackage = json.loads(Path("datapackage/datapackage.json").read_text(encoding="utf-8"))

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

# =============================
# Criar ou atualizar dataset
# =============================
dataset_payload = {
    "name": DATASET_NAME,
    "title": datapackage["title"],
    "notes": datapackage.get("description", ""),
    "owner_org": OWNER_ORG,
    "license_id": "cc-by",
    "state": "active"
}

r = requests.post(
    f"{CKAN_URL}/api/3/action/package_create",
    headers=headers,
    json=dataset_payload
)

if r.status_code != 200:
    # tenta atualizar
    r = requests.post(
        f"{CKAN_URL}/api/3/action/package_update",
        headers=headers,
        json=dataset_payload
    )

print("Dataset CKAN ok.")

# =============================
# Criar recursos
# =============================
for res in datapackage["resources"]:
    resource_payload = {
        "package_id": DATASET_NAME,
        "name": res["title"],
        "url": f"https://raw.githubusercontent.com/transparencia-mg/empregados_terceirizados/main/{res['path']}",
        "format": "CSV",
        "description": res["description"]
    }

    requests.post(
        f"{CKAN_URL}/api/3/action/resource_create",
        headers=headers,
        json=resource_payload
    )

print("Recursos publicados no CKAN.")
