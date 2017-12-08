class ActiveDestructor:
    def __init__(self, name):
        self.__name = name

    def printName(self):
        print(self.__name)

    def __del__(self):
        print('Destructor started for {}'.format(self.__name))


if __name__ == '__main__':
    a = ActiveDestructor('a')
    b = ActiveDestructor('b')
    c = ActiveDestructor('c')

    # get names
    try:
        a.printName()
    except NameError as e:
        print(e)

    try:
        b.printName()
    except NameError as e:
        print(e)

    try:
        c.printName()
    except NameError as e:
        print(e)


    # activate destructor
    print('del a')
    del a

    try:
        a.printName()
    except NameError as e:
        print('{} \n'.format(e))
