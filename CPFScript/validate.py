import re
import art


class ValidateCpf:
    """
        Script que testa a logica numerica de validação de um cpf
        !!! Esse script não verifica se os dados são legitimos, mas se a logica matematica esta correta !!!
    """
    ufs: dict = {
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
        art.tprint(f'{" " * 2} ValidateCpf', "tarty1")
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.get_cpf()

    def get_cpf(self):
        query: str = input("Digite o cpf: (ex:'123.456.789-10' ou '98765432100') \n").lower()
        self.validate_cpf(query)

    def validate_cpf(self, cpf):
        """ Verifia se a logiga matematica e valida nesse cpf """
        value: str = re.sub(r'[.-]', '', cpf)
        if len(value) < 11:
            print("\nCpf precisa ter 11 digitos \n")
            self.get_cpf()

        if self.has_repeated_chars(value):
            print('\nFalso!!! \n CPFS não podem ter todos os digitos iguais \n')
        else:
            first: int = self.validate_character(value, 9)
            second: int = self.validate_character(value, 10)

            if first and second:
                region: str = self.ufs[value[8]]
                print(f"\nO CPF {cpf} é valido e pertence a região {region} \n")
                return True
            else:
                print("\n CPF Invalido!!!")

    @staticmethod
    def has_repeated_chars(value) -> bool:
        """ Verifica se todos os numeros são iguais e retorna invalido """
        query: str = value[:7]
        pattern: re = re.compile(r'^(\w)\1*$')
        match = pattern.match(query)
        return bool(match)

    @staticmethod
    def validate_character(value, index) -> bool:
        """ Calcula se a sequencia base bate com o verificador """
        validator: int = int(value[index])  # numero de verificação
        m: int = index + 1  # valor a ser multiplicado
        total: int = 0

        for item in value[:index]:  # multiplica os chars do cpf para gerar o total
            total += int(item) * m
            m -= 1

        result: int = total % 11  # gera o resto da divisão
        if result > 2:
            result = 11 - result
        else:
            result = 0

        return True if result == validator else False


validate = ValidateCpf()

if __name__ == '__main__':
    validate.welcome()
