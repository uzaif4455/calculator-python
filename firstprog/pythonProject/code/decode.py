# For Encoding
# Taking input from the user
'''a = input("Enter your message: ")

# Checking if the length of the input is less than or equal to 3
if len(a) <= 3:
    # Reversing the input string
    a = a[::-1]
    print(a)
# If the length is greater than or equal to 3
elif len(a) >= 3:
    # Taking input for the starting and ending characters
    starting = input("Enter 3 characters at the starting point: ")
    ending = input("Enter 3 characters at the ending point: ")
    # Modifying the input string
    modified = a[1:] + a[0]
    # Combining the starting characters, modified string, and ending characters
    add = starting + modified + ending
    print(add)

# For Decoding
# Taking input from the user
b = input("Enter your decoded message: ")

# Checking if the length of the input is less than or equal to 3
if len(b) <= 3:
    # Reversing the input string
    b = b[::-1]
    print(b)
# If the length is greater than or equal to 3
elif len(b) >= 3:
    # Extracting the modified part of the decoded message
    again_modified = b[3:-4]
    # Reconstructing the original modified string
    modified = again_modified
    # Extracting the decoded starting character
    modified_decode = b[-4]
    # Reconstructing the original decoded message
    modified = modified_decode + again_modified
    print(modified)'''
