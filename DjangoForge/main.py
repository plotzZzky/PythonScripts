import os
import subprocess
from pathlib import Path
import art

# Conteudo do arquivo do django system/urls.py
urls_system = f"""from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]"""

# Conteudo base dos aqruivos urs.py dos apps
urls_base = """from django.urls import path

from . import views


urlpatterns = [
    path('', views, name=''),
]
"""


# Script apara automatizar o processo de criação de projetos com Django
class DjangoForge:
    def __init__(self):
        # Edit this
        self.terminal = "xfce4-terminal"

        self.BASE_DIC = os.getcwd()
        self.project_name = None

        # folders
        self.folder = ""
        self.back_folder = ""

        self.list_apps = ["users", "core"]
        self.requirements = [
            "django",
            "psycopg2",
        ]
        self.requirements_text = ""

        self.venv_commands = ""
        self.front_command = None
        self.new_line = ""

        self.react_front = ""
        self.rest = ""

    # Apresentação do script
    def wellcome(self):
        art.tprint(f'{" " * 5} DjangoForge', "tarty1")
        print(f"{'-' * 36} https://github.com/plotzzzky {'-' * 36}\n")
        print(
            "Este script automatiza parte do processo de criação de projetos com django\n"
        )
        self.get_project_name()

    # Recebe o nome do projeto via input
    def get_project_name(self):
        self.project_name = input("Digite o nome do projeto:\n")
        self.folder = f"{self.BASE_DIC}/{self.project_name}/"
        self.get_requirements()

    # Recebe a lista de requirements do projeto via input e os adiciona na lista base
    def get_requirements(self):
        query = input("Digite os requisitos do seu projeto separados por espaços\n")
        r = query.split()
        self.requirements.extend(r)
        self.get_app_list()

    # Recebe a lista de apps do django via input
    def get_app_list(self):
        query = input(
            "Digite o nome dos apps para adicionar a seu projeto separados por espaços\n"
            "apps padrao: core e users\n"
        )
        apps = query.split()
        self.list_apps.extend(apps)
        self.create_project_folder()

    # Cria as pastas do projeto
    def create_project_folder(self):
        self.back_folder = f"{self.folder}back/"

        Path.mkdir(Path(self.folder))
        Path.mkdir(Path(self.back_folder))
        self.create_frontend()

    # Menu para verificar como sera feito o front, e cria o comando para a geração do mesmo
    def create_frontend(self):
        self.react_front = input("Criar o frontend com react(Y/n):\n").upper()
        if self.react_front == "Y":
            self.rest = input("Instalar Django-rest-framework?(Y/n):\n").upper()
            self.front_command = (
                f"cd {self.folder}; npm create vite@latest front -- --template react;"
                f" mkdir front/src/elements/"
            )
        self.check_if_install_djangorestframework()

    # Menu para verificar se o usario quer instalar o DRF
    def check_if_install_djangorestframework(self):
        if self.rest == "Y":
            self.requirements.extend(["django-cors-headers", "djangorestframework"])
        self.create_requirements()

    # Cria o arquivo requirements.txt a adiciona os items da variavel requiremets_text
    def create_requirements(self):
        r = [f"{item}\n" for item in self.requirements]
        self.requirements_text = "".join(r)
        with open(f"{self.back_folder}requirements.txt", "w") as file:
            file.write(self.requirements_text)
            file.close()
        self.venv_commands = f"python3 -m venv venv; source venv/bin/activate; pip install -r requirements.txt"
        self.create_venv()

    # Cria o anbiente virtual do python e instala as dependencia do back do projeto
    def create_venv(self):
        create_apps = self.create_apps_command()
        create_project = (
            f"django-admin startproject system .; touch .gitignore; cd system/;"
            f'echo "{urls_system}" > urls.py'
        )
        subprocess.call(
            [
                f"{self.terminal}",
                "-x",
                "sh",
                "-c",
                f"{self.front_command}; cd {self.back_folder};"
                f" {self.venv_commands}; {create_project}; {create_apps}",
            ]
        )
        self.create_list_apps_to_project()

    # Cria a lista de apps do projeto
    def create_list_apps_to_project(self):
        path = f"{self.back_folder}system/settings.py"
        list_apps = [f"    '{item}',\n" for item in self.list_apps]
        rest = [
            "    'corsheaders',\n",
            "    'rest_framework',\n",
            "    'rest_framework.authtoken',\n",
        ]
        if self.rest == "Y":
            list_apps.extend(rest)
        new_line = "".join(list_apps)
        self.insert_apps_in_project_settings(path, new_line)

    # Adiciona a lista de apps ao settings do django
    def insert_apps_in_project_settings(self, path, new_line):
        with open(path, "r") as in_file:
            buf = in_file.readlines()

        with open(path, "w") as out_file:
            for line in buf:
                if line == "    'django.contrib.staticfiles',\n":
                    line = line + new_line
                out_file.write(line)

    # Gera o comando para criar os apps do django (django-admin startapp app_name)
    def create_apps_command(self):
        apps = [self.create_commands_for_app(item) for item in self.list_apps]
        return "".join(apps)

    # Cria o app do django e adiciona o arquivo com as urls de cada app e o conteudo base
    def create_commands_for_app(self, item):
        if item == "users":
            text = f'cd {self.back_folder}; django-admin startapp {item}; cd {item}/; echo "{urls_base}" > urls.py;'
        else:
            text = f'cd {self.back_folder}; django-admin startapp {item}; cd {item}/; echo "{urls_base}" > urls.py;'
        if self.react_front != "Y":
            return (
                text
                + f"mkdir templates/; mkdir static/; touch static/{item}.css; cd static/; mkdir js/;"
            )
        return text


djangoForge = DjangoForge()

if __name__ == "__main__":
    djangoForge.wellcome()
