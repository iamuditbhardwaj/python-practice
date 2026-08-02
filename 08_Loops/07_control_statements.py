# Loop Control Statements

# 1. break -> Terminates the loop immediately.
for i in range(0,50):
    if(i==30):
        break
    print(i)

# 2. continue -> Skips the current iteration and moves to the next iteration.
for i in range(0, 11):
    if(i==8):
        continue
    print(i)

# 3. pass -> Does nothing; used as a placeholder.
for i in range(0, 15):
    pass