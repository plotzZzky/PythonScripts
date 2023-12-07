from DjangoForge.main import djangoForge
from GitGet.main import gitget
from IPInspector.main import ip
from PasswordTest.main import pwd
from Test_macaco_infinito.main import monkey
import art


# Menu para executar um dos scripts desse projeto
class Menu:
    def __init__(self):
        self.apps = ["DjangoForge",
                     "GitGet",
                     "IPInspector",
                     "PasswordTest"]
        self.print_space = f"{'-_' * 20}"

    # Tela de apresentação
    def wellcome(self):
        art.tprint(f'{" " * 9} PythonScripts \n', 'tarty4')
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
    def open_app(self, number):
        if number == 1:
            djangoForge.wellcome()
        elif number == 2:
            gitget.welcome()
        elif number == 3:
            ip.wellcome()
        elif number == 4:
            pwd.wellcome()
        else:
            self.menu()
        self.wellcome()


menu = Menu()
menu.wellcome()
