import pathlib
import requests
import os
import sys
import art
from pathlib import Path


class GitGet:
    def __init__(self):
        self.user = ""
        self.repos = []
        self.path = None
        self.url = ""

    def welcome(self):
        art.tprint(f'{" " * 20} GitGet', 'tarty')
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.find_user()

    def find_user(self):
        self.user = input("Digite o nome do usuario:\n")
        self.url = f"https://api.github.com/users/{self.user}/repos"
        self.get_repos()

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

    def show_repos(self):
        print("Repositorios encontrados:")
        n = 0
        for item in self.repos:
            n += 1
            print(f"{n}- {item['name']}")
        self.get_repos_option()

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

    def download_repo(self, url, name):
        os.system(f"cd {self.path}; git clone {url}")
        print(f"Download {name} concluido!\n")

    def download_all_repos(self):
        self.create_folder()
        for item in self.repos:
            url = f"{item['clone_url']}"
            name = item['name']
            self.download_repo(url, name)
        self.exit_menu()

    def create_folder(self):
        home = Path.home()
        self.path = pathlib.Path(f"{home}/GitGet/{self.user}/")
        self.path.mkdir(parents=True, exist_ok=True)

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
