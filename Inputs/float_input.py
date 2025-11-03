
def int_input(msg: str) -> float | None:
    """
        Input basico que retorna um float

        Args:
            msg (str): Mensagem do input

        Return (float | None):
            Retorna um integer digitada ou um none em caso de erros

        Excepts:
            KeyboardInterrupt -> None
                Exibe uma mensagem fecha a aplicaçao

            TypeError -> None
                Exibe a mensagem de erro e reinica o cli
     """
    try:
        option: float = float(input(msg))

        return option

    except KeyboardInterrupt:
        print("Nenhum valor informado")
        exit()

    except TypeError:
        print("O valor precisa ser um integer")
        int_input(msg)
