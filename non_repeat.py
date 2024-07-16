def find_first_non_repeating_integer(lst):
    # Create a dictionary to store the frequency of each integer
    frequency = {}
    
    # Count the frequency of each integer in the list
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
            
    # Find and return the first integer with a frequency of 1
    for num in lst:
        if frequency[num] == 1:
            return num
            
    return None  # Return None if there is no non-repeating integer

# Example list
lst = [4, 5, 1, 2, 0, 4, 1, 2]

# Find the first non-repeating integer
result = find_first_non_repeating_integer(lst)

# Print the result
if result is not None:
    print("The first non-repeating integer is:", result)
else:
    print("There is no non-repeating integer in the list.")
