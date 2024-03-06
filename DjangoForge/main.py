import art
from rich import print
from pathlib import Path
import os


from DjangoForge.variables import urls_base, urls_system, settings


class DjangoForge:
    def __init__(self):
        # Edit this
        self.terminal = "xfce4-terminal"

        self.BASE_DIC = Path('DjangoForge').cwd()
        self.project_name = None
        self.api = False

        # folders
        self.folder = None
        self.back_folder = None
        self.front_folder = None

        self.list_apps = ["users"]
        self.requirements = [
            "django",
            "psycopg2-binary",
        ]
        self.requirements_text = ""

        self.venv_commands = ""
        self.front_command = None
        self.new_line = ""

        self.react_front = ""
        self.rest = ""

    def wellcome(self):
        art.tprint(f'{" " * 5} DjangoForge', "tarty1")
        print(f"{'-' * 36} https://github.com/plotzzzky {'-' * 36}\n")
        print(
            "Este script automatiza parte do processo de criação de projetos com django e React.js\n"
        )
        self.get_project_name()

    # recebe o no o nome do projeto
    def get_project_name(self):
        self.project_name = input("Digite o nome do projeto:\n")
        self.folder = f"{self.BASE_DIC}/{self.project_name}/"
        self.check_if_api()

    # Verifica se deseja criar o front e o back separados
    def check_if_api(self):
        query = input("Criar front e back separados?[Y/N]:\n").lower()
        self.api = True if query == 'y' else False

        if self.api:
            self.requirements.extend(["djangorestframework", "django-cors-headers"])
        self.get_requirements()

    # Recebe a lista de requirements do projeto via input e os adiciona na lista base
    def get_requirements(self):
        query = input(
            'Digite os pacotes a serem instalados no back, separados por ",":\n'
        )
        if query:
            self.requirements.extend(query.split(","))
        self.get_app_list()

    # Recebe a lista de apps do django via input
    def get_app_list(self):
        print('Digite o nome dos apps para adicionar a seu projeto separados por ",":\n')
        query = input(
            "apps padrao: users\n"
        )
        if query:
            self.list_apps.extend(query.split(","))
        self.create_back_folder()

    # Cria as pastas do back
    def create_back_folder(self):
        if self.api:
            """ Se for api cria pasta project/back/ e project/front/"""
            self.back_folder = f"{self.folder}back/"
            Path.mkdir(Path(self.folder))
        else:
            """ se não cria apenas a past project/ """
            self.back_folder = self.folder

        Path.mkdir(Path(self.back_folder))
        self.create_requirements()

    # cria o requirements.txt com os pacotes necessarios
    def create_requirements(self):
        r = [f"{item}\n" for item in self.requirements]
        self.requirements_text = "".join(r)
        with open(f"{self.back_folder}requirements.txt", "w") as file:
            file.write(self.requirements_text)
            file.close()
        self.create_back()

    def create_back(self):
        commands = (
            f"python3 -m venv {self.back_folder}.venv; "
            f"source {self.back_folder}.venv/bin/activate; "
            f"pip install -r {self.back_folder}requirements.txt; "
            f"touch {self.back_folder}.gitignore;"
            f"django-admin startproject system {self.back_folder}.",
            f"echo '{urls_system}' > {self.back_folder}system/urls.py",
        )
        for command in commands:
            os.system(command)
        self.create_apps()

    # Chama a função para criar o django-app para cada app na lista
    def create_apps(self):
        for app in self.list_apps:
            self.app_command(app)
        self.insert_apps_in_project_settings()

    # cria os django-app escolhidos pelo usuario
    def app_command(self, app):
        commands = [
            f"source {self.back_folder}.venv/bin/activate; cd {self.back_folder}; ./manage.py startapp {app}; "
            f"echo '{urls_base}' > {self.back_folder}{app}/urls.py"
        ]
        if not self.api:
            commands.append(f"mkdir {self.back_folder}{app}/templates; mkdir {self.back_folder}{app}/static")
        for command in commands:
            os.system(command)

    # Adiciona a lista de apps ao settings do django
    def insert_apps_in_project_settings(self):
        apps = "".join([f"    '{item}',\n" for item in self.list_apps])
        db_name = f"{self.project_name}_test"
        settings_content = settings.replace('{apps}', apps).replace('{db_name}', db_name)
        os.system(f'echo "{settings_content}" > {self.back_folder}system/settings.py')

        if self.api:
            self.create_front_folder()

    # Cria as pastas do front
    def create_front_folder(self):
        self.front_folder = f"{self.folder}front/"
        Path.mkdir(Path(self.front_folder))
        self.create_front()

    def create_front(self):
        commands = (
            "exit()",
            f"cd {self.front_folder} "
            f"&& npx create-next-app . --js --use-npm --eslint --no-src-dir --app --no-tailwind --import-alias @comps/*"
            f"&& npm install"
        )
        for command in commands:
            os.system(command)


forge = DjangoForge()
if __name__ == '__main__':
    forge.wellcome()
