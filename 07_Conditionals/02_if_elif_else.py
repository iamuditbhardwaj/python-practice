# If elif else statement
# More than one condition can be checked using if, elif, and else.
# Syntax:
""" if(condition1):
        print()
    elif(condition2):
        print()
    else:
        print()"""

# Example:
a = int(input("Enter age: "))

if(a<13):  
    print("You are a child")  

elif(a<18):
    print("You are a teenager")

else:  
    print("You are an adult") 

# The excution of elif will only take place when the above if condition will be false.
# And the execution of else statement only takes place, when all the above conditions are false.