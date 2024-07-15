def most_frequent_char(input_string):
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with maximum frequency
    max_char = ''
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    return max_char

# Example usage:
input_string = input("Enter a string: ")
result = most_frequent_char(input_string)

print(f"The most frequent character in '{input_string}' is '{result}'")
