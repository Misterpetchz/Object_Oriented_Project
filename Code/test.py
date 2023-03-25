my_list = ["apple", "banana", "orange", "pear", "grape"]

# Ask user for input
search_str = input("Enter a search string: ").lower()

# Iterate over list and check if each element contains the search string (case-insensitive)
for element in my_list:
    if search_str in element.lower():
        print(f"Found element: {element}")