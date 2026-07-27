# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

a = letter.replace("<|Name|>", "Henry").replace("<|Date|>", "27-07-2026")
print(a)