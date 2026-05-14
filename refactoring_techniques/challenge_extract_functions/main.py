def remove_negatives(numbers):
    non_negative = []
    for n in numbers:
        if n >= 0:
            non_negative.append(n)
    return non_negative

def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total

def process_data(numbers):
    non_negative = remove_negatives(numbers)
    total = sum_of_squares(non_negative)
    return f"Sum of squares (non-negative numbers): {total}"

# Example usage
print(process_data([1, -2, 3, 4, -5]))