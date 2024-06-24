# Esse script importa e inicia as classes que estão nos demais arquivos
from PyNance.data import GetData
from PyNance.graph import GraphClass
import art


class PynanceMenu:
    data = GetData()  # classe para preencher as informações dos graficos
    pies = GraphClass(data)

    def wellcome(self):
        art.tprint(f'{" " * 5} PyNance', "tarty1")
        print(f"{'=' * 80}")
        print("Script python para ajudar a gerenciar sua vida fineceira")
        print("Todos os valores devem ser preenchidos com valores inteiros ignorando os centavos\n")
        self.menu()

    def menu(self):
        print(
            "Selecione uma opção:\n"
            "1- Preencher com valores genericos para teste.\n"
            "2- Preencher manualmente"
        )
        option: str = input().lower()
        self.check_menu_option(option)

    def check_menu_option(self, option: str = None):
        if option == "1":
            self.data.test()
        else:
            self.data.get_income()
        self.pies.create_graph()


pynance = PynanceMenu()

if __name__ == "__main__":
    pynance.wellcome()
