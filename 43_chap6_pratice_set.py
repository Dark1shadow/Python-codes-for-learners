num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
num3 = int(input("Enter number 3:\n"))
num4 = int(input("Enter number 4:\n"))
if (num1>num2 and num1>num3 and num1>num4):
    print("num1 is the greatest number", num1)
elif(num2>num3 and num2>num4):
    print("num2 is greatest number", num2)
elif(num3>num4):
    print("num3 is greatest", num3)
else:
    print("num4 is greatest", num4)