def strong(func):
    def wrapper():
        return '<strong>{}</strong>'.format(func())
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>{}</em>'.format(func())
    return wrapper

@emphasis
@strong
def greet():
    return 'Hello!'
