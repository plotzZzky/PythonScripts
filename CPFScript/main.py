from CPFScript.validate import validate
from CPFScript.generate import generator
import art


class CPFMenu:

    def wellcome(self):
        art.tprint(f'{" " * 6} CpfScript', "tarty1")
        print("Os dados gerados por esse script são ficticios, usados apenas para fins acadmicos!")
        self.menu()

    def menu(self):
        print(f"{'_' * 38} Menu {'_' * 38}\n"
              "\n1- Validar matematicamente um cpf\n"
              "2- Gerar um cpf ficticio para teste em sistemas\n"
              )
        try:
            query = input("Digite a opção:\n")
            self.check_menu(query)
        except (ValueError, TypeError):
            print("Opção invalida!")
            self.menu()

    def check_menu(self, query):
        if query == '1':
            validate.get_cpf()
        elif query == '2':
            generator.check_uf()
        else:
            print("Opção não existe!\n")
        self.menu()


cpf = CPFMenu()

if __name__ == '__main__':
    cpf.wellcome()
