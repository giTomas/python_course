from concurrent import futures

def foo(x, y):
    return y - x

if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as pool:
        for result in pool.map(foo, [1,2,3], [4,5,6]):
            print(result)
