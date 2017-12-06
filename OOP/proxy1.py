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
    def f(self): self.__implementation.f()
    def g(self): self.__implementation.g()
    def h(self): self.__implementation.h()

p = Proxy()
p.f()
p.g()
p.h()
