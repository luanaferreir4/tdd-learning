import pytest

"""
    Funcoes do estilo xunit:

    - Setup de modulo:
    (modulo é um arquivo que estamos trabalhando.)
"""

def setup_module(module):
    print('\nIniciando o modulo', module.__name__)

def teardown_module(module):
    print('\nFinalizando o modulo', module.__name__)

"""
    setup: configuracao geral antes de usar os outros varios testes.
    teardown: desmonte (finalizacao).
"""

"""
    - Setup de funcoes:
    (Funcao do teste que deve ser executada aqui.)
                      |
                      V
"""

def setup_function(function):
    print('\nIniciando a funcao', function.__name__)

def teardown_function(function):
    print('\nFinalizando a funcao', function.__name__)

def test_testar_os_testes():
    print('\nEscopo da funcao "testar_os_testes"')
    assert True

def test_testar_os_testes2():
    print('\nEscopo da funcao "testar_os_testes2"')
    assert True
