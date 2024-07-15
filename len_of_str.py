def count_words(input_string):
    # Split the input string into words based on whitespace
    words = input_string.split()
    
    # Return the number of words
    return len(words)

# Example usage:
input_string = input("Enter a string: ")
word_count = count_words(input_string)

print(f"The number of words in '{input_string}' is: {word_count}")
