def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example usage:
my_numbers = [10, 20, 30, 40, 50]
avg = calculate_average(my_numbers)
print(f"Average: {avg}")

my_empty_list = []
avg_empty = calculate_average(my_empty_list)
print(f"Average of empty list: {avg_empty}") #This will print 0

#Example of ZeroDivisionError
my_numbers_2 = []
#This will throw ZeroDivisionError
avg_error = calculate_average(my_numbers_2)