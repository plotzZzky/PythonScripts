from pathlib import Path
import pathlib
import requests
import os
import sys
import art


class GitGet:
    # Script python para baixar repositorios de um usuario de uma conta do GitHub
    user_name: str = "Username"
    repos: list = []
    repo_folder: Path = None
    user_url: str = "url_do_github_do_user"

    def welcome(self):
        # Tela de apresentação do script
        art.tprint(f'{" " * 20} GitGet', "tarty")
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.find_user()

    def find_user(self):
        # Recebe o nome do usario e modifica a url com o username
        try:
            self.user_name: str = input("Digite o nome do usuario:\n")
            self.user_url: str = f"https://api.github.com/users/{self.user_name}/repos"
            self.get_repos_from_user()
        except KeyboardInterrupt:
            print("Saindo...")

    def get_repos_from_user(self):
        # Recebe a lista com todos os respositorios do usuario procurado
        response = requests.get(self.user_url)
        self.repos: dict = response.json()

        if response.status_code == 200:
            self.show_repos_from_user()
        else:
            print("Usuario não encontrado!")
            self.exit_menu()

    def show_repos_from_user(self):
        # Mostra todos os respos encontrados do usuario já formatados
        print("\nRepositorios encontrados:")
        for index, item in enumerate(self.repos, 1):
            print(f"{index}- {item['name']}")
        self.menu_download_option()

    def menu_download_option(self):
        # Menu para verificar quais os repos baixar
        # verifica se deseja salvar todos, alguns selecionados ou fechar o programa
        print(
            "\n'Enter' para baixar todos \n"
            "'N' para cancelar \n"
            "Numero dos repos separados por espaço \n"
        )
        option: str = input("Seleciona a opção \n").lower()
        option_list: list = option.split(" ")

        self.check_menu_download_option(option_list)

    def check_menu_download_option(self, option_list: list):
        if option_list[0].lower() == "n":
            self.exit_menu()
        elif option_list[0].lower() == "":
            self.download_all_repos()
        else:
            self.selected_repos(option_list)

    # Função que gerencia os download dos repos e a criação de pastas
    # Chama a função para criar a pasta e a função de download para cada item selecionado
    def selected_repos(self, options):
        self.create_folder()
        try:
            for item in options:
                index: int = int(item) - 1
                item_dict: dict = self.repos[index]
                url: str = item_dict['clone_url']
                name: str = item_dict["name"]

                self.download_repo(url, name)
            self.exit_menu()
        except TypeError:
            pass

    def download_repo(self, url: str, name: str):
        # Baixa o repositorio selecionado através do git cli
        os.system(f"cd {self.repo_folder}; git clone {url}")
        print(f"Download {name} concluido!\n")

    def download_all_repos(self):
        # Função que baixa todos os respositorios do usuario selecionado
        self.selected_repos(self.repos)

    def create_folder(self):
        # Verifica se existe a pasta do programa existe, se não, cria a pasta para salvar os repos baixados
        home_folder: Path = Path.home()
        self.repo_folder: Path = pathlib.Path(f"{home_folder}/GitGet/{self.user_name}/")
        self.repo_folder.mkdir(parents=True, exist_ok=True)

    def exit_menu(self):
        # Menu para verificar se o usuario deseja fechar o programa
        option: str = input("Deseja baixar mais repos?(Y/N)\n").lower()
        if option == "y":
            new: str = input("Do mesmo usuario?(Y/N)\n").lower()
            if new == "y":
                self.get_repos_from_user()
            else:
                self.find_user()
        else:
            if __name__ == "__main__":
                print("Saindo...")
                sys.exit()


gitget = GitGet()

if __name__ == "__main__":
    gitget.welcome()
