
class Coche:
    def __init__(self,marca='Porsche',modelo='911'):
        self.marca = marca
        self.modelo = modelo

    def __repr__(self):
        return('{0}-{1}'.format(self.marca,self.modelo))


c  = Coche()
print(repr(c))