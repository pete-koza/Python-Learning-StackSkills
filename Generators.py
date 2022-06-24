#G GENERATORS
# def my_generator():
#     yield 100
#     yield 200
#     yield 300
#     yield 400

# x = my_generator()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# print('-' * 20)
# for n in x: # If a for loop comes after generator exhausts yields, nothing happens, unless you put another print(x.__next__()) right above it.
#     print(n)



# from unittest import result

# def my_numbers_squared(n):
#     result = []
#     for x1 in range(n):
#         result.append(x1 ** 2)
#     return result

# def my_numbers_squared_gen(m):
#     for x2 in range(m):
#         yield x2 * x2

# print('-' * 20)
# print(my_numbers_squared(5))
# print('-' * 20)
# print(list(my_numbers_squared_gen(5)))

# print('-' * 20)
# gen1 = my_numbers_squared_gen(5)
# print(gen1.__next__())
# print(next(gen1))


# Generator function to generator expression


# # Processing a list
# animals = ['dog', 'cat', 'hen', 'fox', 'rat']
# #TODO: Generator expression <<
# animals_upper_gen = (animal.upper() for animal in animals)
# #TODO: Print
# print(list(animals_upper_gen))


# Generator Pipeline
def odd_filter(nums):
    for num in nums:
        if num % 2 == 1:
            yield num

def squared(nums):
    for num in nums:
            yield num ** 2

def ending_in_1(nums):
    for num in nums:
        if num % 10 == 1:
            yield num

def convert_to_string(nums):
    for num in nums:
        yield "Match Found --> " + str(num)

gen_pipeline = convert_to_string(ending_in_1(squared(odd_filter(range(1000)))))

for n in gen_pipeline:
    print(n)
