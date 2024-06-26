import sys
from itertools import chain, product
import art
import random
import string
import time


class PasswordTest:
    # Programa para testar a reincidencia de uma senha e a segurança através de um brute force attack
    chars_type: str = []
    all_chars: list = []  # lista com todas os characteres possiveis pelo tipo de senha escolhido
    pwd_length: int = 0
    password: str = None

    start_time: float = 0
    end_time: float = 0
    result_time: float = 0

    attempts_number: int = 0
    result: str = None

    def welcome(self):
        # Tela de boa vinda do programa
        art.tprint(f'{" " * 23} PasswordTest', "tarty2")
        print(f"{'-' * 28} Projeto feito por um estudante python {'-' * 26}")
        print(f"{' ' * 34}https://github.com/plotzZzky\n")
        self.start_menu()

    def start_menu(self):
        # Menu principal, para verificar qual a opção o usuario deseja executar
        print(
            f"{'.' * 44} Menu: {'.' * 43}\n"
            "1- BruteForce random password \n"
            "2- BruteForce your password \n"
            "3- Password incidence \n"
            "4- Exit"
        )
        try:
            option: str = input("Choose a option: \n")
            self.check_menu_option(option)
        except KeyboardInterrupt:
            print("Saindo...")

    def check_menu_option(self, option: str):
        # Verifica qual a opção escolida pelo usuario
        match option:
            case "1":
                self.get_length()
                self.menu_set_password_chars()
                self.test_random_pwd()
            case "2":
                self.menu_set_password_chars()
                self.test_your_pwd()
            case "3":
                self.get_length()
                self.menu_set_password_chars()
                self.test_your_pwd_frequency()
            case "4":
                print("Saindo...")
                if __name__ == '__main__':
                    sys.exit()
            case _:
                self.start_menu()

    def get_length(self):
        # Recebe o tamanho da senha do usuario
        try:
            self.pwd_length = int(input("Enter password length: \n"))
            if self.pwd_length <= 0:
                raise ValueError
        except ValueError:
            print("Invalid value!")
            self.get_length()

    def menu_set_password_chars(self):
        # Função para determinar os parametros para geração das senhas
        print(
            "Select password type: \n"
            "1- Only numbers \n"
            "2- Numbers and strings lowercase \n"
            "3- Numbers ans strings(lower and uppercase) \n"
            "4- Numbers strings e punctuation"
        )
        try:
            option: str = input("")
            self.check_menu_password_chars(option)
        except KeyboardInterrupt:
            print("Saindo...")

    def check_menu_password_chars(self, option: str):
        # Verifica que tipo de senha o usuario quer
        match option:
            case "1":
                self.chars_type = string.digits
            case "2":
                self.chars_type = string.digits + string.ascii_lowercase
            case "3":
                self.chars_type = string.digits + string.ascii_letters
            case "4":
                self.chars_type = string.digits + string.ascii_letters + string.punctuation
            case _:
                print("\nInvalid option!\n")
                self.menu_set_password_chars()

    def generate_pwd(self) -> str:
        # Gera a senha, com os parametros selecionados pelo usuario
        result = "".join(random.choice(self.chars_type) for _ in range(self.pwd_length))
        return result

    def get_all_elements(self) -> list:
        # Retorna uma lista com todos os caracteres do tipo de senha selecionada
        all_chars = [
            "".join(char)
            for char in chain.from_iterable(
                product(self.chars_type, repeat=z) for z in range(1, self.pwd_length + 1)
            )
        ]
        return all_chars

    def start_timer(self):
        # Inicia o timer para determinar o tempo para quebrar a senha
        print(f"working...")
        self.start_time = time.perf_counter()

    def end_timer(self):
        # Encera o timer
        self.end_time = time.perf_counter() - self.start_time

    def bruteforce(self):
        # Função que executa o brute force atack
        self.attempts_number = 0
        self.start_timer()
        while True:
            for x in self.all_chars:
                self.attempts_number += 1
                self.result = x
                if self.result == self.password:
                    self.end_timer()
                    self.show_result()
                    return False

    def pwd_test(self):
        # Função que testa a reincidencia da senha
        self.attempts_number = 0
        self.start_timer()
        while True:
            self.result = self.generate_pwd()
            self.attempts_number += 1
            if self.result == self.password:
                self.end_timer()
                self.show_result()
                return False

    def check_pwd_length(self):
        # Verifica o tamanho da senha
        if len(self.password) == self.pwd_length:
            self.pwd_length = len(self.password)
        else:
            print("The password must have the maximum length informed in the script!\n")
            self.start_menu()

    def show_result(self):
        # Mostra os resultados dos testes
        result_time = f"{self.end_time:0.2f}" if self.end_time > 0.01 else 'less than 0.01 second'

        print(f'{"-" * 42} Eureka!! {"-" * 42}')
        print(f"The result is {self.result}")
        print(f"{self.attempts_number} attempts done - time: {result_time}")
        if __name__ == "__main__":
            self.start_menu()

    def test_random_pwd(self):
        # Função que gera a senha randomica e executa a função do brute force attack
        self.password = self.generate_pwd()
        print(f"Password = {self.password}\n")
        self.all_chars = self.get_all_elements()
        self.bruteforce()

    def test_your_pwd(self):
        # Função que recebe a senha do usuario e executa a função do brute force attack
        self.password = input("Your password:\n")
        self.check_pwd_length()
        self.all_chars = self.get_all_elements()
        self.bruteforce()

    def test_your_pwd_frequency(self):
        # Função que recebe a senha do usuario e chama a função que testa a reincidencia
        self.password = input("Your password:\n")
        self.check_pwd_length()
        self.pwd_test()


pwd = PasswordTest()

if __name__ == "__main__":
    pwd.welcome()
