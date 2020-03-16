# Iterator
class Rango():
    def __init__(self,low,high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current-1


for ele in Rango(5,9):
    print(ele)

# Integrated Functions

#Map applied a function to a data structure or tuple
print(list(map(abs,[-1,2,-3])))

# Zip Combina valores de dos estructuras de datos
print(list(zip('123','abc','ABC')))

# Generator
def firstn(n):
    num = 0
    while num < n:
        yield num # si esta en un for esto se llama cada iteracion del for
    num += 1

#sum_of_first_n = sum(firstn(1))

# Closures Funciones dentro de funciones
def principal():
    x = 7
    def anidada():
        print(x)
    return anidada

res = principal()
print(res())