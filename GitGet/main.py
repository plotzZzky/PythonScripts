from pathlib import Path
import pathlib
import requests
import os
import sys
import art


class GitGet:
    # Script python para baixar repositorios de um usuario de uma conta do GitHub
    user: str = "Username"
    repos: list = []
    path: Path = None
    url: str = "url_do_github_do_user"

    def welcome(self):
        # Tela de apresentação do script
        art.tprint(f'{" " * 20} GitGet', "tarty")
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.find_user()

    def find_user(self):
        # Recebe o nome do usario e modifica a url com o username
        try:
            self.user: str = input("Digite o nome do usuario:\n")
            self.url: str = f"https://api.github.com/users/{self.user}/repos"
            self.get_repos()
        except KeyboardInterrupt:
            print("Saindo...")

    def get_repos(self):
        # Recebe a lista com todos os respositorios do usuario procurado
        response = requests.get(self.url)
        self.repos: dict = response.json()

        if response.status_code == 200:
            self.show_repos()
        else:
            print("Usuario não encontrado!")
            self.exit_menu()

    def show_repos(self):
        # Mostra todos os respos encontrados do usuario já formatados
        print("\nRepositorios encontrados:")
        n: int = 0
        for item in self.repos:
            n += 1
            print(f"{n}- {item['name']}")
        self.get_repos_option()

    def get_repos_option(self):
        # Menu para verificar quais os repos baixar
        # verifica se deseja salvar todos, alguns selecionados ou fechar o programa
        print(
            "\n'Enter' para baixar todos \n"
            "'N' para cancelar \n"
            "Numero dos repos separados por espaço \n"
        )
        option: str = input("Seleciona a opção \n").lower()
        option_list: list = option.split(" ")

        if option.lower() == "n":
            self.exit_menu()
        elif option.lower() == "":
            self.download_all_repos()
        else:
            self.selected_repos(option_list)

    # Função que gerencia os download dos repos e a criação de pastas
    # Chama a função para criar a pasta e a função de download para cada item selecionado
    def selected_repos(self, option):
        self.create_folder()
        try:
            for item in option:
                x: int = int(item) - 1
                url: str = f"{self.repos[x]['clone_url']}"
                name: str = self.repos[x]["name"]
                self.download_repo(url, name)
            self.exit_menu()
        except TypeError:
            pass

    def download_repo(self, url: str, name: str):
        # Baixa o repositorio selecionado através do git cli
        os.system(f"cd {self.path}; git clone {url}")
        print(f"Download {name} concluido!\n")

    def download_all_repos(self):
        # Função que baixa todos os respositorios do usuario selecionado
        self.create_folder()
        for item in self.repos:
            url: str = f"{item['clone_url']}"
            name: str = item["name"]
            self.download_repo(url, name)
        self.exit_menu()

    def create_folder(self):
        # Verifica se existe a pasta do programa existe, se não, cria a pasta para salvar os repos baixados
        home: Path = Path.home()
        self.path = pathlib.Path(f"{home}/GitGet/{self.user}/")
        self.path.mkdir(parents=True, exist_ok=True)

    # Menu para verificar se o usuario deseja fechar o programa
    # Caso o usuario queira fechar o programa e usuario executar este arquivo diretamente ele o fechara,
    # Do contrario voltara para o menu do PythonScripts
    def exit_menu(self):
        option: str = input("Deseja baixar mais repos?(Y/N)\n").lower()
        if option == "y":
            new: str = input("Do mesmo usuario?(Y/N)\n").lower()
            if new == "y":
                self.get_repos()
            else:
                self.find_user()
        else:
            if __name__ == "__main__":
                print("Saindo...")
                sys.exit()


gitget = GitGet()

if __name__ == "__main__":
    gitget.welcome()
