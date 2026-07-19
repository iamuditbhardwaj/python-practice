# Typecasting

# Typecasting in Python is a process of converting a value from one datatype to another
# There are certain build-in functions for conversion of data type.

# 1. int() - Converts a value to a integer 
# 2. float() - Converts a value to a float-point number  
# 3. str() - Converts a value to a string  
# 4. bool() - Converts a value to a boolean 

#For example:

# string to integer conversion:
a1 = "97"
print(type(a1))
a2 = int(a1)
print(type(a2))

# integer to float conversion:
b1 = 84
print(type(b1))
b2 = float(b1)
print(type(b2))

# float to boolean conversion:
c1 = 3.14
print(type(c1))
c2 = bool(c1)
print(type(c2))

# And so on......

# There are a few exceptions while typecasting.
# Some values cannot be converted to certain data types.
# For example:

# A string containing letters cannot be converted to an integer or float.
# Example: int("Hello")  -> ValueError

# A string representing a decimal number cannot be directly converted to an integer.
# Example: int("3.14")   -> ValueError
# It must first be converted to float, then to int.
# Note: When number is converted from float to integer datatype, integer part of the number is taken and decimal part is removed.

# Converting a float to an integer removes the decimal part.
# Example: int(3.14) -> 3
