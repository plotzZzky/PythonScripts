

def str_input(msg: str, empty: bool) -> str | None:
    """
        Input basico que retorna uma string

        Args:
            msg (str): Mensagem do input
            empty (bool): Aceita campo vazio

        Return (str | None):
            Retorna a string digitada ou um none em caso de erros

        Excepts:
            KeyboardInterrupt -> None
                Exibe uma mensagem fecha a aplicaçao

            TypeError -> None
                Exibe a mensagem de erro e reinica o cli

            ValueError -> Cli
                Exibe a mensagem de erro e reinica o cli
     """
    try:
        option: str = str(input(msg))

        if empty: # permite valor vazio?
            if data_is_empty(option):
                return option

            else:
                raise ValueError

        return option

    except KeyboardInterrupt:
        print("Nenhum valor informado")
        exit()

    except TypeError:
        print("O valor precisa ser uma string")
        str_input(msg, empty)

    except ValueError:
        print("O valor nao pode ser vazio!")
        str_input(msg, empty)


def data_is_empty(data: str):
    return True if data == "" or data == " " else False
