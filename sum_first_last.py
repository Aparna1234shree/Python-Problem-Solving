def sum_first_last_digit(number):
    # Convert number to string to easily access first and last digits
    num_str = str(number)
    
    # Get last digit using modulus
    last_digit = int(num_str[-1])
    
    # Get first digit by converting first character to integer
    first_digit = int(num_str[0])
    
    # Calculate and return the sum
    return first_digit + last_digit

# Get integer input from user
try:
    number = int(input("Enter an integer: "))
    result = sum_first_last_digit(number)
    print(f"The sum of the first and last digit of {number} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
