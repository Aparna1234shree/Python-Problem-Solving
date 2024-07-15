def is_prime(num):
    """ Function to check if a number is prime """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(input_list):
    """ Function to find all prime numbers in a given list """
    prime_numbers = []
    for num in input_list:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
input_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_nums = find_primes(input_list)

print("Prime numbers:", prime_nums)
