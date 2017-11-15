# from demopackage import data
from pkgutil import get_data

with open('demopackage/data/datafile.txt') as f:
    for line in f:
        try:
            print(line)
        except ValueError:
            print('nothing')

# name of the pakage, relative path
data = get_data('demopackage', 'data/datafile.txt')
print(data)
list = data.splitlines()
print(list)


# unicode text string
data2 = get_data('demopackage', 'data/datafile.txt').decode('utf8')
print(data2)
list = data2.splitlines()
print(list)


with open('demopackage/data/datafile.txt') as f:
    list = [line.split(',') for line in f.readlines()]
    print(list)

with open('demopackage/data/datafile.txt') as f:
    list = []
    for line in f:
        list.append(line)
    print(list)
