def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

def double_evens(numbers):
    return [n * 2 if n % 2 == 0 else n for n in numbers]

def max_of_two(a, b):
    return max(a, b)

numbers = [1, 2, 3, 4]
print(append_to_list(5))          # [5]
print(double_evens(numbers))      # [1, 4, 3, 8]
print(max_of_two(10, 20))         # 20