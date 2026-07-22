# Modules in Python

'''Modules are files containing Python code that can be imported and used in other Python programs.
   Modules can be built-in (provided by Python) or external (installed separately).'''

# 1. Built-in Modules
# For example, the math module provides mathematical functions and constants.
import math  
print(math.sqrt(16))  

# 2. External Modules
'''An external module can be installed using pip (Python package installer) 
   and then imported into a Python program.'''
# For example:
# To install an external module, you can use the following command in the terminal:
# pip install pyjokes
import pyjokes  
joke = pyjokes.get_joke() # Gets a random joke
print(joke)

