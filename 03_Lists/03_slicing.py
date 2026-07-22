# List Slicing:
slicing = [10, 20, 30, 40, 50]
print(slicing[1:4])  # Output: [20, 30, 40]
print(slicing[:3])   # Output: [10, 20, 30]
print(slicing[2:5])  # Output: [30, 40, 50]
# And so on.....

# Lists can also be sliced with a step value, which allows you to skip elements in the list.
step_slicing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(step_slicing[0:9:2])  # Output: [1, 3, 5, 7, 9]