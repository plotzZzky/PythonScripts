from itertools import chain, product
import art
import random
import string
import time
import os


# Programa para testar a reincidencia de uma senha e a segurança através de um brute force atack
class PasswordTest:
    def __init__(self):
        self.chars = None
        self.possibilities = []
        self.length = 3
        self.password = None
        self.start_time = 0
        self.end_time = 0
        self.result_time = 0
        self.attempts = 0
        self.result = None

    # Tela de boa vinda do programa
    def wellcome(self):
        art.tprint(f'{" " * 23} PasswordTest', "tarty2")
        print(f"{'-' * 28} Projeto feito por um estudante python {'-' * 26}")
        print(f"{' ' * 34}https://github.com/plotzZzky\n")
        self.menu()

    # Menu principal, para verificar qual a opção o usuario deseja executar
    def menu(self):
        print(
            f"{'.' * 44} Menu: {'.' * 43}\n"
            "1- BruteForce random password \n"
            "2- BruteForce your password \n"
            "3- Password incidence "
        )
        option = input("Choose a option: \n")
        match option:
            case "1":
                self.get_length()
                self.set_password_chars()
                self.test_random_pwd()
            case "2":
                self.set_password_chars()
                self.test_your_pwd()
            case "3":
                self.get_length()
                self.set_password_chars()
                self.test_your_pwd_frequency()
            case other:
                self.menu()

    # Recebe o tamanho da senha
    def get_length(self):
        try:
            self.length = int(input("Enter password length: \n"))
        except ValueError:
            self.set_password_chars()

    # Função para determinar os parametros para geração das senhas
    def set_password_chars(self):
        print(
            "Select password type: \n"
            "1- Only numbers \n"
            "2- Numbers and strings lowercase \n"
            "3- Numbers ans strings(lower and uppercase) \n"
            "4- Numbers strings e punctuation"
        )
        option = input("")
        match option:
            case "1":
                self.chars = string.digits
            case "2":
                self.chars = string.digits + string.ascii_lowercase
            case "3":
                self.chars = string.digits + string.ascii_letters
            case "4":
                self.chars = string.digits + string.ascii_letters + string.punctuation
            case _:
                self.chars = string.digits + string.ascii_letters

    # Gera a senha, com os parametros selecionados pelo usuario
    def generate_pwd(self):
        result = "".join(random.choice(self.chars) for i in range(self.length))
        return result

    # Função que retorna uma lista com todos os caracteres do tipo de senha selecionada, através dos parametros selecionados pelo usuario
    def get_all_elements(self):
        return (
            "".join(candidate)
            for candidate in chain.from_iterable(
                product(self.chars, repeat=z) for z in range(1, self.length + 1)
            )
        )

    # Inicia o timer para determinar o tempo para quebrar a senha
    def start_timer(self):
        print(f"working...")
        self.start_time = time.perf_counter()

    # Encera o timer
    def end_timer(self):
        self.end_time = time.perf_counter() - self.start_time

    # Função que executa o brute force atack
    def bruteforce(self):
        self.attempts = 0
        self.start_timer()
        while True:
            for x in self.possibilities:
                self.attempts += 1
                self.result = x
                if self.result == self.password:
                    self.end_timer()
                    self.show_result()
                    return False

    # Função que testa a reincidencia da senha
    def pwd_test(self):
        self.attempts = 0
        self.start_timer()
        while True:
            self.result = self.generate_pwd()
            if self.result == self.password:
                self.end_timer()
                self.show_result()
                return False

    # Verifica o tamanho da senha
    def check_pwd_length(self):
        if len(self.password) == self.length:
            pass
        else:
            print(
                "The password must have the maximum length informed in the script! \n"
            )
            self.menu()

    # Mostra os resultados dos testes
    def show_result(self):
        print(f'{"-" * 42} Eureka!! {"-" * 42}')
        print(f"The result is {self.result}")
        print(f"{self.attempts} attempts done - time {self.end_time:0.2f}")
        if __name__ == "__main__":
            self.menu()

    # Função que gera a senha randomica e executa a função do brute force attack
    def test_random_pwd(self):
        self.password = self.generate_pwd()
        print(f"Password = {self.password}\n")
        self.possibilities = self.get_all_elements()
        self.bruteforce()

    # Função que recebe a senha do usuario e executa a função do brute force attack
    def test_your_pwd(self):
        self.password = input("Your password:\n")
        self.length = len(self.password)
        self.check_pwd_length()
        self.possibilities = self.get_all_elements()
        self.bruteforce()

    # Função que recebe a senha do usuario e chama a função que testa a reincidencia
    def test_your_pwd_frequency(self):
        self.password = input("Your password:\n")
        self.check_pwd_length()
        self.pwd_test()


pwd = PasswordTest()
if __name__ == "__main__":
    pwd.wellcome()
