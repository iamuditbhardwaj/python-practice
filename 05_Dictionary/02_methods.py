# Dictionary Methods:
a = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 1. items(): Returns a list of all key-value pairs in the dictionary.
print(a.items())

# 2. values(): Returns a list of all values in the dictionary.
print(a.values())

# 3. keys(): Returns a list of all keys in the dictionary.
print(a.keys())

# 4. get(): Returns the value of the specified key.
print(a.get("name"))
print(a.get("country", "Not Found"))  # Returns "Not Found" if the key does not exist.

#5. update(): Updates the dictionary with the specified key-value pairs.
a.update({"country": "USA", "age": 31})
print(a)

# 6. pop(): Removes the specified key and returns the corresponding value.
print(a.pop("age"))