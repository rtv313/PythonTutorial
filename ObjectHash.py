
class TestHash():
    pass

t = TestHash()
print(t.__hash__())

x = t
print(x.__hash__())

if x.__hash__() ==  t.__hash__():
    print('Son iguales')

x = TestHash()
print(x.__hash__())