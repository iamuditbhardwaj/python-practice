# What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))

# Reason:
# Python considers both as 1 because their values are equal
# i.e 20 == 20.0 which is true.
# '20' is not a number, it is a string.
# This is why the length of the following set is 2 instead of 3.

