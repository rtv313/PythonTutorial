# Todos los metodos son publicos pero usamos _ para indicar que son privados

class Test():
    def _privado(self):
        print("Método Privado")

t = Test()
t._privado()


class Privado():
    def __init__(self):
        self.__atributo_privado = 1
        self.no_privado = 2

p = Privado()
print(p.no_privado)
# p.__atributo_privado = 1 # Crashea
print(p._Privado__atributo_privado) # Mangling es una tecnica que me permite acceder a atributos "privados"