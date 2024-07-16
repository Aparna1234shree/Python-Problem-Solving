def find_duplicates(list1, list2, list3):
    # Convert lists to sets to remove duplicates within each list
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find the common elements in all three sets
    common_elements = set1.intersection(set2).intersection(set3)
    
    return list(common_elements)

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 7, 8, 9, 10]

# Find duplicates
duplicates = find_duplicates(list1, list2, list3)

# Print the duplicates
print("Duplicates in all three lists:", duplicates)
