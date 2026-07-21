# Tuples

# A tuple is a collection of items just like a list. It can have items of different data type.
a = (1, 3, "Henry", 33.4, True)
print(a, type(a))
b = () # Empty tuple
print(b, type(b))
c = (2,) # Tuple with a single element
print(c, type(c))

# It is immutable.
# One cannot change an exsiting tuple in a program.


# Tuple methods:
num = (1, 2, 3, 2, 10, 4, 10, 10, 56, 70)

# 1. count() = counts the number of occurance of an assigned item.
count = num.count(2)
print(count)

# 2. index() = returns the index of the first occurance of an assigned item.
index = num.index(10)
print(index)

