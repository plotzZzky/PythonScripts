import pathlib
import requests
import os
import sys
import art
from pathlib import Path

# Programa para baixar respositorios de um usario do github
class GitGet:
    def __init__(self):
        self.user = ""
        self.repos = []
        self.path = None
        self.url = ""

    # Tela de apresentação do programa
    def welcome(self):
        art.tprint(f'{" " * 20} GitGet', 'tarty')
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.find_user()

    # Recebe o nome do usario e modifica a url com o username
    def find_user(self):
        self.user = input("Digite o nome do usuario:\n")
        self.url = f"https://api.github.com/users/{self.user}/repos"
        self.get_repos()
        
    # Recebe a lista com todos os respositorios do usuario procurado
    def get_repos(self):
        response = requests.get(self.url)
        self.repos = response.json()

        if response.status_code == 200:
            if self.repos:
                self.show_repos()
            else:
                print("Nenhum repositorio encontrado!")
                self.exit_menu()
        else:
            print("Usuario não encontrado!")
            self.exit_menu()

    # Mostra todos os respos encontrados do usuario já formatados
    def show_repos(self):
        print("Repositorios encontrados:")
        n = 0
        for item in self.repos:
            n += 1
            print(f"{n}- {item['name']}")
        self.get_repos_option()

    # Menu para verificar quais os repos baixar, verifica se deseja salvar todos, alguns selecionados ou nehum
    def get_repos_option(self):
        option = input("Digite 'Enter' para baixar todos, "
                       "'N' para cancelar ou o numero dos repos separados por espaço:\n")
        option_list = option.split(" ")
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
                x = int(item) - 1
                url = f"{self.repos[x]['clone_url']}"
                name = self.repos[x]['name']
                self.download_repo(url, name)
            self.exit_menu()
        except TypeError:
            pass

    # Baixa o repositorio selecionado
    def download_repo(self, url, name):
        os.system(f"cd {self.path}; git clone {url}")
        print(f"Download {name} concluido!\n")

    # Função que baixa todos os respositorios do usuario selecionado
    def download_all_repos(self):
        self.create_folder()
        for item in self.repos:
            url = f"{item['clone_url']}"
            name = item['name']
            self.download_repo(url, name)
        self.exit_menu()

    # Verifica se existe a pasta do programa e cria a pasta para salvar os repos baixados
    def create_folder(self):
        home = Path.home()
        self.path = pathlib.Path(f"{home}/GitGet/{self.user}/")
        self.path.mkdir(parents=True, exist_ok=True)

    # Menu para verificar se o usuario deseja fechar o programa
    # Caso o usuario queira fechar o programa e usuario executar este arquivo diretamente ele o fechara, do contrario voltara para o menu do PythonScripts
    def exit_menu(self):
        option = input("Deseja baixar mais repos?(Y/N)\n").lower()
        if option == "y":
            new = input("Do mesmo usuario?(Y/N)\n").lower()
            if new == "y":
                self.get_repos()
            else:
                self.find_user()
        else:
            if __name__ == '__main__':
                sys.exit()


gitget = GitGet()

if __name__ == '__main__':
    gitget.welcome()
