# scripts/publicar_ckan.py
import os
import subprocess

CKAN_URL = "https://www.dados.mg.gov.br"
DATASET_NAME = "empregados-terceirizados"

subprocess.run([
    "dpckan",
    "publish",
    "datapackage/datapackage.json",
    "--ckan-host", CKAN_URL,
    "--api-key", os.environ["CKAN_API_KEY"],
    "--dataset-name", DATASET_NAME,
    "--organization", "controladoria-geral-do-estado-cge",
    "--force"
], check=True)
