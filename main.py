from DjangoForge.main import djangoForge
from GitGet.main import gitget
from IPInspector.main import ip
from PasswordTest.main import pwd
from Tpass.main import tpass
from PyNance.main import pynance
from Team_Report.main import report
import art


# Menu para executar um dos scripts desse projeto
class Menu:
    def __init__(self):
        self.apps = [
            "DjangoForge",
            "PyNance",
            "GitGet",
            "IPInspector",
            "PasswordTest",
            "Team Report",
            "Tpass",
        ]
        self.print_space = f"{'-_' * 20}"

    # Tela de apresentação
    def wellcome(self):
        art.tprint(f'{" " * 9} PythonScripts \n', "tarty4")
        self.menu()

    # Menu com a lista de apps disponivel
    def menu(self):
        print(f"{self.print_space} Menu {self.print_space}")
        print("Selecione uma opção para executar o script:")
        number = 0
        for item in self.apps:
            number += 1
            print(f"{number}- {item}")
        self.get_option()

    # Recebe a escolha do usuario e verifica se esta entre as opções disponiveis
    def get_option(self):
        option = input("\nEscolha uma opção:\n")
        try:
            number = int(option)
            if number <= len(self.apps):
                self.open_app(number)
            else:
                print("Opção incorreta!")
                self.menu()
        except ValueError:
            print("Opção incorreta!\n")
            self.menu()

    # Executa o script selecionado pelo usuario
    def open_app(self, option):
        funcs = [
            djangoForge.wellcome,
            gitget.welcome,
            ip.wellcome,
            pwd.wellcome,
            pynance.wellcome,
            report.wellcome,
            tpass.wellcome,
        ]
        try:
            user_option = option - 1
            funcs[user_option]()
        except (KeyError, ValueError):
            pass
        menu.menu()


menu = Menu()
menu.wellcome()
