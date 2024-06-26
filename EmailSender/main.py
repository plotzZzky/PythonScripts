from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import pandas as pd
import smtplib
import art


class EmailCreator:
    """ Ferramenta para criar e enviar email de forma automatizada para uma lista de clientes """
    email_titles: list = [
        {"name": "name",
         "title": "Titulo do email - {}\n"  # titulo do email a ser preenchido com o contato do cliente
         },
    ]

    df = None
    data: list = []
    unique_offices: list = None

    def welcome(self):
        art.tprint(f'{" " * 2}EmailSender', "tarty1")
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.open_file()

    def open_file(self):
        """ Abre a lista com os clientes"""
        try:
            path_file: Path = Path(__file__).resolve().parent
            self.df = pd.read_excel(f"{path_file}/companies.ods")
            self.data = self.df.to_dict(orient='records')
            self.check_if_office()
        except FileNotFoundError:
            print("Tabela de clientes não encontrado!!!")

    def check_if_office(self):
        """ Verifica se a empresa possui contabilidade e chama a função adequada para criar o email """
        companies: list = [item for item in self.data if pd.notna(item['Office'])]
        self.create_email_to_office(companies)

        no_office: list = [item for item in self.data if pd.isna(item['Office'])]
        self.create_mail_to_company(no_office)

    def create_email_to_office(self, companies):
        """ Cria o modelo de email para empresas com contabilidade """
        offices: set = set(item['Office'] for item in companies)

        for office in offices:
            costumers: list = [item for item in companies if item['Office'] == office]

            if len(costumers) > 1:
                costumer: dict = {"Model": "all"}
                costumer_list: list = []
                for item in costumers:
                    costumer_list += f"{item['Name']}, CNPJ: {item['CNPJ']}\n"
                path: Path = Path('EmailSender/models/office.md').absolute()
                email_office = open(path, 'r').read()
                email_body = email_office.format(company=costumer_list)

            else:
                costumer: dict = costumers[0]
                contact: str = f"{costumer['Name']}, CNPJ: {costumer['CNPJ']}"
                email: str = self.set_email_body(costumer)
                email_body: str = email.format(company=contact)

            title = self.set_company_title(costumer)
            self.show_email_model(title, office, email_body)

    def create_mail_to_company(self, companies):
        """ Cria o email para empresas sem contabilidade terceirizada """
        for company in companies:
            name: str = company['Name']
            cnpj: str = company['CNPJ']
            contact: str = f"{name}, CNPJ: {cnpj}"

            title = self.set_company_title(company)
            email: str = self.set_email_body(company)
            email_body: str = email.format(company=contact)
            self.show_email_model(title, contact, email_body)

    def set_company_title(self, company):
        """ Preenche o titulo do email com os dados do cliente """
        form: str = company['Model']
        for title in self.email_titles:
            if title['name'] == form:
                return title['title']

    def set_email_body(self, company):
        """ Determina qual email usar e retorna o modelo de email """
        form: str = company['Model']
        model_type: str = company['Type']
        if pd.isna(model_type):
            name: str = form
        else:
            name: str = f"{form}-{model_type}"
        return self.open_email_model(name)

    @staticmethod
    def open_email_model(name):
        """ Abre o modelo de email edequado para cada cliente """
        model_path: str = f"models/{name}.md"
        with open(model_path, 'r') as file:
            email_body = file.read()
        return email_body

    def show_email_model(self, title, office, email_body):
        """ Função para testar os emails antes de enviar """
        print(f"{'-' * 120}")
        print(title.FILE_FORMAT(office), email_body)
        print()
        self.save_email_model(title, office, email_body)

    @staticmethod
    def save_email_model(title, office, email_body):
        """ Salva um txt com o conteudo do email na pasta test """
        office_name: str = office.split(',')[0][:22]
        file_name: str = office_name.replace(' ', '_')
        file_name: str = file_name.lower()
        file_name: str = file_name.replace('_-_', '-')
        file_name: str = file_name.replace('/', '-')

        with open(f'test/{file_name}.txt', 'w') as file:
            file.write(title.FILE_FORMAT(office))
            file.write(email_body)
            file.close()


class EmailSender:
    """ Classe para enviar os emails """
    def __init__(self):
        self.smtp_host: str = 'smtp.office365.com'
        self.smtp_port: int = 587
        self.smtp_user: str = 'seu_email@outlook.com'
        self.smtp_pwd: str = 'sua_senha'
        self.token: str = ''
        self.server = None

    def config_server(self):
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as self.server:
            self.server.starttls()
            self.server.login(self.smtp_user, self.smtp_pwd)

    def config_email(self, contact_email, title, body):
        msg = MIMEMultipart()
        msg['From']: str = self.smtp_user
        msg['To']: str = contact_email
        msg['Subject']: str = title

        msg.attach(MIMEText(body, 'plain'))
        self.server.send_message(msg)


sender = EmailSender()
email_creator = EmailCreator()

if __name__ == '__main__':
    sender.config_server()
    email_creator.welcome()
