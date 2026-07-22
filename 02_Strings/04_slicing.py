# String Slicing
# You can extract a portion of a string using slicing. Slicing allows you to specify a start index and an end index. 
# It will return the substring from the start index up to, but not including, the end index.
# Syntax: variable_name = string[start:end]
# Start index will be included in the substring, while the end index will not be included.
# Example:
slicing = "Python"
print(slicing[0:3])  # Output: Pyt
print(slicing[2:5])  # Output: tho

# Negative slicing can be done in similar manner.
# Example:
print(slicing[-6:-3])  # Output: Pyt
print(slicing[-4:-1])  # Output: tho

# print(slicing[0:3]) and print(slicing[-6:-3]) will give the same output as both are referring to the same characters in the string.
# Also print(slicing[:3]) and print(slicing[0:3]) will give the same output as the start index is optional and defaults to 0 if not specified.
# Same goes for the end index, if not specified it defaults to the length of the string.

# Strings can also be sliced with a step value, which allows you to skip characters in the string. 
# Syntax : variable_name = string[start:end:step]
# Example:
step_slicing = "123456789"
print(step_slicing[0:9:2])  # Output: 13579