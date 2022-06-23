""" #LIST COMPREHENSION [Videos 1 & 2]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main():
    final_list = []
    for n in my_list:
        final_list.append(n+10)

    print(final_list)

    #TODO: Using Comprehension
    final_list_comp1 = [n + 10 for n in my_list]
    print(final_list_comp1)

    #TODO: Using Comprehension & condition
    final_list_comp2 = [n + 10 for n in my_list if n % 2 == 0]
    print(final_list_comp2)

if __name__ == '__main__':
    main()


def main():
    my_numbers = [18, 32, 74, 34, 69, 2, 4, 52, 61, 32, 11, 5, 17, 95, 96, 18, 38, 35, 49, 89, 54, 44, 99, 29]
    my_numbers_double = []
    for n in my_numbers:
        my_numbers_double.append(n*2)
    print(my_numbers_double)

    #TODO: Using Comprehension
    my_numbers_double_comp1 = [n*2 for n in my_numbers]
    print(my_numbers_double_comp1)

    #TODO: Using Comprehension & condition (evens)
    my_numbers_double_comp2 = [n*2 for n in my_numbers if n % 2 == 0]
    print(my_numbers_double_comp2)

    #TODO: Using Comprehension & condition (odds)
    my_numbers_double_comp3 = [n*2 for n in my_numbers if 10 < n < 50]
    print(my_numbers_double_comp3)

if __name__ == '__main__':
    main()






#DICTIONARY COMPREHENSION [Videos 3 - 5]
def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_num_dict = {}
    for n in my_list:
        my_num_dict[n] = n ** 2
    print(my_num_dict)

    #TODO: Using Comprehension
    my_num_dict_comp1 = {n: n**2 for n in my_list}
    print(my_num_dict_comp1)

    #TODO: Using Comprehension & condition
    my_num_dict_comp2 = {n: n ** 2 for n in my_list if n % 2 == 0}
    my_num_dict_comp3 = {n: n ** 2 for n in my_list if 3 < n < 9}
    my_num_dict_comp4 = {n: n ** 2 for n in my_list if n % 2 == 0 if 3 < n < 9}
    print(my_num_dict_comp2)
    print(my_num_dict_comp3)
    print(my_num_dict_comp4)

if __name__ == '__main__':
    main()

def main():
    states = ["Texas", "California", "Colorado", "Arizona", "Georgia"]
    capitals = ["Austin", "Sacramento", "Denver", "Phoenix", "Atlanta"]

    #Create a dictionary with key as numbere & value as the squared of the number
    my_state_cap_dict = {}
    for state in states:
        for capital in capitals:
            if states.index(state) == capitals.index(capital):
                my_state_cap_dict[state] = capital
    print (my_state_cap_dict)

    #TODO: Using zip
    state_capitals = zip(states, capitals)
    print(dict(state_capitals))

    #TODO: Using comprehension
    states_capitals_comp = {s: c for s in states for c in capitals if states.index(s) == capitals.index(c)}
    print(states_capitals_comp)

if __name__ == '__main__':
    main()

def main():
    scores = {'Texas': 10, 'California': 30, 'Colorado': 49, 'Arizona': 33, 'Florida': 55}

    # #Creating dictionary with squared values
    # for item in scores:
    #     scores[item] *= 2
    # print(scores)

    # #TODO: Using comprehension
    # scores_comp1 = {key: value * 2 for (key, value) in scores.items()}
    # print(scores_comp1)

    # #TODO: Using Comprehension & conditions (2)
    # scores_comp2 = {key: value * 2 for (key, value) in scores.items() if value <= 50 if value != 49}
    # print(scores_comp2)

    #TODO: Using Comprehension & conditions (3)
    scores_comp3 = {key: value * 2 for (key, value) in scores.items() if value <= 50 if value != 49 if value != 10}
    print(scores_comp3)

if __name__ == '__main__':
    main()

 """





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
