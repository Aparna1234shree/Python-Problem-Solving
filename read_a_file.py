"""
1.Read the contents of a file and display the contents.
2.Takes the function name as an argument to the function.
"""
def read_and_display_file(filename):
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            # Read the content of the file
            content = file.read()
            # Print the content to the console
            print(f"Content of '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_and_display_file("content_sample.txt")
