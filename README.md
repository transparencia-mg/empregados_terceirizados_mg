# 📊 Dashboard de Empregados Terceirizados – Governo de Minas Gerais

Dashboard interativo para visualização, consulta e download de dados públicos sobre **empregados terceirizados** do Governo do Estado de Minas Gerais, com base em arquivos CSV padronizados e publicação em dados abertos.

---

## 🔍 Visão Geral

Este projeto disponibiliza um **dashboard web público** para consulta e análise dos dados de empregados terceirizados do Governo de Minas Gerais. A solução permite o acompanhamento transparente das informações, com foco em organização, atualização e reutilização dos dados.

Principais funcionalidades:

- Visualização agregada por **órgão**, **empresa** e **cargo**
- Consulta individual de empregados terceirizados
- Carregamento automático de dados a partir de arquivos CSV
- Exportação dos dados filtrados
- Integração com repositório GitHub e dados abertos (CKAN)
- Atualização contínua conforme novos arquivos são adicionados

---

## 🌐 Acesso Online

O dashboard está disponível publicamente em:

👉 **https://transparencia-mg.github.io/empregados_terceirizados_mg/**

Não é necessário login ou autenticação para acesso aos dados.

---

## 🗂️ Estrutura dos Dados

Os dados são organizados em arquivos CSV anuais.

Cada arquivo representa os empregados terceirizados referentes ao respectivo ano.

---

## ⚙️ Atualização dos Dados

A atualização do dashboard ocorre a partir da inclusão ou substituição de arquivos CSV na pasta `data/`.

Fluxo padrão de atualização:

1. Inclusão ou atualização do arquivo CSV
2. Geração automática do `datapackage.json`
3. Versionamento no GitHub
4. Atualização automática do dashboard

Esse fluxo garante rastreabilidade, transparência e consistência dos dados publicados.

---

## 📦 Dados Abertos

Os dados deste projeto seguem o padrão **Data Package**, permitindo:

- Versionamento dos recursos
- Reutilização por outros sistemas
- Publicação em plataformas de dados abertos (CKAN)

---

## 🛠️ Tecnologias Utilizadas

- **HTML5 / CSS3 / JavaScript**
- **DataTables**
- **Chart.js**
- **GitHub Pages**
- **CSV padronizado**
- **Data Package / dpckan**

---

## 📄 Licença

Os dados e o código deste repositório são disponibilizados sob a licença:

**Creative Commons Attribution 4.0 (CC-BY-4.0)**  

É permitida a reutilização dos dados, desde que citada a fonte.

---

## 🏛️ Órgão Responsável

**Controladoria-Geral do Estado de Minas Gerais (CGE-MG)**  
Projeto alinhado às diretrizes de transparência pública e dados abertos do Governo de Minas Gerais.
