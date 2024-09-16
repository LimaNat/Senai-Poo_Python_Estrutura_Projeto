from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.sexo import Sexo


class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
            f"\nLogradouro: {self.logradoura}"
            f"\nNúmero: {self.numero}"
        )