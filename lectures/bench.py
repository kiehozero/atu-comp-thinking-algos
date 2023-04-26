import timeit
import time

setup_code = '''
import random

random_list = [random.random() for i in range(100000)]

'''

t = timeit.Timer('copy=random_list[:]; copy.sort()', setup=setup_code)

runs = t.repeat(7, 1000)

print(runs)

print(min(runs))