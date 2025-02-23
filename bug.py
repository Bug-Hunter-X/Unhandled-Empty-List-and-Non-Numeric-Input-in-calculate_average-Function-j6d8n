def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") #This will return 0, which may not be desired behavior if an error should be raised

my_list_with_zero = [1, 0, 3, 0, 5]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}") #This works fine

my_list_with_strings = [1, 2, 'a', 4, 5]
result = calculate_average(my_list_with_strings) # This will raise a TypeError
print(f"The average is: {result}")