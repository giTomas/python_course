from multiprocessing import Process

# overide run method
class Squares(Process):
    def run(self):
        for i in range(10):
            print(i ** 2)

if __name__ == '__main__':
    squares = Squares()
    squares.start()
