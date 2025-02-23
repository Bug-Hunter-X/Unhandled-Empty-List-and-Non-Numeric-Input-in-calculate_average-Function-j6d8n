def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("Input list must contain only numbers")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
try:
    result = calculate_average(my_empty_list)
    print(f"The average is: {result}")
except ValueError as e:
    print(f"Error: {e}")

my_list_with_strings = [1, 2, 'a', 4, 5]
try:
    result = calculate_average(my_list_with_strings)
    print(f"The average is: {result}")
except TypeError as e:
    print(f"Error: {e}")
