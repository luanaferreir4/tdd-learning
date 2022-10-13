"""
    setup e teardown de classe:
"""

class TestTestes:
    @classmethod
    def setup_class(classe):
        print('\nSetup da classe', classe.__name__)
    
    @classmethod
    def teardown_class(classe):
        print('\nTeardown da classe', classe.__name__)

    def setup_method(self,method):
        print('\nSetup do metodo', method.__name__)
    
    def teardown_method(self,method):
        print('\nTeardown do metodo', method.__name__)

    def test_test_1(self):  # metodos de classe tem que colocar self.
        print('\nEscopo da funcao "test_1"')
        assert True

    def test_test_2(self):
        print('\nEscopo da funcao "test_2"')
        assert True