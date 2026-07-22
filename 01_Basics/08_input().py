# Input() Function in Python

# This function allows the user to take input from the keyboard.
# By default, input() returns the user's input as a string.
# Syntax: variable_name = input()

name = input("Enter name: ")
print(name, type(name))

# Note: The input() function always returns the user's input as a string, even if the user enters a number.

# To use the input() as a integer or float, apply typecasting.
# Syntax: variable_name = data_type(input())

age = int(input("Enter age: "))
print(age, type(age))

height = float(input("Enter height: "))
print(height, type(height))
