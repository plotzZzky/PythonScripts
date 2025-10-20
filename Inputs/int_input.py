

def int_input(msg: str) -> int | None:
    """
        Input basico que retorna um integer

        Args:
            msg (str): Mensagem do input

        Return (int | None):
            Retorna um integer digitada ou um none em caso de erros

        Excepts:
            KeyboardInterrupt -> None
                Exibe uma mensagem fecha a aplicaçao

            TypeError -> None
                Exibe a mensagem de erro e reinica o cli
     """
    try:
        option: int = int(input(msg))

        return option

    except KeyboardInterrupt:
        print("Nenhum valor informado")
        exit()

    except TypeError:
        print("O valor precisa ser um integer")
        int_input(msg)
