# Multiple if statements
# A program can contain more than one if statement.

a = int(input("Enter number: "))

# First if statement:
if(a%2==0):
    print("Even")
# End of first if statement

# Second if statement:
a = int(input("Enter age: "))

if(a<13):  
    print("You are a child")  

elif(a<18):
    print("You are a teenager")

else:  
    print("You are an adult")
# End of second if statement

# Both if statements are independent and will be checked separately.
# An if statement can exist without elif or else.
# However, elif and else cannot exist without an if statement.