
example_list = ['a', 'b', 'c', 'd', 'e', 'f']
capitals = [x.upper() for x in example_list]
print(capitals)

example_dict = {'a': 1, 'b': 2, 'c': 3}
# items to loop trought dict
# key is k: v notation instaead it will be set!!!
squares = {k: v ** 2 for k, v in example_dict.items()}
print(squares)

example_set = {'a', 'b', 'c', 'd', 'e', 'f', '@'}
# ord() value of unicode character
codes = {ord(x) for x in example_set}
print(codes)
# char() repesentation of number in unicode
print(chr(64))

# dict and sets are similar
capital_keys = {x.upper() for x in example_dict.keys()}
print(capital_keys)
print(type(capital_keys))

#tuple compehension
example_tuple = (64, '@')
strigified = tuple(str(x) for x in example_tuple)
print(strigified)
