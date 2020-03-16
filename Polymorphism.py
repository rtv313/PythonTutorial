class Pajaro():
    def desplazar(self):
        print('volar')

class Serpiente():
    def desplazar(self):
        print('reptar')


def mover(animal):
    animal.desplazar()


pajaro = Pajaro()
serpiente = Serpiente()

mover(pajaro)
mover(serpiente)