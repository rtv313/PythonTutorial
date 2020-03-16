class Intro():
    def __init__(self,val):
        self.x = val

    def primer(self):
        print('Primero')

    def segundo(self):
        print('Segundo')

i = Intro('Valor')

print(dir(i)) # Despliega todos los atributes y metodos de la clase

isinstance(i,Intro) # Si una variable es una instancia de una clase

if hasattr(i,'x'): print('i puede acceder a x') # Checa si un objeto tiene cierto atributo

type(i) # Tipo de objeto que es

cad = "Cadena"

callable(cad) #Nos dice si un objeto se puede llamar las variables no se pueden llamar , las fuciones si , True or False

i.__setattr__('x',1) # asignar atributo
i.__getattribute__('x') # obtener atributo