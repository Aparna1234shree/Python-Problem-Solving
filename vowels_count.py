# Define the input string
input_string = "Guvi Geeks Network Private Limited"

# Convert the input string to lowercase to handle case insensitivity
input_string = input_string.lower()

# Initialize variables to count total vowels and individual vowels
total_vowels = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Iterate through each character in the string
for char in input_string:
    if char in "aeiou":
        total_vowels += 1
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

# Print the results
print("Total number of vowels:", total_vowels)
print("Number of 'a' :", count_a)
print("Number of 'e' :", count_e)
print("Number of 'i' :", count_i)
print("Number of 'o' :", count_o)
print("Number of 'u' :", count_u)
