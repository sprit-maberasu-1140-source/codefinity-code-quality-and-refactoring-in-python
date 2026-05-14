def get_even_squares(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n ** 2)
    return result

nums = [1, 2, 3, 4, 5, 6]
print(get_even_squares(nums))  # Should print: [4, 16, 36]
