# def proxy(func):
#     def wrapper(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print('TRACE: calling {}()\nwith {}, {}'.format(func.__name__, args, kwargs))

        original_result = func(*args, **kwargs)

        print('TRACE: {}()\nreturned {}'.format(func.__name__, original_result))

    return wrapper

@trace
def say(name, line):
    return('{}: {}'.format(name, line))

say('Jane', 'Hello, World')
