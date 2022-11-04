
class Cliente:

    """ O @property funciona como um metodo que dá acesso aos atributos.
    Indica que se trata de uma propriedade, que não precisamos colocar o 
    método entre parenteses, podendo executar o @property nome assim: "cliente.nome"
    """

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome.title() # para que a primeira letra seja maiúscula
    
    @nome.setter
    def nome (self, nome):
        self.__nome = nome
    
    """ Na execução fazemos dessa forma:
    cliente.nome = "Victor"
    """