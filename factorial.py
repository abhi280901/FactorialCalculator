l = int(input("Please enter a number:"))
def factorier(x):
    if x>0:
        if x-1!=0:
            result = x*factorier(x-1)
            return result
        elif x-1==0:
            result = 1
            return result
    else:
        if x + 1 != 0:
            result = -(x * factorier(x + 1))
            return result
        elif x+1==0:
            result = -1
            return result
print("The factorial of ",l," is ",factorier(l),"!")