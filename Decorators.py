# Class as decorator
class Decorador(object):
    def __init__(self,f):
        self.f = f
    def __call__(self):
        print('inicio',self.f.__name__)
        self.f()
        print('fin',self.f.__name__)

@Decorador
def funcion():
    print('soy funcion')
funcion()

print("###################################################")
# Function as decorator
def principal(f):
    def nueva():
        print('ini',f.__name__)
        f()
        print('fin',f.__name__)
    return nueva
@principal
def decorada():
    print('decorada')
decorada()

print("###################################################")
class Decorador2(object):
    def __init__(self,f):
        self.f = f

    def __call__(self, *argumentos):
        print('inicio',self.f.__name__)
        self.f(*argumentos)
        print('fin',self.f.__name__)


@Decorador2
def funcion(p1,p2,p3):
    print('soy funcion con argumentos',p1,p2,p3)

funcion('uno','dos','tres')

# Decorador con parametros
def decorator_args(arg1,arg2,arg3):
    def wrap(f):
        print('ini wrap()')
        def wrapped_f(*args):
            print('ini wrapped_f')
            print('decorator args:',arg1,arg2,arg3)
            f(*args)
            print('fin wrapped_f')
        return wrapped_f
    return wrap

@decorator_args(1,2,3)
def fun(a,b):
    print('fun args',a,b)
print('#################')
fun('p1','p2')