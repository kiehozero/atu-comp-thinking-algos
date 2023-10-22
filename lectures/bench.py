# this version follows the lecture's actual practical, the bench2 file is made purely by combining two of week
# 12's lecture slides. In the assignment you'll need to define how each part of this code is working, including
# each of the libraries and in-built functions that you are using.

import timeit
import time

# this is a script that is formatted as a string, and random_list is created using a list comprehension
setup_code = '''
import random

random_list = [random.random() for i in range(1000)]

'''

# note the semi-colon to denote a new line, and the use of a copy of the array. Once an array is sorted, it cannot be
# re-sorted, hence using cope instead of random_list. In the assignment, this sort() function will be replaced with
# your own implementation of each of the five required sorting algorithms, which you'll have to first write from scratch.
# also note that we use a copy rather than the original variable, because once a variable is sorted, it cannot be sorted
# again for the purposes of benchmarking, where you want every algorithm to start from the same starting line. As noted
# in the 'Sorting Basics' section of https://docs.python.org/3/howto/sorting.html, sort() modifies the list in place, it
# isn't creating a copy
t = timeit.Timer('copy=random_list[:]; copy.sort()', setup=setup_code)

# runs 1000 instances of the script, 7 times
runs = t.repeat(7, 1000)

# prints the time taken for each of the 7 instances, i.e. the total time taken to run each set of 1000 instances
print(runs)

# prints the minimum time obtained
print(min(runs))