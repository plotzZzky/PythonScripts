from pytube import YouTube, exceptions
from pathlib import Path
import sys
import art


class YouSave:
    """ Script para salvar videos do youtube"""
    video_name: str = ''
    streams = []
    home: Path = Path.home()
    filename: str = ''

    def welcome(self):
        art.tprint(f'{" " * 11} YouSave', "tarty1")
        print(f'{"_ " * 44}\n')
        self.get_data_from_url()

    def get_data_from_url(self):
        try:
            url: str = input("Digite o url do video:\n")
            self.streams = YouTube(url).streams
            print(self.streams)
            self.show_all_download_options()

        except exceptions.RegexMatchError:  # url invalida
            print('Url invalida!\n')
            self.get_data_from_url()

        except KeyboardInterrupt:
            print("Saindo...")

    def show_all_download_options(self):
        """ Lista todas as opções para download """
        print("\nOpções para download:")
        for index, item in enumerate(self.streams, 1):
            self.show_formated_download_option(index, item)

        self.check_selected_download_option()
        
    @staticmethod
    def show_formated_download_option(index, item):
        file_type: str = item.type
        file: str = item.mime_type
        res: str = f", resolution={item.resolution}" if item.resolution else ''
        value: str = f"{index}- tipo={file_type}, formato={file}{res}"
        print(value)

    def check_selected_download_option(self):
        try:
            option: str = input("\nSelecione a opção:\n").lower()
            formated_option: int = int(option) - 1
            stream = self.streams[formated_option]
            self.download_stream(stream)

        except (IndexError, ValueError):
            print("Opção invalida!\n")
            self.show_all_download_options()
        
    def download_stream(self, stream):
        folder: str = self.check_folder()
        stream.download(output_path=folder)  # faz o download do arquivo selecionado
        self.show_result_message()

    def check_folder(self) -> str:
        """ Verifica se a pasta existe """
        folder: str = f"{self.home}/yousave"

        if not Path(folder).exists():
            Path(folder).mkdir()
        return folder

    def show_result_message(self):
        print(f"Video {self.video_name} salva com sucesso!")
        self.exit_menu()

    def exit_menu(self):
        option: str = input("Baixar mais videos?(Y/N)\n").lower()
        if option == 'y':
            self.get_data_from_url()
        else:
            sys.exit()


yousave = YouSave()
if __name__ == '__main__':
    yousave.welcome()
