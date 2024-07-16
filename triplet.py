def find_triplet_with_sum(lst, target_sum):
    n = len(lst)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return lst[i], lst[j], lst[k]
    return None

# Example list and target sum
lst = [10, 20, 30, 9]
target_sum = 59

# Find the triplet
result = find_triplet_with_sum(lst, target_sum)

# Print the result
if result:
    print("Triplet found:", result)
else:
    print("No triplet found with the given sum.")
