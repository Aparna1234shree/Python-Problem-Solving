def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def find_happy_numbers(numbers):
    happy_numbers = []
    for num in numbers:
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers

# Example usage:
input_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_nums = find_happy_numbers(input_list)

print("Happy numbers:", happy_nums)
