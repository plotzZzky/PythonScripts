"""
 Script que automatiza a busca de informações sobre uma empresa no sistema do minha receita:

    - Se for fazer muitas consultas, para evitar instabilidade ou sobrecarga no servidor, instale o banco de dados
    na sua maquina e mude a url => https://docs.minhareceita.org/instalacao/

    - Sobre o minha receita => https://docs.minhareceita.org/

    Obrigado a equipe do minha receita!
"""
from pathlib import Path
import pandas as pd
import requests
import art


class FindInfo:
    """ Busca informações sobre um cnpj no site do minha receita ou no banco de dados local """
    companies: list = []
    data: list = []

    def welcome(self):
        art.tprint(f'{" " * 4} FindCompanyInfo', "cybersmall")
        print(f"{'_' * 30} https://github.com/plotzzzky {'_' * 30}\n")
        self.open_file()

    def open_file(self):
        """ Abre a lista com todas as empresas """
        try:
            path_file: Path = Path('FindCompanyInfo/companies.ods').absolute()
            df = pd.read_excel(path_file)
            dicts: list = df.to_dict(orient='records')
            self.companies: list = [{key: company[key] for key in company} for company in dicts]

            self.find_info()
        except FileNotFoundError:
            print("Lista de cnpjs para busca não encontrados!")

    def find_info(self):
        """ Busca informações para cada empresa na lista de empresas """
        for company in self.companies:
            self.get_data(company)
        self.save_file()

    def get_data(self, company: dict):
        """ Busca informações para cada una das empresas da lista """
        url: str = f"https://minhareceita.org/{company['CNPJ']}"  # http://0.0.0.0:8000 url local
        response = requests.get(url)
        json_res: dict = response.json()

        self.format_data(json_res)

    def format_data(self, data: dict):
        """ Cria um novo json resumido com as informações mais importantes da empresa """
        data_dict: dict = {
            "CNPJ": data['cnpj'],
            "Razao social": data['razao_social'],
            "nome fantasia": data['nome_fantasia'],
            "email": data['email'],
            "telefone": data['ddd_telefone_1'],
            "telefone_2": data['ddd_telefone_2'],
            "ativa": data['descricao_situacao_cadastral'],
            "mei": data['opcao_pelo_mei'],
            "simples": data['opcao_pelo_simples'],
            "endereco": f"{data['municipio']}, {data['bairro']}, {data['logradouro']}, {data['numero']}",
        }

        self.data.append(data_dict)

    def save_file(self):
        """ Salva uma nova planilha (info.ods) com as informações """
        new_df = pd.DataFrame(self.data)
        new_df.to_excel('info.ods', index=False)
        self.exit()

    @staticmethod
    def exit():
        print('Script completado e arquivo info.ods gerado!')


find = FindInfo()

if __name__ == '__main__':
    find.welcome()
