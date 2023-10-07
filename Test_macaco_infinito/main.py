import random
import string
import time
import sys


class App:
    def __init__(self):
        self.name = 'Simulador do Teorema do macaco infinito'
        self.chars = string.ascii_lowercase + string.whitespace
        self.phrase = ""
        self.length = 0
        self.number = 0
        self.start_time = 0
        self.end_time = 0

    def wellcome(self):
        print(f"{'-' * 25} {self.name} {'-' * 25}")
        print("\nIMPORTANTE:\nEste script foi feito apenas para fins de interterimento sem nehhum foco científico "
              "ou acadêmico.\n")
        self.get_phrase()

    def get_phrase(self):
        self.phrase = input("Digite a sequencia a ser obtida(contendo apenas letras minusculas e espaços):\n").lower()
        self.length = len(self.phrase)
        self.test_phrase()

    # check if a phrase is ok
    def test_phrase(self):
        test_phrase = self.phrase.replace(" ", "")
        if test_phrase.isalpha() and test_phrase.isascii():
            self.test_word()
        else:
            pass
            print("NÂO SÂO PERMITIDOS ACENTOS, SINAIS OU NUMEROS!!!\n")
            self.get_phrase()

    # Timer
    def start_timer(self):
        self.start_time = time.perf_counter()

    def end_timer(self):
        self.end_time = time.perf_counter() - self.start_time

    # Create random phrase
    def generate_word(self):
        result = ''.join(random.choice(self.chars) for i in range(self.length))
        print(result)
        return result

    # check if a phrase is correct
    def test_word(self):
        self.start_timer()
        while True:
            self.number += 1
            print(f"Tentativa {self.number}")
            result = self.generate_word()
            if result == self.phrase:
                self.show_result()
                return False

    def show_result(self):
        self.end_timer()
        print(f"{'-' * 40} Eureka! {'-' * 40}")
        print(f"\nO tempo necessario foi de {self.end_time:0.2f} segundos")
        print(f"Foram feitas {self.number} tentativas ate o resultado '{self.phrase}'")
        self.close_menu()

    def close_menu(self):
        response = input("Deseja tenatar novamente?(Y/N) \n").upper()
        if response == "Y":
            self.wellcome()
        else:
            if __name__ == '__main__':
                sys.exit()


monkey = App()

if __name__ == '__main__':
    monkey.wellcome()
