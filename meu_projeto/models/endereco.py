from meu_projeto.models.enums import uf


class Endereco:
    def __init__(self, logradoura: str, numero: int, uf: uf) -> None:
        self.logradoura = logradoura
        self.numero = numero
        self.uf = uf

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradoura}"
            f"\nNúmero: {self.numero}"
            f"\nUF: {self.uf}"
        )
    