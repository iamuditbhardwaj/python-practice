# Strings
# Strings are sequences of characters enclosed in quotes.
# Strings can be created using single quotes, double quotes, or triple quotes (for multi-line strings).

# Single quotes
a = 'Hello, World!'
print(a)

# Double quotes
b = "Hello, World!"
print(b)

# Triple quotes (for multi-line strings)
c = """This is a multi-line string."""
print(c)


# Strings are immutable, meaning that once a string is created, it cannot be changed. 
# However, you can create a new string based on an existing one.
# Creating a new string from existing string is called string concatenation. You can concatenate strings using the + operator.
# Example:

string_1 = "Good"
string_2 = "Morning"
new_string = string_1 + " " + string_2
print(new_string)


# Strings can be indexed. Each character in a string has an index, starting from 0 for the first character i.e left to right.
# Example:

indexing = "Hello"
print(indexing[0])  # Output: H
print(indexing[1])  # Output: e
print(indexing[2])  # Output: l 
print(indexing[3])  # Output: l
print(indexing[4])  # Output: o

# Strings can also be indexed as negative numbers, starting from -1 for the last character i.e from right to left.
# Example:
print(indexing[-1])  # Output: o
print(indexing[-2])  # Output: l
print(indexing[-3])  # Output: l
print(indexing[-4])  # Output: e
print(indexing[-5])  # Output: H

# String Slicing
# You can extract a portion of a string using slicing. Slicing allows you to specify a start index and an end index, and it will return the substring from the start index up to, but not including, the end index.
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

# Strings can also be sliced with a step value, which allows you to skip characters in the string. 
# Syntax : variable_name = string[start:end:step]
# Example:
step_slicing = "123456789"
print(step_slicing[0:9:2])  # Output: 13579

# String Functions:

function_1 = "mathematics"
function_2 = "MATHS"

# 1. len() - Returns the length of the string
print(len(function_1))
print(len(function_2))  

# 2. startswith() - Returns True if the string starts with the specified prefix, otherwise False
print(function_1.startswith("math"))  
print(function_1.startswith("Hello"))  

# 3. endswith() - Returns True if the string ends with the specified suffix, otherwise False
print(function_1.endswith("Hello"))  
print(function_2.endswith("HS"))  

# 4. capitalize() - Capitalizes the first character of the string and converts the rest to lowercase.
print(function_1.capitalize())  # Output : Mathematics
print(function_2.capitalize())  # Output : Maths

# 5. upper() - Converts all characters in the string to uppercase
print(function_1.upper())

# 6. lower() - Converts all characters in the string to lowercase
print(function_2.lower())


function_3 = "I love Programming. Programming is fun."

# 7. find() - Returns the index of the first occurrence of the specified substring, or -1 if not found
print(function_3.find("Programming")) # Output : 7
print(function_3.find("xyz")) # Output : -1

# 8. replace() - Replaces all occurrences of a specified substring with another substring
print(function_3.replace("Programming", "Coding"))  

# 9. count() - Returns the number of occurrences of a specified substring in the string
print(function_3.count("Programming"))  # Output : 2
