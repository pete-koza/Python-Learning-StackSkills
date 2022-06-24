""" 
#NESTED FUNCTIONS
def my_outer_function():
    def my_inner_function():
        print("Hello from inner function")
    print("Hello from outer function")
    return my_inner_function

x = my_outer_function()

x() """




#DECORATORS
from functools import wraps
from time import sleep, perf_counter
import random

def hello_message_decorator(func):
    """ This is a hello message decorator """
    @wraps(func)
    def wrapper():
        """ This is a wrapper inside the hello message decorator """
        for n in range(5):
            t_start = perf_counter()
            func()
            t_end = perf_counter()
            duration = t_end - t_start
            print(round(duration, 3))
    return wrapper

@hello_message_decorator
def hello_message():
    sleep(random.randint(1,5))
    """ This is a hello message function """
    return 'hello'

print(hello_message())

# message = hello_message_decorator(hello_message())
# print(message())