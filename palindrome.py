def is_palindrome(input_string):
    # Convert input string to lowercase and remove spaces
    processed_string = input_string.lower().replace(" ", "")
    
    # Return True if the processed string is equal to its reverse, else False
    return processed_string == processed_string[::-1]

# Example usage:
input_string = input("Enter a string: ")
result = is_palindrome(input_string)

print(result)
