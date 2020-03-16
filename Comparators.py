
class Coche:
    def __init__(self,marca='Porsche',modelo='911'):
        self.marca = marca
        self.modelo = modelo

    def __gt__(self,objeto):
        if int(self.modelo) > int(objeto.modelo):
            return True
        return False

modelo911 = Coche('Porcsche','911')
modelo910 = Coche('Porsche','910')

if modelo911 > modelo910:
    print('Modelo {0} es mayor a {1}'.format(modelo911.modelo,modelo910.modelo))

# Otros comparadores
'''
__lt__() Menor que
__le__() Menor o igual que
__gt__() Mayor que
__ge__() Mayor igual que
__eq__() Igual a 
__ne__() Distinto de
'''