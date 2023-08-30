comment = input("Enter your comment")

if("make a lot of money" in comment):
    spam = True
elif("buy now"in comment):
    spam = True
elif("subscirbe this"in comment):
    spam = True
elif("click this"in comment):
    spam = True
else:
    spam = False
if(spam == True):
    print("Your text is spam")
else:
    print("Your text is not a spam")