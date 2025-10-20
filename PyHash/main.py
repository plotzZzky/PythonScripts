from datetime import datetime, timezone
import hashlib
import re


class PyHash:
    def __init__(self):
        super().__init__()
        print(f"{'_' * 40} PyHash {'_' * 40}")

    def create_hash_file_md5sum(self, filename: str):
        self.generic_create_hash_file(hashlib.md5(), filename)

    def create_hash_file_sha1sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha1(), filename)

    def create_hash_file_sha256sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha256(), filename)

    def create_hash_file_sha512sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha512(), filename)

    def create_hash_file_sha3_256sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha3_256(), filename)

    def return_hash_md5sum(self, filename: str):
        self.generic_return_hash(hashlib.md5(), filename)

    def return_hash_sha1sum(self, filename: str):
        self.generic_return_hash(hashlib.sha1(), filename)

    def return_hash_sha256sum(self, filename: str):
        self.generic_return_hash(hashlib.sha256(), filename)

    def return_hash_sha512sum(self, filename: str):
        self.generic_return_hash(hashlib.sha512(), filename)

    def return_hash_sha3_256sum(self, filename: str):
        self.generic_return_hash(hashlib.sha3_256(), filename)

    # ______________________ Basic functions _________________________

    def generic_create_hash_file(self, algorithm, filename: str):
        clean_name: str = self.return_clean_name(filename)
        timestamp = self.create_timestamp()
        result_hash = self.generic_return_hash(algorithm, filename)
        hash_file_name: str = f"{algorithm.name}_{clean_name}_{timestamp}.txt"
        self.create_hash_file(hash_file_name, filename, timestamp, result_hash)

    @staticmethod
    def return_clean_name(raw_name: str) -> str:
        """ Retorna o nome sem extensão e chars especiais """
        no_ext: str = raw_name.split(".")[0]
        clean_name: str = re.sub(r'[^A-Za-z0-9]', '_', no_ext)
        return clean_name

    @staticmethod
    def create_timestamp() -> str:
        """ Cria e retorna o timestamp """
        now: datetime = datetime.now(timezone.utc)
        timestamp: str = now.strftime("%Y%m%dT%H%M%S.%f") + "Z"
        return timestamp

    def generic_return_hash(self, algorithm, filename: str) -> bytes:
        """ Retorna a hash criada """
        resul_hash: bytes = self.create_hash(algorithm, filename)
        print(
            f"filename={filename}\n"
            f"{algorithm.name}_hash={resul_hash}\n"
        )
        return resul_hash


    @staticmethod
    def create_hash(algorithm, filename: str) -> bytes:
        """
            Cria a hash do arquivo

            Args:
                algorithm (func) - Algoritimo usado para criar a hash (md5, sha1, sha256...)
                filename (str) - Nome do arquivo para se gerar a hash

            Return:
                Retorna a hash gerada fo arquivo (filename)
        """
        with open(filename, "rb") as file:
            data: bytes = file.read()
            algorithm.update(data)

        return algorithm.hexdigest()

    @staticmethod
    def create_hash_file(hash_file_name: str, filename: str, timestamp: str, result_hash: bytes):
        """
            Cria o txt com os dados do arquivo

            Args:
                hash_file_name (str) - Nome do arquivo com a hash
                filename (str) - Nome do arquivo que foi heshado
                timestamp (str) - Momento que foi feito a hash
                result_hash (bytes) - Hash do arquivo
        """
        with open(hash_file_name, "w") as hash_file:
            hash_file.write(
                f"filename={filename}\n"
                f"timestamp={timestamp}\n"
                f"hash={result_hash}"
            )

py_hash = PyHash()

if __name__ == "__main__":
    py_hash.create_hash_file_md5sum("file.txt")
