# https://www.youtube.com/watch?v=YWY4BZi_o28
tuple_vec = (1, 0, 1)
list_vec = (1, 0, 1)

def print_vector(x, y, z):
    print('<{}, {}, {}>'.format(x, y, z))

print_vector(*tuple_vec)

gen_expr = (x * x for x in range(3))

print_vector(*gen_expr)

# ** d9ictionary unpack

dict_vec = {'x': 1, 'y': 0, 'z': 1}
print_vector(**dict_vec)

#extract keys
print_vector(*dict_vec)
