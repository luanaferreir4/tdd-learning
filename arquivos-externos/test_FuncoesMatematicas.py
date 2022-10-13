"""
    - Criar classe funcoes_matematicas.
    - Criar funcao somar_dois_numeros, sendo esses dois numeros passados como parametro.
"""
from FuncoesMatematicas import FuncoesMatematicas

def test_somar_um_mais_dois_no_metodo_somar_dois_numeros_e_retornar_tres():
    funcoes = FuncoesMatematicas()
    assert funcoes.somar_dois_numeros(1, 2) == 3

    # https://docs.pytest.org/en/7.1.x/ = documentacao pytest.