# Multiple elif statements
# You can use multiple elif statements to check several conditions.
# It is also called as if else ladder

a = int(input("Enter age: "))

if(a<0):
    print("Age cannot be negative")

elif(a==0):
    print("Invalid age")

elif(a<13):  
    print("You are a child")  

elif(a<18):
    print("You are a teenager")

else:  
    print("You are an adult") 

# Note:
# Python checks the conditions from top to bottom.
# As soon as one condition becomes True, its block is executed and the remaining elif and else blocks are skipped.