import sys


class PyCli:
    """ Modelo de BoilerPlate de appcli feito em python """
    APP_NAME: str = 'PyCli'
    APP_DESC: str = "Um BoilerPlate simples de cliapp feito em python"

    def __init__(self):
        # O init é necessario para usar o self
        self.menu_options = [
            self.first_function,
            self.second_function,
        ]

    def welcome(self):
        print(f"{' ' * 35} {self.APP_NAME}")
        print(self.APP_DESC)
        self.start_menu()

    def start_menu(self):
        print(f"{'__' * 18} Menu {'__' * 18}")

        for index, option in enumerate(self.menu_options, 1):
            print(f"{index}- {option.__name__}")

        self.check_start_menu_option()

    def check_start_menu_option(self):
        try:
            option: int = int(input("\nSelecione uma opção:\n")) - 1
            self.menu_options[option]()  # chama a função selecionada

        except (ValueError, IndexError):
            print('\nOpção invalida!!!!!\n')
            self.start_menu()
        except KeyboardInterrupt:
            print("\nSaindo...")

    def first_function(self):
        print("Function1")
        self.exit_menu()

    def second_function(self):
        print("Function2")
        self.exit_menu()

    def exit_menu(self):
        try:
            option: str = input("\nSair?(Y/N)\n").upper()
            self.check_exit_menu_option(option)
        except KeyboardInterrupt:
            sys.exit()

    def check_exit_menu_option(self, option: str):
        if option == 'Y':
            sys.exit()
        else:
            self.start_menu()


app = PyCli()

if __name__ == '__main__':
    app.welcome()
