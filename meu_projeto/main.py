import os

from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.pessoa import Pessoa

os.system("cls || clear")

#Instanciando classe.
pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO,
                  Endereco("Rua A.", 35))

print(pessoa_1)