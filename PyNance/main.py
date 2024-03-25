# Esse script importa e inicia as classes que estão nos demais arquivos
from PyNance.data import GetData
from PyNance.graph import GraphClass
import art


class PynanceMenu:
    @staticmethod
    def wellcome():
        art.tprint(f'{" " * 5} PyNance', "tarty1")
        print(f"{'=' * 80}")
        print("Script python para ajudar a gerenciar sua vida fineceira")
        print(
            "Todos os valores devem ser preenchidos com valores inteiros ignorando os centavos\n"
        )
        option = input(
            "Digite Y para preencher os valores ou qualquer tecla para testar a ferramenta "
            "com valores genericos\n"
        ).lower()
        if option == "y":
            data.get_income()
        else:
            data.test()
        pies.create_graph()


data = GetData()
pies = GraphClass(data)
pynance = PynanceMenu()


if __name__ == "__main__":
    pynance.wellcome()
