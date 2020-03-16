from math import pi

class Circle:
    def __init__(self,radio):
        self.radio = radio  # variable de instancia

    #Variable que se calcula , # No admite mas parametros como un metodo normal
    @property
    def area(self):
            return  pi * (self.radio ** 2)

    #Otra forma de crear una property es declarar un metodo y llamar a property
    def double_area(self):
        return (pi * (self.radio ** 2)) * 2
    double_area = property(double_area)

c = Circle(25)
print(c.area)
print(c.double_area)

# Setter Example
class Circle_Two:
    # Se crea la propiedad
    @property
    def radio(self):
        return self.__radio
    # Se crea su asignador
    @radio.setter
    def radio(self,radio):
        self.__radio = radio

circulo = Circle_Two()
circulo.radio = 23
print(circulo.radio)

