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

# A list can be indexed and sliced in the same way as strings.

# List Indexing:
indexing = ["a", "b", "c", "d", "e"]
print(indexing[0])  # Output: a
print(indexing[2])  # Output: c
print(indexing[-1]) # Output: e
# And so on.....

# List Slicing:
slicing = [10, 20, 30, 40, 50]
print(slicing[1:4])  # Output: [20, 30, 40]
print(slicing[:3])   # Output: [10, 20, 30]
print(slicing[2:5])  # Output: [30, 40, 50]
# And so on.....

# Lists can also be sliced with a step value, which allows you to skip elements in the list.
step_slicing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(step_slicing[0:9:2])  # Output: [1, 3, 5, 7, 9]

# List Methods:
num = [84, 8, 97, 54, 53, 23, 10]

# append(): Adds an element at the end of the list.
num.append(100)
print(num)  

# sort(): Sorts the list in ascending order.
num.sort()
print(num)  

# reverse(): Reverses the order of the list.
num.reverse()
print(num)

# insert(): Inserts an element at the specified position.
num.insert(2, 90)  
print(num)

# remove(): Removes the first occurrence of the specified element from the list.
num.remove(23)
print(num)

# pop(): Removes the element at the specified position (or the last element if no index is specified) and returns it.
popped_element = num.pop(2)
print(popped_element) 
print(num) 