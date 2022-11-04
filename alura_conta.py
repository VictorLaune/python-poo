class Conta:
    
    ''' 
    Encapsulamento em python utiliza: __
    Indica que o atributo foi criado para ser usado dentro da classe
    através dos métodos.

    Uma classe deve ter uma única função, isso é manter a coesão da classe.

    Getters e Setters
    Se quiser fazer algo com o seu atributo, utilizamos métodos.
    Para apenas coletar os atributos, utilizamos o getters.
    Para atribuir valores, definimos com os setters.
    Mas devemos criar apenas quando houver necessidade!


    '''
    
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    """ Quando temos métodos da classe, devemos utilizar o @staticmethod
    São estáticos por que são da classe, não do objeto.
    """
    @staticmethod
    def codigo_banco(self):
        return "001"

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    


    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    """ O metodo __pode_sacar é um método privado
    só pode ser chamado dentro do metodo sacar()
    Assim como existem atributos privados, também 
    existem os metodos privados
    """

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else: 
            print(f'O valor {valor} passou o limite.')
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)