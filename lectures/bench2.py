# combines slides Time in Python III and Time in Python IV from wk 12 slides
import random
import timeit

num_runs = 10
results = []
for r in range(num_runs):
    start_time = timeit.default_timer()

    def random_array(n):
        array = []
        for i in range(0,n,1):
            array.append(random.randint(0,100))
        return array
    
    end_time = timeit.default_timer()
    time_elapsed = end_time - start_time
    results.append(time_elapsed);

print(results)