# String methods:

string_1 = "mathematics"
string_2 = "MATHS"

# 1. len() - Returns the length of the string
print(len(string_1))
print(len(string_2))  

# 2. startswith() - Returns True if the string starts with the specified prefix, otherwise False
print(string_1.startswith("math"))  
print(string_1.startswith("Hello"))  

# 3. endswith() - Returns True if the string ends with the specified suffix, otherwise False
print(string_2.endswith("Hello"))  
print(string_2.endswith("HS"))  

# 4. capitalize() - Capitalizes the first character of the string and converts the rest to lowercase.
print(string_1.capitalize())  # Output : Mathematics
print(string_2.capitalize())  # Output : Maths

# 5. upper() - Converts all characters in the string to uppercase
print(string_1.upper())

# 6. lower() - Converts all characters in the string to lowercase
print(string_2.lower())


function_3 = "I love Programming. Programming is fun."

# 7. find() - Returns the index of the first occurrence of the specified substring, or -1 if not found
print(function_3.find("Programming")) # Output : 7
print(function_3.find("xyz")) # Output : -1

# 8. replace() - Replaces all occurrences of a specified substring with another substring
print(function_3.replace("Programming", "Coding"))  

# 9. count() - Returns the number of occurrences of a specified substring in the string
print(function_3.count("Programming"))  # Output : 2