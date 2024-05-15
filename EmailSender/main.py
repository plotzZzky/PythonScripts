from pathlib import Path
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import art


class EmailCreator:
    """ Ferramenta para criar e enviar email de forma automatizada para uma lista de clientes """
    email_titles = [
        {"name": "name",
         "title": "Titulo do email - {}\n"  # titulo do email a ser preenchido com o contato do cliente
         },
    ]

    def __init__(self):
        self.df = None
        self.data = []
        self.unique_offices = None

    def wellcome(self):
        art.tprint(f'{" " * 2 }EmailSender', "tarty1")
        print(f"{'-' * 30} https://github.com/plotzzzky {'-' * 30}\n")
        self.open_file()

    def open_file(self):
        """ Abre a lista com os clientes"""
        path_file = Path(__file__).resolve().parent
        self.df = pd.read_excel(f"{path_file}/companies.ods")
        self.data = self.df.to_dict(orient='records')
        print(self.data)
        #self.check_if_office()

    def check_if_office(self):
        """ Verifica se a empresa possui contabilidade e chama a função adequada para criar o email """
        companies = [item for item in self.data if pd.notna(item['Office'])]
        self.create_email_to_office(companies)

        no_office = [item for item in self.data if pd.isna(item['Office'])]
        self.create_mail_to_company(no_office)

    def create_email_to_office(self, companies):
        """ Cria o modelo de email para empresas com contabilidade """
        offices = set(item['Office'] for item in companies)

        for office in offices:
            costumers = [item for item in companies if item['Office'] == office]

            if len(costumers) > 1:
                costumer = {"Model": "all"}
                costumer_list = ""
                for item in costumers:
                    costumer_list += f"{item['Name']}, CNPJ: {item['CNPJ']}\n"
                path = Path('EmailSender/models/office.md').absolute()
                email_office = open(path, 'r').read()
                email_body = email_office.format(company=costumer_list)

            else:
                costumer = costumers[0]
                contact = f"{costumer['Name']}, CNPJ: {costumer['CNPJ']}"
                email = self.set_email_body(costumer)
                email_body = email.format(company=contact)

            title = self.set_company_title(costumer)
            self.show_email_model(title, office, email_body)

    def create_mail_to_company(self, companies):
        """ Cria o email para empresas sem contabilidade terceirizada """
        for company in companies:
            name = company['Name']
            cnpj = company['CNPJ']
            contact = f"{name}, CNPJ: {cnpj}"

            title = self.set_company_title(company)
            email = self.set_email_body(company)
            email_body = email.format(company=contact)
            self.show_email_model(title, contact, email_body)

    def set_company_title(self, company):
        """ Preenche o titulo do email com os dados do cliente """
        form = company['Model']
        for title in self.email_titles:
            if title['name'] == form:
                return title['title']

    def set_email_body(self, company):
        """ Determina qual email usar e retorna o modelo de email """
        form = company['Model']
        model_type = company['Type']
        if pd.isna(model_type):
            name = form
        else:
            name = f"{form}-{model_type}"
        return self.open_email_model(name)

    @staticmethod
    def open_email_model(name):
        """ Abre o modelo de email edequado para cada cliente """
        model_path = f"models/{name}.md"
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
        x = office.split(',')[0][:22]
        file_name = x.replace(' ', '_').lower().replace('_-_', '-').replace('/', '-')

        with open(f'test/{file_name}.txt', 'w') as file:
            file.write(title.FILE_FORMAT(office))
            file.write(email_body)
            file.close()


class EmailSender:
    """ Classe para enviar os emails """
    def __init__(self):
        self.smtp_host = 'smtp.office365.com'
        self.smtp_port = 587
        self.smtp_user = 'seu_email@outlook.com'
        self.smtp_pwd = 'sua_senha'
        self.token = ''
        self.server = None

    def config_server(self):
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as self.server:
            self.server.starttls()
            self.server.login(self.smtp_user, self.smtp_pwd)

    def config_email(self, contact_email, title, body):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = contact_email
        msg['Subject'] = title

        msg.attach(MIMEText(body, 'plain'))
        self.server.send_message(msg)


sender = EmailSender()
email_creator = EmailCreator()

if __name__ == '__main__':
    # sender.config_server()
    email_creator.wellcome()
