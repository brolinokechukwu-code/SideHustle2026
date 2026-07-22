# Ask the user for their name
name = input("What is your name? ")

# Removes whitespace from str and capitalize users name
name = name.strip()

# Capitalize name
name = name.title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {last}") 