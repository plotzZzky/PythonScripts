from CPFScript.main import cpf
from DjangoForge.main import forge
from EmailSender.main import email_creator
from FindCompanyInfo.main import find
from GitGet.main import gitget
from IPInspector.main import ip
from PasswordTest.main import pwd
from Tpass.main import tpass
from PyGraphy.main import pygraphy
from PyNance.main import pynance
from PySystem.main import pysystem
from SimpleRansomware.main import ransomware
from TeamReport import main as teamreport
import art


# Menu para executar um dos scripts desse projeto
class Menu:
    def __init__(self):
        self.apps = [
            "CpfScript",
            "DjangoForge",
            "EmailSender",
            "FindCompanyInfo",
            "GitGet",
            "IPInspector",
            "PasswordTest",
            "PyGraphy",
            "PyNance",
            "PySytem",
            "SimpleRansomware",
            "TeamReport",
            "Tpass",
        ]
        self.print_space = f"{'-' * 36}"

    # Tela de apresentação
    def wellcome(self):
        art.tprint(f'{" " * 13} Python', "tarty1")
        art.tprint(f'{" " * 13} Scripts', "tarty1")
        self.menu()

    # Menu com a lista de apps disponivel
    def menu(self):
        print(f"{self.print_space} Menu {self.print_space}\n")
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
                self.wellcome()
        except ValueError:
            print("Opção incorreta!\n")
            self.wellcome()

    # Executa o script selecionado pelo usuario
    def open_app(self, option):
        funcs = [
            cpf.wellcome,
            forge.wellcome,
            email_creator.wellcome,
            find.wellcome,
            gitget.welcome,
            ip.wellcome,
            pwd.wellcome,
            pygraphy.wellcome,
            pynance.wellcome,
            pysystem.wellcome,
            ransomware.alert,
            teamreport.start,
            tpass.wellcome,
        ]
        try:
            user_option = option - 1
            funcs[user_option]()
        except (KeyError, ValueError):
            pass
        self.wellcome()


menu = Menu()
menu.wellcome()
