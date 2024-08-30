#1. expected output of the code

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

"""
The filter function applies the lambda function (lambda x: x > 4) to each element in the data list.
It returns an iterator that contains only the elements for which the lambda function returns True.
The lambda function checks if the element is greater than 4.

so the expected output is : # o/p: [10, 501, 22, 37, 100, 999, 87, 351]

"""
# 2. Python Code Using Lambda to Check if Elements are Integers or Strings
data = [10, "hello", 22, "world", 100, "python"]

# Lambda function to check if each element is an integer or string
check_type = lambda x: "Integer" if isinstance(x, int) else "String" if isinstance(x, str) else "Other"

result = list(map(check_type, data))
print(result)

#output : ['Integer', 'String', 'Integer', 'String', 'Integer', 'String']

# 3. Python Lambda Function to Create a Fibonacci Series up to 50 Elements

# Lambda function to generate Fibonacci series up to n elements
from functools import reduce
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])

# Generate Fibonacci series up to 50 elements
fib_series = fibonacci(50)
print(fib_series)


# 4. Python Function to Validate Regular Expressions
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_bangladesh_mobile(number):
    pattern = r'^(\+88|88)?01[3-9]\d{8}$'
    return bool(re.match(pattern, number))

def validate_usa_telephone(number):
    pattern = r'^\+?1?\d{10}$'
    return bool(re.match(pattern, number))

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return bool(re.match(pattern, password))

# Example usage
print(validate_email("example@example.com"))  # True
print(validate_bangladesh_mobile("+8801700000000"))  # True
print(validate_usa_telephone("+1234567890"))  # True
print(validate_password("Aa1@123456789012"))  # True


