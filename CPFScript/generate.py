import random
import art


class CpfGenerator:
    """
        Script que gera cpfs para uso em teste de sites ou sistemas
        !!! Importante esses cpfs são !!!FICTICIOS!!! servindo apenas para testes!!!
    """
    ufs = {
        "0": ['RS'],
        "1": ["DF", "GO", "MS", "MT", "TO"],
        "2": ["AC", "AM", "AP", "PA", "RO", "RR"],
        "3": ["CE", "MA", "PI"],
        "4": ["AL", "PB", "PE", "RN"],
        "5": ["BA", "SE"],
        "6": ["MG"],
        "7": ["ES", "RJ"],
        "8": ["SP"],
        "9": ["PR", "SC"]
    }

    def welcome(self):
        art.tprint(f'{" " * 2 } CPFGenerator', "tarty1")
        print(f"{'-' * 38} https://github.com/plotzzzky {'-' * 38}\n")
        print("IMPORTANTE!!!\n"
              "Esse cpf não é valido e serve apenas para fins de teste de sistemas\n")
        self.get_uf()

    def get_uf(self):
        """ Recebe o digito de verificação """
        query = input("Digite a sigla da uf:\n")
        if not query:
            # seleciona um estado de forma randomica
            n = str(random.randint(0, 9))
            x = random.randint(0, len(self.ufs[n]))
            query = self.ufs[n][x]

        uf = self.check_uf(query)
        self.create_new_cpf(uf)

    def create_new_cpf(self, uf):
        """ Cria o cpf """
        try:
            base = self.create_sequence()  # sequencia base com 8 digitos aleatorios
            sequence = base + uf  # sequnecia base + o digito da uf

            first = self.validate_character(sequence, 9)  # retorna o primeiro digito verificador
            text = sequence + first  # sequencia + primeiro digito verificador
            second = self.validate_character(text, 10)  # retorna o segundo digito verificador

            self.show_result(uf, sequence, first, second)
        except TypeError:
            print("Valor invalido!\n")
            self.get_uf()

    def show_result(self, index, sequence, first, second):
        """ Mostra na tela os resultaods """

        cpf = f"{sequence[:3]}.{sequence[3:6]}.{sequence[6:9]}-{first}{second}"
        uf = self.ufs[index]

        print(f"\nCpf para teste é {cpf}")
        print(f"A região é {uf}")

    def check_uf(self, value):
        """ Verifica a unidade da uf na lista e retorna o digito correto """
        for index in self.ufs:
            for uf in self.ufs[index]:
                if uf == value.upper():
                    return index

    def create_sequence(self):
        """ Cria a sequencia base """
        value = ''
        for _ in range(8):
            number = self.get_random_number()
            value += number
        return str(value)

    @staticmethod
    def get_random_number():
        """ Retorna um numero randomico """
        value = str(random.randint(0, 9))
        return value

    @staticmethod
    def validate_character(value, index):
        """ Cria o digito de verificação """
        m = index + 1
        total = 0

        for item in value:
            total += int(item) * m
            m -= 1

        result = total % 11
        if result > 2:
            result = 11 - result
        else:
            result = 0

        return str(result)


generator = CpfGenerator()

if __name__ == '__main__':
    generator.welcome()
