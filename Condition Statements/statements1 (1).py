age = input("Please enter your age: \n")

try:
    age = int(age)
except:
    age = ("Please enter a valid age: \n")
    age = int(age)


if age>10:

    
    lang = = input("Do you speak english or spanish(Yes/No)

    if lang=="Yes":
        print("You can create an account")
    elif lang=="No":
        print("You can't create ana account")

        
    # eng = input("Do you speak english(Yes/No)")
    # if eng =="Yes":
        #  print("You can create an account")
    # elif eng=="No":
    #     spa  = input("Do you speak spanish(Yes/No)")
    #     if spa=="Yes":
    #         print("You can create an account")
    # else:
    #     print("You can't create ana account")

else:
    print("You can't create an account")