from BoilerPlate.boilerplate import CliBoilerplate


class MyTestApp(CliBoilerplate):
    def __init__(self):
        super().__init__()
        self.CLI_DESC = "Test de app usando o CliBoilerplate"

        self.menu_options = [
            self.exemple_function,
            self.another_exemple_function,
        ]

    @staticmethod
    def exemple_function():
        print("New exemple function!")

    @staticmethod
    def another_exemple_function():
        print("Another exemple function!")


app = MyTestApp()

if __name__ == "__main__":
    app.main_loop()
