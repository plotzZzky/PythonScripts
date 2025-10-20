

def bool_input(msg: str) -> bool | None:
    """
        Input basico que retorna um bool

        Args:
            msg (str): Mensagem do input

        Return (Bool):
            Retorna o valor booleano digitado pelo usuario

        Excepts:
            KeyboardInterrupt -> None
                Exibe uma mensagem fecha a aplicaçao

            TypeError -> None
                Exibe a mensagem de erro e reinica o cli

            ValueError -> Cli
                Exibe a mensagem de erro e reinica o cli
     """
    try:
        option: bool = bool(input(msg))

        return option

    except KeyboardInterrupt:
        print("Nenhum valor informado")
        exit()

    except TypeError:
        print("O valor precisa ser uma bool")
        bool_input(msg)
