class Test():
    pass

class Ini():
    def __new__(cls):
        print('New')
        #return super(Test,cls).__new__(cls)
    def __init__(self):
        print('Init')

    def __del__(self):
        print('del')


life_cicle = Ini()