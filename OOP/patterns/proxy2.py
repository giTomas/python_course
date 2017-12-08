class Implementation:
    def f(self):
        print("Implementattion.f()")
    def g(self):
        print("Implementattion.g()")
    def h(self):
        print("Implementattion.h()")

class Proxy:
    def __init__(self):
        self.__implementation = Implementation()
    def __getattr__(self, name):
        return getattr(self.__implementation, name)

p = Proxy()
p.f()
p.g()
p.h()
