import time

times = time.time()
print(times)

def speed_calc_decorator(function):
    def wrapped_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time-start_time}s")
    return wrapped_function

@speed_calc_decorator
def fast_calculation():
    for i in range(1000000):
        i*i

@speed_calc_decorator
def slow_calculation():
    for i in range(1000000):
        i*i

fast_calculation()
slow_calculation()

# Output

# 1707405316.373305
# fast_calculation run speed: 0.03440690040588379s
# slow_calculation run speed: 0.026829957962036133s

