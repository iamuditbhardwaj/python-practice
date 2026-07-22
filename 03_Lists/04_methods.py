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