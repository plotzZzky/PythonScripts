from CPFScript.main import cpf
from DjangoForge.main import forge
from EmailSender.main import email_creator
from FindCompanyInfo.main import find
from GitGet.main import gitget
from IPInspector.main import ip
from PasswordTest.main import pwd
from ProjectCreator.main import menu as projectcreator
from PyGraphy.main import pygraphy
from PyNance.main import pynance
from PyRecord.main import pyrecord
from PySystem.main import pysystem
from SimpleRansomware.main import ransomware
from TeamReport import main as teamreport
from YouSave.main import yousave
import art


class Menu:
    # Menu para executar um dos scripts desse projeto
    def __init__(self):
        self.apps: list = [
            "CpfScript",
            "DjangoForge",
            "EmailSender",
            "FindCompanyInfo",
            "GitGet",
            "IPInspector",
            "PasswordTest",
            "ProjectCreator",
            "PyGraphy",
            "PyNance",
            "PyRecord",
            "PySystem",
            "SimpleRansomware",
            "TeamReport",
            "YouSave",
        ]

        self.funcs: list = [
            cpf.welcome,
            forge.welcome,
            email_creator.welcome,
            find.welcome,
            gitget.welcome,
            ip.welcome,
            pwd.welcome,
            projectcreator.welcome,
            pygraphy.welcome,
            pynance.welcome,
            pyrecord.welcome,
            pysystem.welcome,
            ransomware.alert,
            teamreport.start,
            yousave.welcome,
        ]

        self.print_space: str = f"{'-' * 36}"

    def welcome(self):
        # Tela de apresentação
        art.tprint(f'{" " * 13} Python', "tarty1")
        art.tprint(f'{" " * 13} Scripts', "tarty1")
        self.menu()

    def menu(self):
        # Menu com a lista de apps disponivel
        print(f"{self.print_space} Menu {self.print_space}\n")
        print("Selecione uma opção para executar o script:")

        for index, item in enumerate(self.apps, 1):
            print(f"{index}- {item}")
        self.get_option()

    def get_option(self):
        # Recebe a escolha do usuario e verifica se esta entre as opções disponiveis
        option: str = input("\nEscolha uma opção:\n")
        try:
            number: int = int(option)
            if 1 <= number <= len(self.apps):
                self.open_app(number)
            else:
                print("Opção incorreta!")
                self.welcome()
        except ValueError:
            print("Opção incorreta!\n")
            self.welcome()

    def open_app(self, option):
        # Executa o script selecionado pelo usuario
        try:
            self.funcs[option - 1]()
        except (KeyError, ValueError):
            pass
        self.welcome()


menu = Menu()
if __name__ == '__main__':
    menu.welcome()
