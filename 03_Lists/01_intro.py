# Lists

# Lists are a collection of items of same or different data types. 
# They are mutable, meaning you can change their content without changing their identity. 
# Lists are defined by enclosing elements in square brackets [].
# Syntax: list_name = [item1, item2, item3, ...]
# Example:

list_1 = [1, 2, 3, 4, 5]
list_2 = ["apple", "banana", "cherry"]
list_3 = [1, "apple", 3.14, True]   
print(list_1)
print(list_2)
print(list_3)

# As lists are mutable, you can change their content by assigning new values to specific indices.
# Example:
list_1[0] = 10
print(list_1)  # Output: [10, 2, 3, 4, 5]
