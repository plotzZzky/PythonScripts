import re
import art


class ValidateCpf:
    """
        Script que testa a logica numerica de validação de um cpf
        !!! Esse script não verifica se os dados são legitimos, mas se a logica matematica esta correta !!!
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
        art.tprint(f'{" " * 2 } ValidateCpf', "tarty1")
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.get_cpf()

    def get_cpf(self):
        query = input("Digite o cpf: (ex:'123.456.789-10' ou '98765432100') \n")
        self.validate_cpf(query)

    def validate_cpf(self, cpf):
        """ Verifia se a logiga matematica e valida nesse cpf """
        value = re.sub(r'[.-]', '', cpf)
        if len(value) < 11:
            print("Cpf precisa ter 11 digitos")
            self.get_cpf()

        if self.has_repeated_chars(value):
            print('Falso!!!\nCPFS não podem ter todos os digitos iguais')
        else:
            first = self.validate_character(value, 9)
            second = self.validate_character(value, 10)

            if first and second:
                region = self.ufs[value[8]]
                print(f"O CPF {cpf} é valido e pertence a região {region}")
                return True
            else:
                print("CPF Invalido!!!")

    @staticmethod
    def has_repeated_chars(value):
        """ Verifica se todos os numeros são iguais e retorna invalido """
        query = value[:7]
        pattern = re.compile(r'^(\w)\1*$')
        match = pattern.match(query)
        return bool(match)

    @staticmethod
    def validate_character(value, index):
        """ Calcula se a sequencia base bate com o verificador """
        validator = int(value[index])  # numero de verificação
        m = index + 1  # valor a ser multiplicado
        total = 0

        for item in value[:index]:  # multiplica os chars do cpf para gerar o total
            total += int(item) * m
            m -= 1

        result = total % 11  # gera o resto da divisão
        if result > 2:
            result = 11 - result
        else:
            result = 0

        return True if result == validator else False


validate = ValidateCpf()

if __name__ == '__main__':
    validate.welcome()
