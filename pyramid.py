# Define the maximum number of rows in the pyramid
max_rows = 10

# Initialize a counter for numbers
number = 1

# Iterate over each row
for i in range(1, max_rows + 1):
    # Print leading spaces to center-align the pyramid
    print(' ' * (max_rows - i), end='')
    
    # Iterate over each column in the current row
    for j in range(1, i + 1):
        # Print the current number and increment it
        print(f'{number:2}', end=' ')
        number += 1
    
    # Move to the next line after each row is printed
    print()
