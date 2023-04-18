for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")

#The output "*" will be stop on the count of ten, because the "i" have been declared as 10, so in the IF statement already controlled
#to break if reaches ten.