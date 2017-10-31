import math

def example_function(name: str, radius: float) -> str:
    area = math.pi * radius ** 2
    return "The area of {} is {}".format(name, area)


print(example_function(5, 5.5))
