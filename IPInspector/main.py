from rich import print
import sys
import socket
import requests


class IPInspector:
    # Script para buscar informações sobre um ip via terminal
    ip: str = ""
    domain: str = ""
    ip_json: dict = {"ip": "1111", "city": "city"}

    print_space: str = f'{"--" * 13}'  # Usado nos titulos

    def welcome(self):
        # Apresentação do script
        print(f"{self.print_space} [bold blue] Bem vindo ao IPInspector [/bold blue] {self.print_space}")
        print(f"{' ' * 10} Esse script busca informações de servidores por ip ou dominio.")
        print(f" {'-' * 79} ")
        self.menu()

    def menu(self):
        # Menu para verificar a função desejada pelo usario e a executa
        print(
            "1- Buscar por Ip \n"
            "2- Buscar por Dominio \n"
            "3- Sair"
        )
        try:
            option: str = input("Selecione uma opção: \n").lower()
            self.check_menu_option(option)
        except KeyboardInterrupt:
            print("Saindo...")

    def check_menu_option(self, option: str):
        if option == "1":
            self.get_ip()
        elif option == "2":
            self.get_domain()
        elif option == "3":
            print("Saindo...")
            if __name__ == '__main__':  # Se não for o main retorna ao menu inicial dos scripts
                sys.exit()
        else:
            print("Valor incorreto!\n")
            self.menu()

    def get_ip(self):
        # Função que recebe o ip atraves de um input
        self.ip: str = input("\nDigite o ip:\n").lower()
        self.get_info_by_ip()

    def get_info_by_ip(self):
        # Busca as infos do ip na api e chama a função para mostrar os resultados
        url: str = f"https://ipapi.co/{self.ip}/json/"
        response = requests.get(url)
        self.ip_json: dict = response.json()
        self.show_result()

    def get_domain(self):
        # Recebe um dominio via input, obtem o ip desse dominio e chama a função para obter informções do ip
        self.domain: str = input("\nDigite o dominio:\n")
        self.ip = socket.gethostbyname(self.domain)
        self.get_info_by_ip()

    def show_result(self):
        # Mostra os resultados ja formatados
        print(f"{self.print_space} Result {self.print_space}\n")
        print(f"Ip: {self.ip_json['ip']}")
        print(f"Country: {self.ip_json['country']}")
        print(f"City: {self.ip_json['city']}\n")
        self.close_menu()

    def close_menu(self):
        # Função para fechar o programa
        # Se o usuario executou o menu da raiz volta para esse menu, do contrario, fecha o programa e o terminal
        option: str = input("Deseja fazer nova busca?(Y/N) \n").upper()
        if option == "Y":
            self.show_result()
        else:
            if __name__ == "__main__":
                print("Saindo...")
                sys.exit()


ip = IPInspector()
if __name__ == "__main__":
    ip.welcome()
