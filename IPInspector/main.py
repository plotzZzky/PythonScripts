import sys
import socket
import requests


# Programa para buscar informações sobre um ip via terminal
class IPInspector:
    def __init__(self):
        # ip variables
        self.ip = ''
        self.domain = ''
        self.ip_json = {'ip': '1111', 'city': 'city'}
        # format variables
        self.print_space = f'{"-_" * 20}'

    # Aprsentação do programa
    def wellcome(self):
        print(f"{self.print_space} Bem vindo ao IPInspector {self.print_space}\n")
        print(f"Essa ferramente te ajudara a encomtrar informaçõe de servidores por ip ou dominio.\n")
        self.menu()

    # Menu para verificar a função desejada pelo usario e a executa
    def menu(self):
        print("Selecione uma opção:\n")
        print("1- Buscar por Ip \n"
              "2- Buscar por Dominio")
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

    # Busca as infos do api na api e chama a função para mostrar os resultados
    def get_info_by_ip(self):
        url = f"https://ipapi.co/{self.ip}/json/"
        response = requests.get(url)
        self.ip_json = response.json()
        self.show_result()

    # Recebe um dominio via input, obtem o ip desse dominio e chama a função para obter informções do ip
    def get_domain(self):
        self.ip = input("\nDigite o dominio:\n")
        self.ip = socket.gethostbyname("www.diolinux.com")
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
            if __name__ == '__main__':
                sys.exit()


ip = IPInspector()

if __name__ == '__main__':
    ip.wellcome()
