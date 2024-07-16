def has_zero_sum_sublist(lst):
    cumulative_sum = 0
    seen_sums = set()

    for num in lst:
        cumulative_sum += num
        # Check if cumulative sum is 0 or already seen
        if cumulative_sum == 0 or cumulative_sum in seen_sums:
            return True
        seen_sums.add(cumulative_sum)
    
    return False

# Example list
lst = [4, 2, -3, 1, 6]

# Check if there is a sublist with sum equal to zero
result = has_zero_sum_sublist(lst)

# Print the result
if result:
    print("There is a sublist with sum equal to zero.")
else:
    print("There is no sublist with sum equal to zero.")
