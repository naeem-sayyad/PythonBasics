print("welcome to reverse string program")

noob = input("enter the string you want: ")  # Get user input
reversed_string = ""  # Initialize empty string for result

for char in noob:  # Loop through each character in the input string
    reversed_string = char + reversed_string  # Prepend each character

print(reversed_string)