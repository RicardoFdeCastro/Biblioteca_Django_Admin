# 📚 Sistema de Biblioteca - Django Admin

Ferramenta profissional desenvolvida com **Python + Django Admin** para gestão de bibliotecas.  
Permite o **cadastro de funcionários, clientes, acervo de livros, empréstimos** e controle de **multas por atraso**.

---

## 🚀 Funcionalidades

- Cadastro de **funcionários**, **clientes** e **livros**.
- Registro de **empréstimos** e **devoluções**.
- Cálculo de **multas automáticas** para atrasos.
- Filtros no admin para status de empréstimos.
- Relatórios básicos de livros emprestados.
- Interface administrativa simplificada com o Django Admin.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **Django 5+**
- **SQLite** (banco de dados padrão)
- **django-import-export** (importação/exportação de dados)

---

## 📦 Instalação e uso

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/seu-repositorio.git
cd seu-repositorio

2️⃣ Criar e ativar ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Aplicar migrações do banco de dados
python manage.py migrate

5️⃣ Criar usuário administrador
python manage.py createsuperuser

6️⃣ Rodar o servidor
python manage.py runserver
Acesse no navegador: http://127.0.0.1:8000/admin

📂 Estrutura do projeto
biblioteca/
│── biblioteca/         # Configurações principais do Django
│── core/               # App principal com models, views e admin
│── templates/          # Templates HTML
│── manage.py           # Arquivo principal do Django
│── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo

📜 Licença
Este projeto está sob a licença MIT.
Você pode usá-lo livremente para fins pessoais e comerciais