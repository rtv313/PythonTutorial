
class Padre():
    def __init__(self):
        self.x = 8
        print("Constructor clase padre")

    def metodo(self):
        print('Metodo clase padre')


class Hija(Padre):

    def met_hija(self):
        print('Metodo clase hija')

hija = Hija()
hija.metodo()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

