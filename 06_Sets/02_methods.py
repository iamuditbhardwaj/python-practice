# Set methods:
s = {1, 7, 8, 84, 97}
print(s)

# 1. add() = adds an element to the set
s.add(54)
print(s)

# 2. update([]) = adds multiple elements to a set
s.update([53, 44])
print(s)

# 3. remove() = removes the element from the set
s.remove(7)
print(s)

# 4. pop() = removes an element randomly from the set and returns the element removed.
value = s.pop()
print(value)
print(s)

# 5. clear() = removes all the elements from the set
s.clear()
print(s)

s1 = {97, 8, 84}
s2 = {53, 54, 44, 8, 84}
# 6. union() = combines both sets.
a = s1.union(s2)
print(a)

# 7. intersection() = seperates the common elements
b = s1.intersection(s2)
print(b)
