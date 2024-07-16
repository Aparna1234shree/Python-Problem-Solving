def find_min_in_rotated_sorted_list(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If the mid element is greater than the rightmost element,
        # then the minimum element is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum element is in the left half
            right = mid
    
    # At the end of the while loop, left == right and pointing to the minimum element
    return nums[left]

# Example list
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]

# Find the minimum element
min_element = find_min_in_rotated_sorted_list(rotated_sorted_list)

# Print the result
print("The minimum element in the rotated sorted list is:", min_element)
