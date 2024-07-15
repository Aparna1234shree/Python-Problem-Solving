def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

# Example usage:
input_list = [10, 501, 22, 37, 100, 999, 87, 351]
even_nums, odd_nums = separate_even_odd(input_list)

print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
