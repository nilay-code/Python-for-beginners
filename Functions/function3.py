x = input("Enter a number\n")

x = int(x)

def even(nb):
    
    if nb%2==0:
        return True
    else:
        return False

print(even(x))
