class Test:
    def __init__(self):
        self.x = 8
    # Un metodo statico no necesita ningun argumento de referencia
    # Un metodo statico no puede acceder a ningun atributo de clase
    @staticmethod
    def metodo_statico(valor):
        print("Valor:{0}".format(valor))
        # self.x = 8 variables de instancia no puede ser accedido

# Sin instancia
Test().metodo_statico(4)

# Con instancia
t = Test()
t.metodo_statico(8)
