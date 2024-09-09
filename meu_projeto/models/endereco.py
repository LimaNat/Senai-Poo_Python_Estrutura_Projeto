class Endereco:
    def __init__(self, logradoura: str, numero: int) -> None:
        self.logradoura = logradoura
        self.numero = numero

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradoura}"
            f"\nNúmero: {self.numero}"
        )
    