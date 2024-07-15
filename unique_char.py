def most_unique_char(input_string):
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count occurrences of each character in the input string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Initialize variables to track the most unique character
    unique_char = None
    min_count = float('inf')  # Start with a very large number
    
    # Iterate over the characters and their counts
    for char, count in char_count.items():
        # Check if the character appears exactly once and update if it's the most unique so far
        if count == 1:
            if count < min_count:
                unique_char = char
                min_count = count
    
    return unique_char

# Example usage:
input_string = input("Enter a string: ")
result = most_unique_char(input_string)

if result:
    print(f"The most unique character in '{input_string}' is '{result}'.")
else:
    print("No unique character found in the input string.")
