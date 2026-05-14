def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def greet_user(name, greeting="Hello"):
    """
    Print a greeting message to a user.

    Parameters:
        name (str): The name of the user.
        greeting (str, optional): The greeting message. Defaults to "Hello".

    Returns:
        None
    """
    print(f"{greeting}, {name}!")

def find_max(numbers):
    """
    Find the maximum value in a list of numbers.

    Parameters:
        numbers (list of int or float): The list of numbers to search.

    Returns:
        int or float or None: The maximum value in the list, or None if the list is empty.
    """
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

add_numbers(2, 3)
greet_user("Alice")
find_max([4, 7, 1, 3])