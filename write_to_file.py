"""
Author: <Aparna Shree R>
1. Create a text file with the current timestamp
2. File name has the current time stamp as content
"""
import datetime as dt


# create_timestamp_file function definition

def create_timestamp_file():
    # Get the current timestamp
    current_timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Define the filename using the current timestamp
    filename = f"{current_timestamp}.txt"
    # created a text file

    # Create and write the current timestamp into the file
    with open(filename, "w") as file:
        file.write(current_timestamp)

    print(f"File '{filename}' created with content: {current_timestamp}")


# function call
create_timestamp_file()
