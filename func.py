def foo():
    pass

print(foo)

bar = foo

print(bar)

print(bar.__name__)

bar.plugin_name = 'demo'

print(bar.plugin_name)

import atexit
print(atexit.register(bar))
