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
<<<<<<< HEAD
# from functools import wraps
# from time import sleep, perf_counter
# import random

# def hello_message_decorator(func):
#     """ This is a hello message decorator """
#     @wraps(func)
#     def wrapper():
#         """ This is a wrapper inside the hello message decorator """
#         for n in range(5):
#             t_start = perf_counter()
#             func()
#             t_end = perf_counter()
#             duration = t_end - t_start
#             print(round(duration, 3))
#     return wrapper

# @hello_message_decorator
# def hello_message():
#     sleep(random.randint(1,5))
#     """ This is a hello message function """
#     return 'hello'

# print(hello_message())

# # message = hello_message_decorator(hello_message())
# # print(message())

# 1. Implement decorator to return "S3cR3T" by the wrapper function.
# 2. Implement wraps
# 3. Modify get_secure_message function to take two integers as arguments. These arguments will be used as from & to values for the range.
#    Use sleep function to randomly sleep for n seconds where n is from the range above. 
#    Your wrapper function will have to accept the arguments as well. 
#    Simulate the performance testing using a for loop.
# from functools import wraps
# from time import sleep, perf_counter
# import random


# def get_secure_message_decorator(func):
#     """This is secure message decorator"""
#     @wraps(func)
#     def wrapper(n, m):
#         """This is wrapper inside get_secure_message decorator"""
#         for x in range(5):
#             t_start = perf_counter()
#             func(n,m)
#             t_end = perf_counter()
#             duration = t_end - t_start
#             print('{} Iteration {} --> Duration: {:.3f}'.format(func.__name__, x + 1, duration))
#             return "S3cR3T"
#         return wrapper

# @get_secure_message_decorator
# def get_secure_message(n, m):
#     """This is secure message function"""
#     sleep(random.randit(n, m))
#     return 'secret'
# print(get_secure_message(1, 3))
=======
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
>>>>>>> 700eb67a824a7ee80aabd31aef9c4b8c4e770399
