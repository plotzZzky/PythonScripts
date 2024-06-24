from datetime import datetime
import pyaudio
import wave
import art
import sys
import os


class PyRecorder:
    """ Script python para gravar audio via terminal """
    # consts do pyaudio
    CHANNELS: int = 2
    RATE: int = 44100
    CHUNK: int = 1024
    FILE_FORMAT = pyaudio.paInt16
    AUDIO = pyaudio.PyAudio()

    stream = None
    frames: list = []
    filename: str = ""

    def wellcome(self):
        os.system('clear')
        art.tprint(f'{" " * 2} PyRecorder', "tarty1")
        print(f"{'-' * 38} https://github.com/plotzzzky {'-' * 38}\n")
        self.menu()

    def menu(self):
        try:
            option: str = input("Iniciar uma gravação?(Y/N)\n").upper()
            if option == 'Y':
                self.record_audio()
            else:
                print(f"\nBye!")
                sys.exit()
        except KeyboardInterrupt:
            print(f"\nBye!")
            sys.exit()

    def record_audio(self):
        """ Incia a gravação do audio """
        self.stream = self.AUDIO.open(
                format=self.FILE_FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True
            )

        try:
            print("Recording...")
            while True:
                data = self.stream.read(self.CHUNK)
                self.frames.append(data)

        except KeyboardInterrupt:
            print("Finished recording.")
            self.stop_record()

    def stop_record(self):
        """ Encerra a gravação """
        self.stream.stop_stream()
        self.stream.close()
        self.AUDIO.terminate()

        self.save_file()

    def save_file(self):
        """ Salva o arquivo gravado com "o nome selecionado """
        self.filename = self.get_name()
        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.AUDIO.get_sample_size(self.FILE_FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))

    @staticmethod
    def get_name() -> str:
        """ Verifica se o usario quer renomear o audio ou cria um nome randomico """
        option: str = input(f'\nDigite um nome para o audio ou enter para ignorar:\n')
        if option:
            file_name: str = f"{option}.wav"
        else:
            now = datetime.now()
            now_str: str = str(now).replace('-', '_').replace(' ', '_').split('.')[0]
            file_name: str = f"{now_str}.wav"

        return file_name


pyrecord = PyRecorder()

if __name__ == "__main__":
    pyrecord.wellcome()
