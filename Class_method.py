class Test:
    y = 1
    def __init__(self):
        self.x = 8

    @classmethod
    def metodo_clase(cls,param1): # se declara agregando cls y decorator @classmethod
        print("Parametro:{0}".format(param1))
        cls.y = 3 # Podemos acceder variables de clase,
        # self.x = 3  pero de instancia no, Crashea

Test.metodo_clase(6) # Podemos llamarlo sin necesidad de instanciar una clase

# Podemos llamarlo creando una instancia tambien
t = Test()
t.metodo_clase(5)