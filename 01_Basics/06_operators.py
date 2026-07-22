# Operators in Python

# 1. Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)  # Division
print("Modulus:", a % b)  # Modulus

# 2. Assignment Operators
c = 20
print("Simple Assignment:", c)  # Simple Assignment
c += 5  # Equivalent to c = c + 5
print("Addition Assignment:", c)  # Addition Assignment
c -= 5  # Equivalent to c = c - 5
print("Subtraction Assignment:", c)  # Subtraction Assignment
c *= 5  # Equivalent to c = c * 5
print("Multiplication Assignment:", c)  # Multiplication Assignment
c /= 5  # Equivalent to c = c / 5
print("Division Assignment:", c)  # Division Assignment

# 3. Comparison Operators
x = 10
y = 20  
print("Equal:", x == y)  # Equal
print("Not Equal:", x != y)  # Not Equal
print("Less Than:", x < y)  # Less Than
print("Greater Than:", x > y)  # Greater Than
print("Less Than or Equal:", x <= y)  # Less Than or Equal
print("Greater Than or Equal:", x >= y)  # Greater Than or Equal

# 4. Logical Operators
p = True
q = False

# Truth table for Logical AND
print("True and True is:", p and p )
print("True and False is:", p and q )
print("False and True is:", q and p )
print("False and False is:", q and q )

# Truth table for Logical OR
print("True or True is:", p or p )
print("True or False is:", p or q )
print("False or True is:", q or p )
print("False or False is:", q or q )

# Truth table for Logical NOT
print("True is: ", not(p))
print("False is: ", not(q))
