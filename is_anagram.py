def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if is_anagram(input_str1, input_str2):
    print(f"'{input_str1}' is an anagram of '{input_str2}'.")
else:
    print(f"'{input_str1}' is not an anagram of '{input_str2}'.")
