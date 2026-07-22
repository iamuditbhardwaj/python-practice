# Tuple Slicing:
tuple = (100, 200, 300, 400, 500)
print(tuple[1:4])  # Output: (200, 300, 400)
print(tuple[:3])   # Output: (100, 200, 300)
print(tuple[2:5])  # Output: (300, 400, 500)
# And so on.....

# Tuples can also be sliced with a step value, which allows you to skip elements in the tuple.
step_slicing = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(step_slicing[0:9:2])  # Output: (1, 3, 5, 7, 9)