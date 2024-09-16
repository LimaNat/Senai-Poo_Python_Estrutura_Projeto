import pytest
from meu_projeto.models.pessoa import Pessoa  # Caminho relativo
from meu_projeto.models.endereco import Endereco # Caminho absoluto
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.enums.uf import UnidadeFederativa

# Modelo.
@pytest.fixture
def Criar_pessoa():
    pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO,
                    Endereco("Rua A", 35, UnidadeFederativa.BAHIA))
    return pessoa_1

def test_pessoa_atribuido_nome(Criar_pessoa):
    assert Criar_pessoa.nome == "Marta"

def test_pessoa_atribuido_idade(Criar_pessoa):
    assert Criar_pessoa.idade == 22
