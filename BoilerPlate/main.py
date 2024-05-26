import sys


class PyCli:
    """ Modelo de BoilerPlate de appcli feito em python """
    name = 'PyCli'
    desc = "Um BoilerPlate simples de cliapp via terminal feito em python"

    def __init__(self):
        self.menu_options = [
            self.first_function,
            self.second_function,
        ]

    def wellcome(self):
        print(f"{' ' * 30} {self.name}")
        print(self.desc)
        self.start_menu()

    def start_menu(self):
        print(f"{'__' * 16} Menu {'__' * 16}")

        for index, option in enumerate(self.menu_options, 1):
            print(f"{index}- {option.__name__}")

        self.check_start_menu_option()

    def check_start_menu_option(self):
        try:
            option = int(input("\nSelecione uma opção:\n"))
            self.menu_options[option - 1]()  # chama a função selecionada

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
            option = input("\nSair?(Y/N)\n")

            if option.lower() == 'y':
                sys.exit()
            else:
                self.start_menu()

        except KeyboardInterrupt:
            print("\nSaindo...")


app = PyCli()

if __name__ == '__main__':
    app.wellcome()
