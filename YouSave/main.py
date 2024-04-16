from pytube import YouTube, exceptions
from pathlib import Path
import sys
import art


class YouSave:
    """ Script para salvar videos do youtube"""
    video_name = ''
    streams = []
    home = Path.home()
    filename = ''

    def wellcome(self):
        art.tprint(f'{" " * 11} YouSave', "tarty1")
        print(f'{"_ " * 44}\n')
        self.get_content()

    def get_content(self):
        try:
            url = input("Digite o url do video:\n")
            self.streams = YouTube(url).streams
            self.show_options_for_download()
        except exceptions.RegexMatchError:  # url invalida
            print('Url invalida!\n')
            self.get_content()
        except KeyboardInterrupt:
            print("Saindo...")

    def show_options_for_download(self):
        """ Lista todas as opções para download """
        print("\nOpções para download:")
        n = 1

        for option in self.streams:
            type = option.type
            file = option.mime_type
            res = f", resolution={option.resolution}" if option.resolution else ''
            value = f"{n}- tipo={type}, formato={file}{res}"
            print(value)
            n += 1

        self.select_option_for_download()

    def select_option_for_download(self):
        option = input("\nSelecione a opção:\n")
        folder = self.check_folder()
        self.streams[int(option) - 1].download(output_path=folder)  # faz o download do arquivo selecionado
        self.show_result()

    def check_folder(self):
        """ Verifica se a pasta existe """
        folder = f"{self.home}/yousave"

        if not Path(folder).exists():
            Path(folder).mkdir()

        return folder

    def show_result(self):
        print(f"Video {self.video_name} salva com sucesso!")
        self.exit_menu()

    def exit_menu(self):
        option = input("Baixar mais videos?(Y/N)\n").lower()
        if option == 'y':
            self.get_content()
        else:
            sys.exit()


you_save = YouSave()

if __name__ == '__main__':
    you_save.wellcome()
