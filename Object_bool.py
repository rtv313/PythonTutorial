
class TestBool():
    def __bool__(self):
        return True


t = TestBool()
print(t.__bool__())