from rich import print
import sys
import socket
import requests


# Script para buscar informações sobre um ip via terminal
class IPInspector:
    def __init__(self):
        # ip variables
        self.ip = ""
        self.domain = ""
        self.ip_json = {"ip": "1111", "city": "city"}

        self.print_space = f'{"--" * 20}'  # Usado nos titulos

    # Apresentação do script
    def wellcome(self):
        print(
            f" {self.print_space} [bold blue] Bem vindo ao IPInspector [/bold blue] {self.print_space} "
        )
        print(
            f" {' ' * 20} Esse script busca informações de servidores por ip ou dominio."
        )
        print(f" {'-' * 108} ")
        self.menu()

    # Menu para verificar a função desejada pelo usario e a executa
    def menu(self):
        print("Selecione uma opção:\n")
        print("1- Buscar por Ip \n" "2- Buscar por Dominio")
        response = input()
        if response == "1":
            self.get_ip()
        elif response == "2":
            self.get_domain()
        else:
            print("Valor incorreto!\n")
            self.menu()

    # Função que recebe o ip atraves de um input
    def get_ip(self):
        self.ip = input("\nDigite o ip:\n")
        self.get_info_by_ip()

    # Busca as infos do ip na api e chama a função para mostrar os resultados
    def get_info_by_ip(self):
        url = f"https://ipapi.co/{self.ip}/json/"
        response = requests.get(url)
        self.ip_json = response.json()
        self.show_result()

    # Recebe um dominio via input, obtem o ip desse dominio e chama a função para obter informções do ip
    def get_domain(self):
        self.domain = input("\nDigite o dominio:\n")
        self.ip = socket.gethostbyname(self.domain)
        self.get_info_by_ip()

    # Mostra os resultados ja formatados
    def show_result(self):
        print(f"{self.print_space} Result {self.print_space}\n")
        print(f"Ip: {self.ip_json['ip']}")
        print(f"Country: {self.ip_json['country']}")
        print(f"City: {self.ip_json['city']}\n")
        self.close_menu()

    # Função para fechar o programa
    # Se o usuario executou o menu da raiz volta para esse menu, do contrario, fecha o programa e o terminal
    def close_menu(self):
        response = input("Deseja fazer nova busca?(Y/N) \n").upper()
        if response == "Y":
            self.show_result()
        else:
            if __name__ == "__main__":
                sys.exit()


ip = IPInspector()

if __name__ == "__main__":
    ip.wellcome()
