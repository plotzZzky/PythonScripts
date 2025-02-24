import tkinter as tk
from main import pycli


class ScriptInterface:
    """ Interface grafica para faciliar o uso do script """
    root = None
    title = "BoilerPlate interface"

    def create_window(self):
        # Criação da janela do app
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry("640x200")

        self.create_instructions_label()
        self.create_buttons()

        # Inicia o loop da interface gráfica
        self.root.mainloop()

    def create_instructions_label(self):
        """ Cria o label com as instruções do app """
        label_text: str = (
            "Apresentação do app\n"
        )

        label = tk.Label(self.root, text=label_text, font=("Arial", 14, "bold"))
        label.pack(pady=20)

    def create_buttons(self):
        """Cria o botão que executa o script de geração das tabelas """
        frame = tk.Frame()
        frame.pack(pady=5)

        button = tk.Button(frame, text="First function", command=pycli.first_function, font=("Arial", 12))
        button.pack(padx=10, side="left")

        button = tk.Button(frame, text="Second function", command=pycli.second_function, font=("Arial", 12))
        button.pack(padx=10, side="left")

        button = tk.Button(frame, text="Close app", command=self.close_app, font=("Arial", 12))
        button.pack(padx=10, side="right")

    def close_app(self):
        self.root.destroy()


app = ScriptInterface()
app.create_window()
