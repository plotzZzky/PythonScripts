from pathlib import Path
import pandas as pd
from datetime import datetime


PMS_AMOUNT: int = 67
PIMPF_AMOUNT: int = 77


class AssignCompanies:
    date = datetime.now()
    year = date.strftime("%Y")

    old_companies = None
    new_companies = None
    staff = {}


    def welcome(self):
        """ Menu inicial do appcli """
        wellcome_msg: str = f"{'_' * 20} AssignCompanies {'_' * 20}"
        print(wellcome_msg)
        print(
            "Esse script gera uma tabela com a lista das empresas deste ano com o nome do colaborador "
            "responsavel no ano anterior!\n"
        )

        self.run_script()

    def run_script(self):
        self.new_companies = self.open_companies_table("empresas_novas")
        self.old_companies = self.open_companies_table("empresas_antigas")
        self.select_old_companies_to_assign()

        self.select_new_companies_to_find()

    def open_companies_table(self, filename: str):
        """ Função generica para abrir as tabelas com as empresas """
        try:
            path = f"./Tabelas/{filename}.ods"
            file_path: Path = Path(path)

            if file_path.exists():
                print(f"Tabela {filename}.ods encontrada!\n")
                companies = self.convert_table_to_dict(file_path)
                return companies

            else:
                raise FileExistsError

        except FileExistsError:
            print(f"Lista {filename}.ods não encontrada!\n")

    @staticmethod
    def convert_table_to_dict(file_path):
        """ Cria uma lista de dicts com chave o nome do colaborador e valor a lista de empresas dele """
        data_frame = pd.read_excel(file_path)
        dicts: list = data_frame.to_dict(orient='records')

        return [{key: company[key] for key in company} for company in dicts]

    def select_old_companies_to_assign(self):
        """ Seleciona as empresasa da lista antiga para criar a lista de empresas de cada colaborador """
        print("Preenchendo a tabela nova com o nome dos colaboradores...\n")

        for company in self.old_companies:
            self.assign_companies_to_staff_member(company)

        print("Nova tabela preenchida!\n")

    def assign_companies_to_staff_member(self, company):
        """ Atribui cada empresa ao dict do respectivo colaborador """
        name = company['Responsável pela Abordagem'].split(' ')[0]

        if name not in self.staff:
            self.staff[name] = []

        self.staff[name].append(company)

    def select_new_companies_to_find(self):
        """ Seleciona cada empresa nova para verificar se estava na lista antiga """
        for company in self.new_companies:
            self.find_new_companies_in_old_list(company)

        self.save_new_companies_filled()

    def find_new_companies_in_old_list(self, new_company):
        """ Busca a empresa na lista antiga se encontrada salva o nome do responsavel antigo na lista nova """
        for old_company in self.old_companies:

            if old_company['CNPJ'] == new_company["CNPJ"]:
                new_company['Responsável pela Abordagem'] = old_company['Responsável pela Abordagem']

    def save_new_companies_filled(self):
        """ Salva a nova lista de empresa já preenchida """
        print("Salvando a lista de empresas preenchida...\n")

        df = pd.DataFrame(self.new_companies)
        path: str = f"./Tabelas/Lista_todas_empresas_{self.year}.ods"
        df.to_excel(path, index=False)

        print("Concluido!")


relatorio_app = AssignCompanies()

if __name__ == '__main__':
    relatorio_app.welcome()