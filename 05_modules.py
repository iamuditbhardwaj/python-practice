# Modules in Python

'''Modules are files containing Python code that can be imported and used in other Python programs.
   Modules can be built-in (provided by Python) or user-defined (created by the user).
i.e built-in modules or external modules'''

# 1. Built-in Modules
# For example, the math module provides mathematical functions and constants.
import math  
print(math.sqrt(16))  

# 2. External Modules
'''An external module can be installed using pip (Python package installer) 
   and then imported into a Python program.'''
# For example:
import pyjokes  
joke = pyjokes.get_joke() # Prints a random joke
print(joke)

