import sys
from pathlib import Path
import pandas as pd
import requests
import art

"""
Script que automatiza a busca de informações sobre uma empresa no sistema do minha receita:

    - Se for fazer muitas consultas, para evitar instabilidade ou sobrecarga no servidor, instale o banco de dados
    na sua maquina e mude a url => https://docs.minhareceita.org/instalacao/

    - Sobre o minha receita => https://docs.minhareceita.org/

    Obrigado a equipe do minha receita!
"""


class FindInfo:
    """ Busca informações sobre um cnpj no site do minha receita ou no banco de dados local """
    menu_options = [
        'Buscar um cnpj',
        'Buscar um lista de cnpjs em um .csv',
        'Sair'
    ]

    companies: list = []
    companies_jsons: list = []

    def welcome(self):
        art.tprint(f'{" " * 4} FindCompanyInfo', "cybersmall")
        print(f"{'_' * 30} https://github.com/plotzzzky {'_' * 30}\n")
        self.start_menu()

    def start_menu(self):
        print(f"{'__' * 20} Menu {'__' * 20}")
        for index, option in enumerate(self.menu_options, 1):
            print(f"{index}- {option}")

        option: str = input("Digite a opção: \n")
        self.check_start_menu_option(option)

    def check_start_menu_option(self, option: str):
        try:
            options = [
                self.get_cnpj,
                self.open_file,
                self.exit,
            ]
            options[int(option) - 1]()
        except (IndexError, TypeError, ValueError):
            print("Opção invalida!\n")
            self.start_menu()

    def get_cnpj(self):
        cnpj: str = input("Digite o cnpj sem pontos ou simbolos:\n")
        cnpj.replace('.', '')
        cnpj.replace('-', '')
        cnpj.replace('/', '')
        company = {'CNPJ': cnpj}

        self.get_data_from_company(company)

    def open_file(self):
        """ Abre a lista com todas as empresas """
        try:
            path_file: Path = Path('FindCompanyInfo/companies.ods').absolute()
            df = pd.read_excel(path_file)
            dicts: list = df.to_dict(orient='records')
            self.companies: list = [{key: company[key] for key in company} for company in dicts]

            self.select_companies()
        except FileNotFoundError:
            print("\nLista de cnpjs para busca não encontrados! \n")
            self.start_menu()

    def select_companies(self):
        """ Seleciona cada empresa na lista de empresas e busca informações sobre elas """
        for company in self.companies:
            self.get_data_from_company(company)
        self.save_result_file()

    def get_data_from_company(self, company: dict):
        """ Busca informações da empresa selecionada """
        url: str = f"https://minhareceita.org/{company['CNPJ']}"  # http://0.0.0.0:8000 url local
        response = requests.get(url)

        if response.status_code == 200:
            json_res: dict = response.json()
            self.format_response_data(json_res)
        else:
            print("\nCNPJ não cadastrado na receita federal!")

    def format_response_data(self, cnpj_data: dict):
        """ Cria um novo json resumido com as informações mais importantes da empresa """
        endereco = f"{cnpj_data['municipio']}, {cnpj_data['bairro']}, {cnpj_data['logradouro']}, {cnpj_data['numero']}"

        data_dict: dict = {
            "CNPJ": cnpj_data['cnpj'],
            "Razao social": cnpj_data['razao_social'],
            "nome fantasia": cnpj_data['nome_fantasia'],
            "email": cnpj_data['email'],
            "telefone": cnpj_data['ddd_telefone_1'],
            "telefone_2": cnpj_data['ddd_telefone_2'],
            "ativa": cnpj_data['descricao_situacao_cadastral'],
            "mei": cnpj_data['opcao_pelo_mei'],
            "simples": cnpj_data['opcao_pelo_simples'],
            "endereco": endereco,
        }

        self.companies_jsons.append(data_dict)

    def save_result_file(self):
        """ Salva uma nova planilha (info.ods) com as informações """
        new_df = pd.DataFrame(self.companies_jsons)
        new_df.to_excel('info.ods', index=False)
        print('Script completado e arquivo info.ods gerado!')

    @staticmethod
    def exit():
        print("Saindo...")

        if __name__ == '__main__':
            sys.exit()


find = FindInfo()

if __name__ == '__main__':
    find.welcome()
