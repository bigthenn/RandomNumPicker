import random

# Get the lower and upper bounds of the range
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

# Generate a random number within the specified range
random_number = random.randint(lower_bound, upper_bound)

# Print the random number
print("The random number is:", random_number)
