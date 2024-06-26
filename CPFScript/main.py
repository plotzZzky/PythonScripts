import sys

from CPFScript.validate import validate
from CPFScript.generate import generator
import art


class CPFMenu:

    def welcome(self):
        art.tprint(f'{" " * 6} CpfScript', "tarty1")
        print("Os dados gerados por esse script são ficticios, usados apenas para fins acadmicos!")
        self.menu()

    def menu(self):
        print(f"{'_' * 38} Menu {'_' * 38}")
        print(
              "1- Validar matematicamente um cpf\n"
              "2- Gerar um cpf ficticio para teste em sistemas\n"
              "3- Sair \n"
              )
        try:
            query: str = input("Digite a opção:\n").lower()
            self.check_menu(query)
        except (ValueError, TypeError):
            print("Opção invalida!")
            self.menu()
        except KeyboardInterrupt:
            print("Saindo...")

    def check_menu(self, query):
        if query == '1':
            validate.get_cpf()
        elif query == '2':
            generator.check_uf()
        elif query == '3':
            print("Saindo...")
        else:
            print("Opção não existe!\n")

        if __name__ == '__main__':
            self.menu()


cpf = CPFMenu()

if __name__ == '__main__':
    cpf.welcome()
